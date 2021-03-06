import requests
from bs4 import BeautifulSoup
import sys
import time
import json
import re
import encodings
from unidecode import unidecode
from categories import categories
import unicodedata


def extract_categories():
    global categories
    session = requests.session()

    response = session.get(
        "https://www2.yggtorrent.pe/engine/search?name=walking+dead&description=&file=&uploader=&category=all&sub_category=all&do=search"
    )

    page = BeautifulSoup(response.content, features="lxml")

    left_menu = page.find("div", {"id": "cat"})

    ul_tags = left_menu.find("ul").find_all(
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
    return strip_accents(string.strip().replace(" ", "_")).lower()


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


def parse_option(option):
    if "id" not in option or "name" not in option:
        print("not in")
        return None

    item = {"name": decode(option["name"]), "id": decode(option["id"])}

    if "multiple" in option:
        item["multiple"] = option["multiple"]

    if "values" in option:
        item["values"] = []
        for value in option["values"]:
            item["values"].append(decode(value))

    return item


def download_options():
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


def extract_options():
    global categories

    session = requests.session()

    for category in categories:
        for subcategory in category["subcategories"]:

            response = session.get(
                f"https://www2.yggtorrent.pe/engine/category_fields?id={subcategory['id']}"
            )

            result = response.json()

            subcategory["options"] = []

            for json_data in result:
                if (
                    "id" in json_data
                    and "name" in json_data
                    and json_data["id"] is not None
                    and len(json_data["id"]) > 0
                ):
                    parsed_option = parse_option(json_data)

                    if parsed_option:
                        subcategory["options"].append(parsed_option)
                else:
                    for json_data_row in json_data:
                        if "id" not in json_data_row or len(json_data_row["id"]):
                            continue

                        parsed_option = parse_option(json_data)

                        if parsed_option:
                            subcategory["options"].append(parsed_option)


def extract_options_from_files():
    global categories

    for category in categories:
        for subcategory in category["subcategories"]:
            with open(f"categories\\{subcategory['id']}.json") as json_file:
                result = json.load(json_file)

                subcategory["options"] = []

                for json_data in result:
                    if (
                        "id" in json_data
                        and "name" in json_data
                        and json_data["id"] is not None
                        and len(json_data["id"]) > 0
                    ):
                        parsed_option = parse_option(json_data)

                        if parsed_option:
                            subcategory["options"].append(parsed_option)
                    else:
                        for json_data_row in json_data:
                            if "id" not in json_data_row or len(json_data_row["id"]):
                                continue

                            parsed_option = parse_option(json_data)

                            if parsed_option:
                                subcategory["options"].append(parsed_option)


def strip_accents(text):

    try:
        text = unicode(text, "utf-8")
    except NameError:  # unicode is a default on python 3
        pass

    text = unicodedata.normalize("NFD", text).encode("ascii", "ignore").decode("utf-8")

    return str(text)


"""
extract_categories()

download_options()
extract_options_from_files()

with open("categories.py", "w") as fp:
    json.dump(categories, fp)
"""


def search(parameters):
    id_category = "all"
    id_subcategory = "all"
    options_index = []

    if "category" in parameters:
        for category in categories:
            if parameters["category"] == category["name"]:
                id_category = category["id"]

                if "subcategory" in parameters:
                    for subcategory in category["subcategories"]:
                        if parameters["subcategory"] == subcategory["name"]:
                            id_subcategory = subcategory["id"]

                            if "options" in parameters:
                                for key, values in parameters["options"].items():
                                    for option in subcategory["options"]:
                                        if key == option["name"]:
                                            for searched_value in values:
                                                for index, value in enumerate(
                                                    option["values"]
                                                ):
                                                    if searched_value == value:
                                                        options_index.append(index)

    print(id_category)
    print(id_subcategory)
    print(options_index)


search(
    {
        "category": "films_&_videos",
        "subcategory": "animation",
        "options": {"langue": {"anglais", "vostfr"}},
    }
)

extract_categories()
extract_options_from_files()

with open(f".\\categories.py", "w") as file:
    json.dump(categories, file)
# print(categories["name"])
