"""Scrapy settings for the docs crawler."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import settings as app_settings

BOT_NAME = 'docscrawler'

SPIDER_MODULES = ['crawler']
NEWSPIDER_MODULE = 'crawler'

USER_AGENT = app_settings.CRAWLER_USER_AGENT

ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS = app_settings.CRAWLER_CONCURRENT_REQUESTS

DOWNLOAD_DELAY = app_settings.CRAWLER_DOWNLOAD_DELAY

CONCURRENT_REQUESTS_PER_DOMAIN = 16

COOKIES_ENABLED = True

TELNETCONSOLE_ENABLED = False

DEPTH_LIMIT = app_settings.CRAWLER_DEPTH_LIMIT

CLOSESPIDER_PAGECOUNT = app_settings.MAX_PAGES_LIMIT

DOWNLOAD_TIMEOUT = 30

RETRY_TIMES = 2
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]

HTTPERROR_ALLOWED_CODES = [403, 404, 429, 500, 502, 503, 504]

ITEM_PIPELINES = {
    'crawler.pipelines.TextExtractionPipeline': 100,
    'crawler.pipelines.BlockingDetectionPipeline': 200,
    'crawler.pipelines.JSONLWriterPipeline': 300,
}

DOWNLOADER_MIDDLEWARES = {
    'crawler.middlewares.BlockingSignalMiddleware': 543,
}

LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'
