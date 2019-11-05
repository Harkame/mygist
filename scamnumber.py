import json
from scrapers import DixHuitScraper
import time

"""
scraper = DixHuitScraper()

start = None
numbers = []
missing_pages = []

start = scraper.page(0)[0]

page_counter = scraper.count()

for index in range(0, page_counter):
    try:
        numbers.extend(scraper.page(index))
        print(f"{index} - {page_counter}")
        time.sleep(0.5)
    except ConnectionError:
        missing_pages.append(index)

with open("./dixhuit.json", "w+") as out_file:
    json.dump(numbers, out_file)

print(f"start : {start}")

print(f"missing_pages : {missing_pages}")

"""

filtered_numbers = []

with open("dixhuit.json") as json_file:
    numbers = json.load(json_file)

    for number in numbers:

        if len(number) != 10:
            continue

        for char in number:
            if not char.isdigit():
                continue

        if number[0] != "0":
            continue

        if number[0] == "0" and number[1] == "0":
            continue

        if number.count(number[0]) == len(number):
            continue

        filtered_numbers.append(number)

    print(f"numbers : {len(numbers)}")
    print(f"filtered_numbers : {len(filtered_numbers)}")

    with open("./filtered_dixhuit.json", "w+") as out_file:
        json.dump(filtered_numbers, out_file)
