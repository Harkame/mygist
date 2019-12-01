import requests
from bs4 import BeautifulSoup
import sys

categories = {
    "all": "all",
    "film_video": "2145",
    "application": "2139",
    "jeux_video": "2142",
    "ebook": "2140",
    "emulation": "2141",
    "gps": "2143",
}

sub_categories = {
    "all": "all",
    "Animation": "2178",
    "Animation Serie": "2179",
    "Concert": "2180",
    "Documentaire": "2181",
    "Emission TV": "2182",
    "Film": "2183",
    "Serie TV": "2184",
    "Spectacle": "2185",
    "Sport": "2186",
    "Video-clips": "2187",
    "Karaoke": "2147",
    "Musique": "2148",
    "Podcast Radio": "2150",
    "Samples": "2149",
    "Autre": "2177",
    "Formation": "2176",
    "Linux": "2171",
    "MacOS": "2172",
    "Smartphone": "2174",
    "Tablette": "2175",
    "Windows": "2173",
    "Autre": "2167",
    "Linux": "2159",
    "MacOS": "2160",
    "Microsoft": "2162",
    "Nintendo": "2163",
    "Smartphone": "2165",
    "Sony": "2164",
    "Tablette": "2166",
    "Windows": "2161",
    "Audio": "2151",
    "Bds": "2152",
    "Comics": "2153",
    "Livres": "2154",
    "Mangas": "2155",
    "Presse": "2156",
    "Emulateurs": "2157",
    "Roms": "2158",
    "Applications": "2168",
    "Cartes": "2169",
    "Divers": "2170",
    "Films": "2189",
    "Hentai": "2190",
    "Images": "2191",
}


def string_to_code():
    pass


session = requests.session()

response = session.get(
    "https://www2.yggtorrent.pe/engine/search?name=walking+dead&description=&file=&uploader=&category=all&sub_category=all&do=search"
)

page = BeautifulSoup(response.content, features="lxml")

option_tag = page.find("select", {"id": "categorie"}).find_all("option")

categories = []

for option in option_tag:
    categories.append({option["value"]: option.text.lower().replace(" ", "_")})

# print(categories)

print("----------------------------")

sub_categories = {}

sub_categories_select = page.find("div", {"id": "sub_categorie_container"}).find_all(
    "select"
)

for sub_categorie_select in sub_categories_select:
    subcop = []
    for sub_categorie_option in sub_categorie_select.find_all("option"):
        print(f"'{sub_categorie_option.text}' : '{sub_categorie_option['value']}', ")
