import requests
import csv
import time
import random

headers = {
    'Host': 'invisioncommunity.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
}

with open('invision_people.csv', mode='a', encoding='utf8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for i in range(11558, 11600):
        url = f'https://invisioncommunity.com/profile/{i}-{i}/'
        with requests.Session() as session:
            response = session.get(url, headers=headers)
            my_url = response.url
            print(my_url)
            writer.writerow([my_url])
        time.sleep(random.uniform(0.25, 0.50))
