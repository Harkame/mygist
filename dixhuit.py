import time

import scamnumberscraper
import json

scraper = scamnumberscraper.DixHuitScraper()

first = scraper.page(1)[0]

print(first)

numbers = []


for index in range(1, scraper.count() + 1):
    page = scraper.page(index)
    numbers += page
    time.sleep(0.5)
    exit()

print(numbers.length)

with open("dixhuit.json", "w") as file:
    json.dump(numbers, file)
