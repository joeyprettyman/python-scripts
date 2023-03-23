import requests
import html
from pyquery import PyQuery as pq
import time
import csv
import random

# Headers
headers = {
    'Host' : 'invisioncommunity.com',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
}

i = 11558

while i < 1_000_000_000:

    url = f'https://invisioncommunity.com/profile/{i}-{i}/'

    with open('invision_people.csv', mode='a', encoding='utf8', newline='') as file:
        with requests.Session() as session:
            my_url = session.get(url, headers=headers).url
            print(my_url)
            file.write(f'{my_url}\n')            
    
    i += 1
    #delay = random.randint(0.25,0.50)
    #time.sleep(delay)