import logging
import re
import timeit
from pathlib import Path


# Set up logging configuration to display log messages on the console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)

# List of filenames to search for the string "Gregorio"
list_dir = [
    'rfc-ref.txt',
    'rfc3164.txt',
    'rfc4287.txt',
    'rfc4709.txt',
    'rfc5023.txt',
    'rfc5785.txt',
    'rfc5829.txt',
    'rfc5988.txt',
    'rfc5995.txt',
    'rfc6272.txt'
]


# Function to search a file for the string "Gregorio" and return True if found, False otherwise
def search_file(filename):
    with open(filename, mode='r', encoding='ISO-8859-1') as file:
        content = file.read()
        if re.search('Gregorio', content):
            # Log a message indicating that "Gregorio" was found in the file
            logging.info(f'✅ {filename}')
            return True
        else:
            # Log a message indicating that "Gregorio" was NOT found in the file
            logging.info(f'❌ {filename}')
            return False


# Main program
def main():
    # Start the timer
    start_time = timeit.default_timer()

    # Initialize lists to store the filenames of successful and unsuccessful searches
    success_files = []
    failure_files = []

    # Iterate over each filename in the list_dir and search for the string "Gregorio" in each file
    for filename in list_dir:
        # Resolve the filename to a path object
        path = Path(filename).resolve()

        # Log a message indicating which file is being searched
        logging.info(f'Searching for "Gregorio" in {filename}...')

        # Start the timer for this search
        t1 = timeit.default_timer()

        # Search the file for the string "Gregorio"
        if search_file(path):
            success_files.append(str(path))
        else:
            failure_files.append(str(path))

        # Stop the timer for this search and log the elapsed time
        t2 = timeit.default_timer()
        logging.info(f'Search completed in {t2 - t1:.6f} seconds')

    # Write the filenames of successful and unsuccessful searches to separate text files
    with open('success.txt', 'w') as file:
        file.write('\n'.join(success_files))
    with open('failures.txt', 'w') as file:
        file.write('\n'.join(failure_files))

    # Stop the timer and log the total elapsed time for all searches
    end_time = timeit.default_timer()
    total_time = end_time - start_time
    logging.info(f'Search completed in {total_time:.6f} seconds')


# Call the main program if this script is run as the main module
if __name__ == '__main__':
    main()
