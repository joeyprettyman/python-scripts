import requests
import html
import json
import csv
import re
import random
import time


# Get basic cleaned HTML from a given url.
def fetch_source_from_url(url):

    headers = {
        "Host": "web.archive.org",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    }

    with requests.Session() as session:
        source_raw = session.get(url)
        source_text = source_raw.text
        source_clean = html.unescape(source_text)

        return source_clean


# Perform initial archive discovery
def perform_archive_discovery(url):
    wayback_machine_url = "web.archive.org/cdx/search/cdx"
    query = f"url={url}&output=json&matchType=prefix&limit=5&showResumeKey=true"
    full_url = f"https://{wayback_machine_url}?{query}"
    discovery_data = fetch_source_from_url(full_url)

    return discovery_data


# Write json data to a file.
def write_json_to_csv(filename, data):
    json_datas = json.loads(data)
    with open(filename, mode="w", encoding="utf8", newline="") as csv_file:
        output = csv.writer(csv_file)
        for json_data in json_datas:
            output.writerow(json_data)


# Write data to a file.
def write_data_to_csv(filename, datas):
    with open(filename, mode="w", encoding="utf8", newline="") as csv_file:
        output = csv.writer(csv_file)
        for data in datas:
            output.writerow([data])


# Load the data?
def load_data(filename):
    with open(filename, mode="r", encoding="utf8", newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",", quotechar='"')

        container = []

        for row in csv_reader:
            container.append(row)

        return container


def extract_month(timestamp):
    timestamp = timestamp[4:-8].lstrip("0")

    # Month handler
    months = {
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }

    for month in months:
        if timestamp == month:
            return months[month]


def extract_day(timestamp):
    return timestamp[6:8]


def extract_year(timestamp):
    return timestamp[:4]


def date_get(format, timestamp):

    if format == "month":
        value = extract_month(timestamp)
    if format == "day":
        value = extract_day(timestamp)
    if format == "year":
        value = extract_year(timestamp)

    return value


def parse_discovered_data(datas):
    container = []
    for data in datas[1:]:
        urlkey = data[0]
        timestamp = data[1]
        original = data[2]
        mimetype = data[3]
        statuscode = data[4]
        digest = data[5]
        length = data[6]

        url = urlkey.split(")")[0]
        url = url.split(",")

        url = f"https://web.archive.org/web/{timestamp}/{url[1]}.{url[0]}"

        container.append(url)

    return container


def perform_initial_scrape(urls):
    print(f"✅ Starting...")
    start = time.time()

    with open("./output/3_links.csv", mode="a", encoding="utf8") as file:
        for position, url in enumerate(urls):
            temp = ", ".join(url)

            if temp:
                print(f"\t🔗 Fetching [{position+1}] \x1b[6;30;42m{temp}\x1b[0m")
                source = fetch_source_from_url(temp)
                links = re.findall(r'href="([^"]*?)"', source)

                for link in links:
                    file.write(f'"{link}"\n')
            delay = random.randint(1, 2)
            time.sleep(delay)
    finish = time.time()
    total = round(finish - start, 3)

    print(f"🏁 Finished!")
    print(f"TOTAL: {total}ms")
