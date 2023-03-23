import functions

# Only the domain (hostname) here please.
domain = 'forums.invisionpower.com'

"""
Perform the intial discovery process by 
requesting all historical data from the wayback
machine for the domain specified above.
"""
discovery_file = './output/1_discovery_data.csv'
discovery_data = functions.perform_archive_discovery(domain)
#functions.write_json_to_csv(discovery_file, discovery_data)

"""
Now that the initial discovery has been performed
we will want to parse that lovely discovery data
for our spider to begin crawling later.
"""
#parsed_file = './output/2_parsed_data.csv'
#loaded_data = functions.load_data(discovery_file)
#parsed_data = functions.parse_discovered_data(loaded_data)
#functions.write_data_to_csv(parsed_file, parsed_data)

"""
Now we will load the urls and begin prepping
for scraping. The step before should be about
parsing the data and formatting it the way we
want it to be before leaving. Aka pre-flight.
"""
#initial_scrape_file = './output/3_initial_scrape_data.csv'
#initial_scrape_data = functions.load_data(parsed_file)
#functions.perform_initial_scrape(initial_scrape_data)

print(discovery_data)