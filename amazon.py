import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}

r = requests.get("https://www.amazon.fr/dp/B07YFW75X9", headers=headers)

print(r.status_code)

page = BeautifulSoup(r.content, "lxml")

product_title_tag = page.find(id="titleSection")

print(product_title_tag)

f = open("amazon_result.html", "w+")
f.write(str(r.content))
f.close()
