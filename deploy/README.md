# Skrapp Deploy

This repo includes deploy artifacts for a simple Ubuntu host running:

- `gunicorn` for the Flask app
- `systemd` for process management
- `nginx` as the HTTPS reverse proxy

Files:

- `deploy/skrapp-web.service`
- `deploy/skrapp-worker.service`
- `deploy/skrapp-nginx.conf`
- `deploy/skrapp.env.example`

## 1. Clone the app

```bash
sudo rm -rf /opt/skrapp
sudo git clone https://github.com/weeargh/skrapp.git /opt/skrapp
cd /opt/skrapp
python3 -m venv .venv
./.venv/bin/pip install -U pip
./.venv/bin/pip install -r requirements.txt
./.venv/bin/playwright install chromium
```

## 2. Create runtime directories

```bash
sudo mkdir -p /etc/skrapp
sudo mkdir -p /var/lib/skrapp/data
sudo mkdir -p /var/lib/skrapp/out
sudo cp deploy/skrapp.env.example /etc/skrapp/skrapp.env
sudo chmod 640 /etc/skrapp/skrapp.env
```

If your host has a dedicated app user, adjust ownership for that user. The shipped systemd units do not hard-code a Unix account, so they also work on hosts that do not have `www-data`.

## 3. Install systemd units

```bash
sudo cp deploy/skrapp-web.service /etc/systemd/system/skrapp-web.service
sudo cp deploy/skrapp-worker.service /etc/systemd/system/skrapp-worker.service
sudo systemctl daemon-reload
sudo systemctl enable skrapp-web.service
sudo systemctl enable skrapp-worker.service
sudo systemctl restart skrapp-web.service
sudo systemctl restart skrapp-worker.service
sudo systemctl status skrapp-web.service --no-pager
sudo systemctl status skrapp-worker.service --no-pager
```

## 4. Install nginx

```bash
sudo apt-get update
sudo apt-get install -y nginx certbot python3-certbot-nginx
sudo cp deploy/skrapp-nginx.conf /etc/nginx/sites-available/skrapp
sudo ln -sf /etc/nginx/sites-available/skrapp /etc/nginx/sites-enabled/skrapp
sudo rm -f /etc/nginx/sites-enabled/default
```

Edit `/etc/nginx/sites-available/skrapp` if your certificate path is different.

## 5. Install TLS certificate

Run this after DNS for `skrapp.swnds.com` points at the server:

```bash
sudo certbot --nginx -d skrapp.swnds.com
```

If certbot rewrites the server block, keep these properties in place:

- `listen 443 ssl http2;`
- `gzip on;`
- the static asset cache block for `css`, `js`, `svg`, `ico`, and images
- `proxy_pass http://127.0.0.1:8080;`

## 6. Validate nginx and reload

```bash
sudo nginx -t
sudo systemctl reload nginx
curl -I https://skrapp.swnds.com/
curl -I https://skrapp.swnds.com/css/style.css
curl -I https://skrapp.swnds.com/js/app.js
curl -I https://skrapp.swnds.com/favicon.svg
```

Expected behavior:

- `/` and `/status` should return `Cache-Control: public, max-age=0, no-store`
- static assets should return `Cache-Control: public, max-age=86400`
- nginx should terminate TLS and speak HTTP/2 to the browser

## 7. Update deploy

```bash
cd /opt/skrapp
git fetch origin
git checkout main
git pull
./.venv/bin/pip install -r requirements.txt
sudo systemctl restart skrapp-web.service
sudo systemctl restart skrapp-worker.service
```

## Logs

```bash
journalctl -u skrapp-web.service -f
journalctl -u skrapp-worker.service -f
sudo tail -f /var/log/nginx/access.log /var/log/nginx/error.log
```
