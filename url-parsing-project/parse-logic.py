from urllib.parse import urlparse

# Url to be parsed
url = 'http://uSEr.n4m3:p@s$w0rD@www.example.org:80/en_US/locations/us/ny/brooklyn.store_details.html?open="9-5"?rating="good"#fragment'

# Parsed url
parsed_url = urlparse(url)

# Print out the details
print('[Scheme]: ' + parsed_url.scheme) # http
print('[Netloc]: ' + parsed_url.netloc) # uSEr.n4m3:p@s$w0rD@www.example.org:80
print('[Path]: ' + parsed_url.path) # /en_US/locations/us/ny/brooklyn.store_details.html
print('[Query]: ' + parsed_url.query) # open="9-5"?rating="good"
print('[Fragment]: ' + parsed_url.fragment) # fragment
print('[Username]: ' + parsed_url.username) # uSEr.n4m3
print('[Password]: ' + parsed_url.password) # p@s$w0rD
print('[Hostname]: ' + parsed_url.hostname) # www.example.org
print('[Port]: ' + str(parsed_url.port)) # 80