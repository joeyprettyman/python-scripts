import requests
import html

# Get basic cleaned HTML from a given url.
def fetch_source_from_url(url):

    headers = {
        'Host': 'web.archive.org',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    }    

    with requests.Session() as session:
        source_raw = session.get(url)
        source_text = source_raw.text
        source_clean = html.unescape(source_text)

        return source_clean

# Perform initial archive discovery
def perform_archive_discovery(url):
    wayback_machine_url = 'web.archive.org/cdx/search/cdx'
    query = f'url={url}&output=json&matchType=prefix&limit=5&showResumeKey=true'
    full_url = f'https://{wayback_machine_url}?{query}'
    discovery_data = fetch_source_from_url(full_url)

    return discovery_data