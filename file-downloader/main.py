from dl_urls import urls as urls
import requests
import numpy as np
import time
import urllib

# Let's create 2 containers for good & bad urls.
good_links = []
bad_links = []

#---------------------------------------------------
# Values you may change.
#---------------------------------------------------
# Set output & logs directory paths.
files_dir = './output/files/'
logs_dir = './output/logs/'

# Success and failure file names.
success_file_name = 'success.txt'
failure_file_name = 'failure.txt'

# Format for use later.
success_file_name = logs_dir + success_file_name
failure_file_name = logs_dir + failure_file_name

# Would you like to follow redirected URLs?
redirects = True

# Delay between pulls.
# Randomization min/max values.
min_val = 1
max_val = 2
#---------------------------------------------------



#---------------------------------------------------
# Header Values
#---------------------------------------------------
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
}




#---------------------------------------------------
# Values you MAY NOT change.
#---------------------------------------------------
# Define important variables
ConnectTimeout = requests.ConnectTimeout
HTTPError = requests.HTTPError
ReadTimeout = requests.ReadTimeout
Timeout = requests.Timeout
ConnectionError = requests.ConnectionError

# Let us know the process is starting.
print('Starting...')

# Now lets iterate through each URL in the dl_urls.py file.
for id, url in enumerate(urls):

    #---------------------------------------------------
    # Random Delay Function
    #---------------------------------------------------
    # Helps try not to get banned.
    random_num = np.random.randint(low=min_val, high=max_val, size=1)
    #random_delay = int(random_num)
    random_delay = 0.25

    # Stringify ID
    id = str(id)

    #---------------------------------------------------
    # Create a contextual manager with a request.
    #---------------------------------------------------
    with requests.Session() as session:

        # Initiate a random sleep before requesting again.
        #time.sleep(random_delay)

        # Try the normal prodecure
        try:

            # Initiate contact with the destination server.
            raw_response = session.get(url, timeout=5.0, headers=headers, allow_redirects=redirects)
            #raw_response = session.get(url, timeout=random_delay, allow_redirects=redirects)

            # With headers below...
            # raw_response = session.get(url, headers=headers, timeout=random_delay, allow_redirects=redirects)

            # Status code
            status_code = raw_response.status_code

            # Establish the delay time total.
            delay_time_total = str(random_delay)

            # If a status code is even returned...
            if status_code:
                
                # Then if it's successful (aka 200)
                if status_code == 200:

                    # Add to the good_links container.
                    good_links.append(url)

                    # Get only the filename portion from the url.
                    file_name = url.split('/')
                    file_name = file_name[-1]

                    # Does ? mark exist in the url?
                    qmark_found = file_name.find('?')

                    # If a qmark is even found...
                    if qmark_found:
                        
                        # If the question mark is found return only
                        # the file name instead of the entire parameters
                        # fragments, queries, etc.
                        if qmark_found != -1:
                            file_name = file_name.partition('?')
                            file_name = file_name[0]

                    # Print out success info to the console.
                    print('🆔 ' + id + ' | ⌛ ' + delay_time_total + 's | ✅ ' + url)

                    # File destination
                    file_destination = files_dir + file_name

                    # Perform the request
                    urllib.request.urlretrieve(url, file_destination)

                # If the file ISN'T available...
                else:

                    # Add to the bad_links container.
                    bad_links.append(url)

                    # Print out failure info to the console.
                    print('🆔 ' + id + ' | ⌛ ' + delay_time_total + 's | ❌ ' + url)

        # If error occurs, catch it, ignore it, and continue.
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
            pass


    # Write good and bad files.
    good_file = open(success_file_name, 'w')
    bad_file = open(failure_file_name, 'w')

    # Write the lines themselves.
    for urls in good_links:
        links = urls + '\n'
        good_file.write(links)

    for urls in bad_links:
        links = urls + '\n'
        bad_file.write(links)

    # Close the files.
    good_file.close()
    bad_file.close()