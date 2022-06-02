import re
import time
import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# droplink url
url = ""

# ==============================================
    
def droplink_bypass(url):
    DOMAIN = 'https://yoshare.net'
    link = link.replace("droplink.com", "droplink.co")
    client = cloudscraper.create_scraper(interpreter='nodejs', allow_brotli=False)
    res = client.get(url)

    h = {'referer': DOMAIN}
    res = client.get(url, headers=h)

    bs4 = BeautifulSoup(res.content, 'lxml')
    inputs = bs4.find_all('input')
    data = { input.get('name'): input.get('value') for input in inputs }

    h = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-requested-with': 'XMLHttpRequest'
    }
    p = urlparse(url)
    final_url = f'{p.scheme}://{p.netloc}/links/go'

    time.sleep(3.1)
    res = client.post(final_url, data=data, headers=h).json()

    return res["url"]

# ==============================================

print(droplink_bypass(url))
