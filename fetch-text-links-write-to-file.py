import requests
import re

# Which url do we want to scrape?
url = 'https://www.ietf.org/rfc/'

# Make request, scrape for a hrefs (links).
# But specifically ones with a .txt file ext.
raw_response = requests.get(url)
text = raw_response.text
links = re.findall(r'href="([^"]*?.txt)"', text)

# Write the link to each txt file in a txt file.
file = open('text_files.txt', 'w')
with file as new_file:
    for link in links:
        link = f'https://www.ietf.org/rfc/{link}'
        new_file.write(f'{link}\n')