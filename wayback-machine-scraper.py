import requests
from html import unescape

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'
ACCEPT_HEADERS = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'

def fetch_source_from_url(url):
    """
    Fetches the HTML source code of a webpage and cleans it using the html.unescape() function.
    """
    headers = {'User-Agent': USER_AGENT, 'Accept': ACCEPT_HEADERS}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    source_clean = unescape(response.text)
    return source_clean

def perform_archive_discovery(url):
    """
    Performs archive discovery on a webpage using the Wayback Machine's CDX API.
    """
    WAYBACK_MACHINE_URL = 'https://web.archive.org/cdx/search/cdx'
    params = {'url': url, 'output': 'json', 'matchType': 'prefix', 'limit': 5, 'showResumeKey': 'true'}
    response = requests.get(WAYBACK_MACHINE_URL, params=params)
    response.raise_for_status()
    discovery_data = response.json()
    return discovery_data
