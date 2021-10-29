# Scrapy settings for zipfiles project

BOT_NAME = 'zipfiles'

SPIDER_MODULES = ['zipfiles.spiders']
NEWSPIDER_MODULE = 'zipfiles.spiders'
ITEM_PIPELINES = {'zipfiles.pipelines.ZipfilesPipeline': 1}
FILES_STORE = 'downloads'
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
    'Accept-Language': 'en',
    'Referer': 'https://www.nirsoft.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}


ROBOTSTXT_OBEY = True

# Slowdown the download speed so that site is not 
# overloaded with lot of requests
# AUTOTHROTTLE_ENABLED = True
