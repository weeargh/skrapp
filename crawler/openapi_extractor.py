"""Detect OpenAPI/Swagger pages and convert their spec to markdown."""
from __future__ import annotations

import json
import logging
import re
from urllib.parse import urljoin, urlparse

import requests
import yaml

logger = logging.getLogger(__name__)

_SWAGGER_UI_SIGNALS = [
    "SwaggerUIBundle",
    "swagger-ui-bundle",
    "swagger-ui.css",
    "swagger-initializer",
]
_REDOC_SIGNALS = [
    "<redoc ",
    "redoc.standalone",
    "ReDoc.init",
]

# Common fallback spec paths to probe
_FALLBACK_SPEC_PATHS = [
    "/openapi.json",
    "/openapi.yaml",
    "/swagger.json",
    "/swagger.yaml",
    "/api-docs",
    "/api-docs.json",
    "/v2/api-docs",
    "/v3/api-docs",
    "/docs/openapi.json",
    "/docs/swagger.json",
]


def detect_openapi_spec_url(html: str, page_url: str) -> str | None:
    """
    Detect if a page is a Swagger UI or Redoc API doc page and return the spec URL.
    Returns None if not detected.
    """
    is_swagger = any(signal in html for signal in _SWAGGER_UI_SIGNALS)
    is_redoc = any(signal in html for signal in _REDOC_SIGNALS)

    if not (is_swagger or is_redoc):
        return None

    logger.info("OpenAPI page detected at %s (swagger=%s, redoc=%s)", page_url, is_swagger, is_redoc)

    # Try to extract spec URL from Redoc element: <redoc spec-url="...">
    m = re.search(r'<redoc[^>]+spec-url=["\']([^"\']+)["\']', html, re.IGNORECASE)
    if m:
        return urljoin(page_url, m.group(1))

    # Try SwaggerUIBundle({ url: "..." })
    m = re.search(r'SwaggerUIBundle\s*\(\s*\{[^}]*\burl\s*:\s*["\']([^"\']+)["\']', html, re.DOTALL)
    if m:
        return urljoin(page_url, m.group(1))

    # Try SwaggerUIBundle({ configUrl: "..." })
    m = re.search(r'configUrl\s*:\s*["\']([^"\']+)["\']', html)
    if m:
        config_url = urljoin(page_url, m.group(1))
        spec_url = _resolve_config_url(config_url)
        if spec_url:
            return urljoin(page_url, spec_url)

    # Try swagger-initializer.js URL attribute
    m = re.search(r'src=["\']([^"\']*swagger-initializer[^"\']*)["\']', html, re.IGNORECASE)
    if m:
        init_url = urljoin(page_url, m.group(1))
        spec_url = _extract_url_from_initializer(init_url)
        if spec_url:
            return urljoin(page_url, spec_url)

    # Try data-url on #swagger-ui div
    m = re.search(r'<div[^>]+id=["\']swagger-ui["\'][^>]*data-url=["\']([^"\']+)["\']', html, re.IGNORECASE)
    if m:
        return urljoin(page_url, m.group(1))

    # Fallback: probe common paths
    base = _base_origin(page_url)
    for path in _FALLBACK_SPEC_PATHS:
        candidate = base + path
        if _is_openapi_url(candidate):
            return candidate

    return None


def fetch_openapi_spec(spec_url: str, page_url: str | None = None) -> dict | None:
    """Fetch a JSON or YAML OpenAPI spec from a URL. Returns parsed dict or None."""
    from urllib.parse import urlparse
    referer = page_url or f"{urlparse(spec_url).scheme}://{urlparse(spec_url).netloc}/"
    try:
        resp = requests.get(spec_url, timeout=30, headers={
            "Accept": "application/json, application/yaml, */*",
            "User-Agent": "Mozilla/5.0 (compatible; SkrappBot/1.0)",
            "Referer": referer,
        })
        resp.raise_for_status()
        content = resp.text.strip()
        # Try JSON first
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            pass
        # Try YAML
        try:
            data = yaml.safe_load(content)
            if isinstance(data, dict):
                return data
        except yaml.YAMLError:
            pass
        logger.warning("Could not parse spec from %s as JSON or YAML", spec_url)
    except Exception as e:
        logger.warning("Failed to fetch OpenAPI spec from %s: %s", spec_url, e)
    return None


def convert_spec_to_markdown(spec: dict) -> str:
    """Convert a parsed OpenAPI 2.x / 3.x spec dict into readable markdown."""
    lines: list[str] = []

    info = spec.get("info", {})
    title = info.get("title", "API Reference")
    version = info.get("version", "")
    description = info.get("description", "")

    lines.append(f"# {title}" + (f" (v{version})" if version else ""))
    lines.append("")

    # Base URL
    if "servers" in spec:  # OAS 3.x
        for server in spec["servers"][:1]:
            url = server.get("url", "")
            desc = server.get("description", "")
            lines.append(f"**Base URL:** `{url}`" + (f" — {desc}" if desc else ""))
        lines.append("")
    elif "host" in spec:  # Swagger 2.x
        scheme = (spec.get("schemes") or ["https"])[0]
        base_path = spec.get("basePath", "/")
        lines.append(f"**Base URL:** `{scheme}://{spec['host']}{base_path}`")
        lines.append("")

    if description:
        lines.append(description.strip())
        lines.append("")

    # Authentication / security schemes
    security_schemes = (
        spec.get("components", {}).get("securitySchemes")  # OAS 3.x
        or spec.get("securityDefinitions")  # Swagger 2.x
        or {}
    )
    if security_schemes:
        lines.append("## Authentication")
        lines.append("")
        for name, scheme in security_schemes.items():
            scheme_type = scheme.get("type", "")
            scheme_in = scheme.get("in", "")
            scheme_name = scheme.get("name", "")
            scheme_desc = scheme.get("description", "")
            detail = f"`{scheme_type}`"
            if scheme_in:
                detail += f" in `{scheme_in}`"
                if scheme_name:
                    detail += f" as `{scheme_name}`"
            lines.append(f"- **{name}**: {detail}" + (f" — {scheme_desc}" if scheme_desc else ""))
        lines.append("")

    # Endpoints
    paths = spec.get("paths", {})
    if paths:
        lines.append("## Endpoints")
        lines.append("")

        # Group by tags
        tag_groups: dict[str, list[tuple[str, str, dict]]] = {}
        for path, path_item in paths.items():
            for method in ("get", "post", "put", "patch", "delete", "head", "options"):
                operation = path_item.get(method)
                if not operation:
                    continue
                tags = operation.get("tags") or ["General"]
                for tag in tags:
                    tag_groups.setdefault(tag, []).append((method.upper(), path, operation))

        for tag, operations in tag_groups.items():
            lines.append(f"### {tag}")
            lines.append("")
            for method, path, operation in operations:
                summary = operation.get("summary", "")
                description = operation.get("description", "")
                operation_id = operation.get("operationId", "")
                deprecated = operation.get("deprecated", False)

                heading = f"#### `{method} {path}`"
                if deprecated:
                    heading += " *(deprecated)*"
                lines.append(heading)
                lines.append("")
                if summary:
                    lines.append(f"**{summary}**")
                    lines.append("")
                if operation_id:
                    lines.append(f"*Operation ID: `{operation_id}`*")
                    lines.append("")
                if description:
                    lines.append(description.strip())
                    lines.append("")

                # Parameters
                params = operation.get("parameters") or path_item.get("parameters") or []
                if params:
                    lines.append("**Parameters:**")
                    lines.append("")
                    for param in params:
                        p_name = param.get("name", "")
                        p_in = param.get("in", "")
                        p_required = param.get("required", False)
                        p_desc = param.get("description", "")
                        schema = param.get("schema", param)
                        p_type = schema.get("type", "")
                        p_format = schema.get("format", "")
                        p_default = schema.get("default")
                        type_str = p_type
                        if p_format:
                            type_str += f"({p_format})"
                        req_str = " *(required)*" if p_required else ""
                        default_str = f", default: `{p_default}`" if p_default is not None else ""
                        lines.append(
                            f"- `{p_name}` ({p_in}, {type_str}{req_str}{default_str}): {p_desc}"
                        )
                    lines.append("")

                # Request body (OAS 3.x)
                request_body = operation.get("requestBody")
                if request_body:
                    rb_desc = request_body.get("description", "")
                    rb_required = request_body.get("required", False)
                    req_str = " *(required)*" if rb_required else ""
                    lines.append(f"**Request Body{req_str}:** {rb_desc}")
                    content = request_body.get("content", {})
                    for media_type, media_obj in list(content.items())[:2]:
                        lines.append(f"- Content-Type: `{media_type}`")
                        schema = media_obj.get("schema", {})
                        schema_str = _summarize_schema(schema, spec)
                        if schema_str:
                            lines.append(f"  - Schema: {schema_str}")
                    lines.append("")

                # Responses
                responses = operation.get("responses", {})
                if responses:
                    lines.append("**Responses:**")
                    lines.append("")
                    for code, resp in responses.items():
                        resp_desc = resp.get("description", "")
                        lines.append(f"- `{code}`: {resp_desc}")
                    lines.append("")

                lines.append("---")
                lines.append("")

    return "\n".join(lines)


# --- helpers ---

def _base_origin(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"


def _is_openapi_url(url: str) -> bool:
    """Return True if the URL returns a valid OpenAPI spec."""
    from urllib.parse import urlparse as _urlparse
    origin = f"{_urlparse(url).scheme}://{_urlparse(url).netloc}/"
    try:
        resp = requests.get(url, timeout=10, headers={
            "Accept": "application/json, */*",
            "User-Agent": "Mozilla/5.0 (compatible; SkrappBot/1.0)",
            "Referer": origin,
        })
        if resp.status_code != 200:
            return False
        data = resp.json()
        return isinstance(data, dict) and ("openapi" in data or "swagger" in data or "paths" in data)
    except Exception:
        return False


def _resolve_config_url(config_url: str) -> str | None:
    """Fetch a Swagger config JSON and extract the spec URL."""
    try:
        resp = requests.get(config_url, timeout=8)
        resp.raise_for_status()
        data = resp.json()
        return data.get("url") or data.get("urls", [{}])[0].get("url")
    except Exception:
        return None


def _extract_url_from_initializer(init_url: str) -> str | None:
    """Fetch swagger-initializer.js and extract the spec URL."""
    try:
        resp = requests.get(init_url, timeout=8)
        resp.raise_for_status()
        m = re.search(r'\burl\s*:\s*["\']([^"\']+)["\']', resp.text)
        return m.group(1) if m else None
    except Exception:
        return None


def _summarize_schema(schema: dict, spec: dict, depth: int = 0) -> str:
    """Return a brief human-readable description of a schema."""
    if "$ref" in schema:
        ref = schema["$ref"]
        name = ref.split("/")[-1]
        if depth == 0:
            resolved = _resolve_ref(ref, spec)
            if resolved:
                return f"`{name}` ({_schema_type_hint(resolved)})"
        return f"`{name}`"
    return _schema_type_hint(schema)


def _schema_type_hint(schema: dict) -> str:
    s_type = schema.get("type", "")
    s_format = schema.get("format", "")
    if s_type == "array":
        items = schema.get("items", {})
        item_hint = _schema_type_hint(items) if items else "any"
        return f"array of {item_hint}"
    if s_type:
        return f"{s_type}({s_format})" if s_format else s_type
    if "properties" in schema:
        return "object"
    return ""


def _resolve_ref(ref: str, spec: dict) -> dict | None:
    """Walk a $ref path like #/components/schemas/Foo."""
    if not ref.startswith("#/"):
        return None
    parts = ref.lstrip("#/").split("/")
    node = spec
    for part in parts:
        if not isinstance(node, dict):
            return None
        node = node.get(part)
    return node if isinstance(node, dict) else None
