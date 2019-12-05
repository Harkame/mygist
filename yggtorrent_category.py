import requests
from bs4 import BeautifulSoup
import sys
import time
import json
import re
import encodings

from categories import categories


def extract_categories():
    global categories
    session = requests.session()

    response = session.get(
        "https://www2.yggtorrent.pe/engine/search?name=walking+dead&description=&file=&uploader=&category=all&sub_category=all&do=search"
    )

    page = BeautifulSoup(response.content, features="lxml")

    left_menu = page.find("div", {"id": "cat"})

    ul_tags = left_menu.find_all(
        "ul"
    )  # , {"style": "color: rgb(201, 193, 189) !important;"})

    for ul_tag in ul_tags:
        category = {}

        a_tags = ul_tag.find_all("a")
        a_index = 0

        for a_tag in a_tags:
            href = a_tag["href"]

            id_category = substring(href, "category=", "&sub_category=")
            id_subcategory = substring(href, "&sub_category=", "&do=search")

            if (
                id_category is None
                or id_subcategory is None
                or len(id_category) == 0
                or len(id_subcategory) == 0
            ):
                continue

            atext = decode(a_tag.text)

            if a_index == 0:
                category["name"] = atext
                category["id"] = id_category
                category["subcategories"] = []
            else:
                subcategory = {"name": atext, "id": id_subcategory}

                category["subcategories"].append(subcategory)

            a_index = a_index + 1

        categories.append(category)


"""
option_tag = page.find("select", {"id": "categorie"}).find_all("option")

categories = []

for option in option_tag:
    categories.append({option["value"]: option.text.lower().replace(" ", "_")})
"""


def decode(string):
    return string.encode().decode("cp1252").strip().replace(" ", "_")


def substring(string, begin, end):
    result = re.search(f"{begin}(.*){end}", string)
    return result.group(1)


def extract_subcategegories():
    global categories

    session = requests.session()

    response = session.get(
        "https://www2.yggtorrent.pe/engine/search?name=walking+dead&description=&file=&uploader=&category=all&sub_category=all&do=search"
    )
    sub_categories = {}

    sub_categories_select = page.find(
        "div", {"id": "sub_categorie_container"}
    ).find_all("select")

    for sub_categorie_select in sub_categories_select:
        subcop = []
        for sub_categorie_option in sub_categorie_select.find_all("option"):
            print(
                f"'{sub_categorie_option.text}' : '{sub_categorie_option['value']}', "
            )


def parse_field(field):
    if "id" not in field or "name" not in field:
        print("not in")
        return None

    item = {"name": decode(field["name"]), "id": decode(field["id"])}

    if "values" in field:
        item["values"] = []
        for value in field["values"]:
            item["values"].append(decode(value))

    return item


def download_fields():
    global categories

    session = requests.session()

    for category in categories:
        for subcategory in category["subcategories"]:

            response = session.get(
                f"https://www2.yggtorrent.pe/engine/category_fields?id={subcategory['id']}"
            )

            result = response.json()

            with open(f".\\categories\\{subcategory['id']}.json", "w") as file:
                json.dump(result, file)


def extract_fields():
    global categories

    session = requests.session()

    for category in categories:
        for subcategory in category["subcategories"]:

            response = session.get(
                f"https://www2.yggtorrent.pe/engine/category_fields?id={subcategory['id']}"
            )

            result = response.json()

            subcategory["fields"] = []

            for json_data in result:

                if "id" in json_data and len(json_data["id"]) > 0:
                    subcategory["fields"].append(json_data)
                else:
                    for json_data_row in json_data:
                        if "id" in json_data and len(json_data_row["id"]) > 0:
                            subcategory["fields"].append(json_data_row)


def extract_fields_from_files():
    global categories

    for category in categories:
        for subcategory in category["subcategories"]:
            with open(f"categories\\{subcategory['id']}.json") as json_file:
                result = json.load(json_file)

                subcategory["fields"] = []

                print(subcategory["id"])
                for json_data in result:
                    print(json_data)

                    if (
                        "id" in json_data
                        and json_data["id"] is not None
                        and len(json_data["id"]) > 0
                    ):
                        parsed_field = parse_field(json_data)

                        if parsed_field:
                            subcategory["fields"].append(parsed_field)
                    else:
                        for json_data_row in json_data:
                            if "id" not in json_data_row or len(json_data_row["id"]):
                                continue

                            parsed_field = parse_field(json_data)

                            if parsed_field:
                                subcategory["fields"].append(parsed_field)


extract_categories()
# print(categories)
# print(categories)

# download_fields()
extract_fields_from_files()

# with open("categories.py", "w") as fp:
#    json.dump(categories, fp)
