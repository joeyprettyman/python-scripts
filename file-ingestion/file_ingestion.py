from os import sep, path, curdir
import requests
import urllib
from urllib.parse import urlparse
from headers import default
from functions.http_codes import allowable_codes, forbidden_codes
from functions.tlds_list import tlds

# Let us know our script is beginning.
print('Starting...')

# =======================================================================

# Set directory names and their locations.
directories = {
    'root' : curdir,
    'downloads' : 'downloads',
    'logs' : 'logs',
    'example' : 'example/example',
}

# For each directory in dictionary above get the
# full path then add a trailing [/] slash suffix.
for directory in directories:
    this_dir = directories[directory]
    this_dir_path = path.abspath(this_dir)
    directories[directory] = f'{this_dir_path}{sep}'

# Assign folders to variables.
root_dir = directories['root']
downloads_dir = directories['downloads']
logs_dir = directories['logs']

# Assign files to variables.
ingest_file = f'{root_dir}ingest.txt'
log_file = f'{logs_dir}log.txt'

# =======================================================================

# Ingestion container
ingest_container = []

# Open the ingest file.
with open(ingest_file, 'r') as ingested_file:

    # Begin reading line-by-line.
    lines = ingested_file.readlines()

    # Remove wspace then add to ingest_container.
    for line in lines:
        clean_line = line.strip()
        ingest_container.append(clean_line)

# =======================================================================

# For each url in the ingest_container...
for ingested_url in ingest_container:

    # Begin a session (context manager)
    with requests.Session() as session:

        # Import headers.
        headers = default.headers

        # For this session attempt to retrieve the ingested_url.
        raw_response = session.get(ingested_url, timeout=5.0, headers=headers, allow_redirects=True)

        # Response status code.
        status_code = raw_response.status_code

        # If we got any response at all...
        if status_code:
            
            # If response is bad, log it and continue.
            if status_code in forbidden_codes:
                print(f'❌ {status_code} - {ingested_url} bad response')
                continue
            
            # If response is good, download the file and log it.
            if status_code in allowable_codes:
                
                # Parse the url for use later.
                my_url = urlparse(raw_response.url)

                if my_url.path == '/':
                    print(f'👎 {status_code} - {ingested_url} url path is only slash.')
                    continue
                
                # Get last portion of url after /.
                file_name = my_url.path.split('/')[-1]

                if file_name.find('.') == -1:
                    print(f'🚩 {status_code} - {ingested_url} no period.')
                    continue
                
                else:
                    print(f'✅ {status_code} - {ingested_url} success!')
                    file_dest = f'{downloads_dir}{file_name}'
                    urllib.request.urlretrieve(ingested_url, file_dest)

# Let us know our script is done.
print('Fin.')