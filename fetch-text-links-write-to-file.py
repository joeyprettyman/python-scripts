import requests
import re


BASE_URL = 'https://www.ietf.org/rfc/'
LINK_REGEX = r'href="(.+\.txt)"'


try:
    # Make a request to the base URL
    response = requests.get(BASE_URL)
    response.raise_for_status()

    # Extract all links to .txt files
    links = re.findall(LINK_REGEX, response.text)

    # Write links to a file
    with open('text_files.txt', 'w') as file:
        for link in links:
            url = BASE_URL + link
            file.write(url + '\n')

except requests.exceptions.RequestException as e:
    print(f'Error occurred: {e}')