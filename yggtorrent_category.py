import requests
from bs4 import BeautifulSoup

session = requests.session()

response = session.get(
    "https://www2.yggtorrent.pe/engine/search?name=walking+dead&description=&file=&uploader=&category=all&sub_category=all&do=search"
)

page = BeautifulSoup(response.content, features="lxml")

options = page.find("select", {"id": "categorie"}).find_all("option")

categories = []

for option in options:
    categories.append(option["value"])

print(categories)

subcat = []

subc_selects = page.find("div", {"id": "sub_categorie_container"}).find_all("select")

for subc_select in subc_selects:
    for subcoption in subc_select.find_all("option"):
        subcat.append(subcoption["value"])

print(subcat)

"""
all=all
movie_and_video=2145
category=audio2139
application=2144
video_game=2142
ebook=2140
emulation=2141
gps=2143




		<li class="film">
			<ul>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2145&sub_category=all&do=search">Films & vidéos <span class="ico_film"></span></a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=game+of+thrones&description=&file=&uploader=&category=all&sub_category=&do=search&order=desc&sort=publish_date" style="color: #f1f1f1; font-weight: bold;"> Game Of Thrones <small style="color: #fd5656; font-size: 8px; font-family: verdana; text-transform: uppercase;">Tendance</small></a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2145&sub_category=2178&do=search">Animation</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2145&sub_category=2179&do=search">Animation Série</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2145&sub_category=2180&do=search"">Concert</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2145&sub_category=2181&do=search"">Documentaire</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2145&sub_category=2182&do=search"">Emission TV</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2145&sub_category=2183&do=search"">Film</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2145&sub_category=2184&do=search"">Série TV</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2145&sub_category=2185&do=search"">Spectacle</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2145&sub_category=2186&do=search"">Sport</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2145&sub_category=2187&do=search"">Vidéo-clips</a></li>
			</ul>
		</li>
		<li class="livre">
			<ul>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2140&sub_category=all&do=search">eBook <span class="ico_book"></span></a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2140&sub_category=2151&do=search">Audio</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2140&sub_category=2152&do=search">BDS</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2140&sub_category=2153&do=search">Comics</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2140&sub_category=2154&do=search">Livres</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2140&sub_category=2155&do=search">Manga</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2140&sub_category=2156&do=search">Presse</a></li>
			</ul>
		</li>
		<li class="audio">
			<ul>

				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2139&sub_category=all&do=search">Audio <span class="ico_music"></span></a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2139&sub_category=2147&do=search">Karaoké</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2139&sub_category=2148&do=search">Musique</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2139&sub_category=2150&do=search">Podcast Radio</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2139&sub_category=2149&do=search">Samples</a></li>
			</ul>
		</li>
				<li class="app">
			<ul>

				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2144&sub_category=all&do=search">Applications <span class="ico_windows"></span></a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2144&sub_category=2177&do=search">Autre</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2144&sub_category=2176&do=search">Formation</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2144&sub_category=2171&do=search">Linux</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2144&sub_category=2172&do=search">MacOS</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2144&sub_category=2174&do=search">Smartphone</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2144&sub_category=2175&do=search">Tablette</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2144&sub_category=2173&do=search">Windows</a></li>
			</ul>
		</li>
		<li class="jeu">
			<ul>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2142&sub_category=all&do=search">Jeux vidéo <span class="ico_gamepad"></span></a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2142&sub_category=2167&do=search">Autre</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2142&sub_category=2159&do=search">Linux</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2142&sub_category=2160&do=search">MacOS</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2142&sub_category=2162&do=search">Microsoft</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2142&sub_category=2163&do=search">Nintendo</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2142&sub_category=2165&do=search">Smartphone</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2142&sub_category=2164&do=search">Sony</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2142&sub_category=2166&do=search">Tablette</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2142&sub_category=2161&do=search">Windows</a></li>
			</ul>
		</li>
		<li class="emu">
			<ul>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2141&sub_category=all&do=search">Émulation <span class="ico_gamepad"></span></a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2141&sub_category=2157&do=search">Émulateur</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2141&sub_category=2158&do=search">ROM/ISO</a></li>
			</ul>
		</li>
		<li class="gps">
			<ul>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2143&sub_category=all&do=search">GPS <span class="ico_map"></span></a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2143&sub_category=2168&do=search">Applications</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2143&sub_category=2169&do=search">Cartes</a></li>
				<li><a  href="https://www2.yggtorrent.pe/engine/search?name=&description=&file=&uploader=&category=2143&sub_category=2170&do=search">Divers</a></li>
			</ul>
		</li>
"""
