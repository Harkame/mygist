import requests
from bs4 import BeautifulSoup
import sys
import time
import json
import re
import encodings

categories = [
    {
        "name": "Films & vidéos ",
        "id": "2145",
        "subcategories": [
            {"name": " Game Of Thrones Tendance", "id": ""},
            {"name": "Animation", "id": "2178"},
            {"name": "Animation Série", "id": "2179"},
            {"name": "Concert", "id": "2180"},
            {"name": "Documentaire", "id": "2181"},
            {"name": "Emission TV", "id": "2182"},
            {"name": "Film", "id": "2183"},
            {"name": "Série TV", "id": "2184"},
            {"name": "Spectacle", "id": "2185"},
            {"name": "Sport", "id": "2186"},
            {"name": "Vidéo-clips", "id": "2187"},
            {"name": "eBook ", "id": "all"},
            {"name": "Audio", "id": "2151"},
            {"name": "BDS", "id": "2152"},
            {"name": "Comics", "id": "2153"},
            {"name": "Livres", "id": "2154"},
            {"name": "Manga", "id": "2155"},
            {"name": "Presse", "id": "2156"},
            {"name": "Audio ", "id": "all"},
            {"name": "Karaoké", "id": "2147"},
            {"name": "Musique", "id": "2148"},
            {"name": "Podcast Radio", "id": "2150"},
            {"name": "Samples", "id": "2149"},
            {"name": "Applications ", "id": "all"},
            {"name": "Autre", "id": "2177"},
            {"name": "Formation", "id": "2176"},
            {"name": "Linux", "id": "2171"},
            {"name": "MacOS", "id": "2172"},
            {"name": "Smartphone", "id": "2174"},
            {"name": "Tablette", "id": "2175"},
            {"name": "Windows", "id": "2173"},
            {"name": "Jeux vidéo ", "id": "all"},
            {"name": "Autre", "id": "2167"},
            {"name": "Linux", "id": "2159"},
            {"name": "MacOS", "id": "2160"},
            {"name": "Microsoft", "id": "2162"},
            {"name": "Nintendo", "id": "2163"},
            {"name": "Smartphone", "id": "2165"},
            {"name": "Sony", "id": "2164"},
            {"name": "Tablette", "id": "2166"},
            {"name": "Windows", "id": "2161"},
            {"name": "Émulation ", "id": "all"},
            {"name": "Émulateur", "id": "2157"},
            {"name": "ROM/ISO", "id": "2158"},
            {"name": "GPS ", "id": "all"},
            {"name": "Applications", "id": "2168"},
            {"name": "Cartes", "id": "2169"},
            {"name": "Divers", "id": "2170"},
        ],
    },
    {
        "name": "Films & vidéos ",
        "id": "2145",
        "subcategories": [
            {"name": " Game Of Thrones Tendance", "id": ""},
            {"name": "Animation", "id": "2178"},
            {"name": "Animation Série", "id": "2179"},
            {"name": "Concert", "id": "2180"},
            {"name": "Documentaire", "id": "2181"},
            {"name": "Emission TV", "id": "2182"},
            {"name": "Film", "id": "2183"},
            {"name": "Série TV", "id": "2184"},
            {"name": "Spectacle", "id": "2185"},
            {"name": "Sport", "id": "2186"},
            {"name": "Vidéo-clips", "id": "2187"},
        ],
    },
    {
        "name": "eBook ",
        "id": "2140",
        "subcategories": [
            {"name": "Audio", "id": "2151"},
            {"name": "BDS", "id": "2152"},
            {"name": "Comics", "id": "2153"},
            {"name": "Livres", "id": "2154"},
            {"name": "Manga", "id": "2155"},
            {"name": "Presse", "id": "2156"},
        ],
    },
    {
        "name": "Audio ",
        "id": "2139",
        "subcategories": [
            {"name": "Karaoké", "id": "2147"},
            {"name": "Musique", "id": "2148"},
            {"name": "Podcast Radio", "id": "2150"},
            {"name": "Samples", "id": "2149"},
        ],
    },
    {
        "name": "Applications ",
        "id": "2144",
        "subcategories": [
            {"name": "Autre", "id": "2177"},
            {"name": "Formation", "id": "2176"},
            {"name": "Linux", "id": "2171"},
            {"name": "MacOS", "id": "2172"},
            {"name": "Smartphone", "id": "2174"},
            {"name": "Tablette", "id": "2175"},
            {"name": "Windows", "id": "2173"},
        ],
    },
    {
        "name": "Jeux vidéo ",
        "id": "2142",
        "subcategories": [
            {"name": "Autre", "id": "2167"},
            {"name": "Linux", "id": "2159"},
            {"name": "MacOS", "id": "2160"},
            {"name": "Microsoft", "id": "2162"},
            {"name": "Nintendo", "id": "2163"},
            {"name": "Smartphone", "id": "2165"},
            {"name": "Sony", "id": "2164"},
            {"name": "Tablette", "id": "2166"},
            {"name": "Windows", "id": "2161"},
        ],
    },
    {
        "name": "Émulation ",
        "id": "2141",
        "subcategories": [
            {"name": "Émulateur", "id": "2157"},
            {"name": "ROM/ISO", "id": "2158"},
        ],
    },
    {
        "name": "GPS ",
        "id": "2143",
        "subcategories": [
            {"name": "Applications", "id": "2168"},
            {"name": "Cartes", "id": "2169"},
            {"name": "Divers", "id": "2170"},
        ],
    },
]


def extract_categories():
    global categories
    session = requests.session()

    response = session.get(
        "https://www2.yggtorrent.pe/engine/search?name=walking+dead&description=&file=&uploader=&category=all&sub_category=all&do=search"
    )

    page = BeautifulSoup(response.content, features="lxml")

    left_menu = page.find("div", {"id": "cat"})

    ul_tags = left_menu.find_all("ul")

    for ul_tag in ul_tags:

        category = {}

        a_tags = ul_tag.find_all("a")

        a_index = 0

        for a_tag in a_tags:
            href = a_tag["href"]

            # print(a_tag.text)
            # print(href)

            id_category = substring(href, "category=", "&sub_category=")
            id_subcategory = substring(href, "&sub_category=", "&do=search")

            if id_category is None or id_subcategory is None:
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
    return string.encode().decode("cp1254")


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

    print("---------------------------")
    print(field)
    print(f"{field['name']} : {field['id']}")
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

            with open(f".\\categories\\{subcategory['id']}.json", "w+") as file:
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

                if "id" in json_data:
                    subcategory["fields"].append(json_data)
                else:
                    for json_data_row in json_data:
                        if "id" not in json_data_row:
                            continue

                        subcategory["fields"].append(json_data_row)


def extract_fields_from_files():
    global categories

    for category in categories:
        for subcategory in category["subcategories"]:
            with open(f"categories\\{subcategory['id']}.json") as json_file:
                result = json.load(json_file)

                subcategory["fields"] = []

                for json_data in result:

                    print(subcategory["id"])

                    if "id" in json_data:
                        parsed_field = parse_field(json_data)

                        if parsed_field:
                            subcategory["fields"].append(parsed_field)
                    else:
                        for json_data_row in json_data:
                            if "id" not in json_data_row:
                                continue

                            parsed_field = parse_field(json_data)

                            if parsed_field:
                                subcategory["fields"].append(parsed_field)


# extract_categories()
# print(categories)
print("--------")
# download_fields()
extract_fields_from_files()
print(categories)
with open("categories.json", "w") as fp:
    json.dump(categories, fp)
