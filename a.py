import requests
from yggtorrentscraper import YggTorrentScraper

scraper = YggTorrentScraper(requests.session())

torrents_url = scraper.search(
    {
        "name": "walking dead",
        "category": "films_&_videos",
        "subcategory": "serie_tv",
        "options": {
            "langue": {"francais_(vff/truefrench)", "multi_(francais_inclus)"},
            "qualite": {"bluray_[full]"},
            "saison": {"serie_integrale"},
        },
    }
)

for torrent_url in torrents_url:
    print(torrent_url)
    scraper.download_from_torrent_url(torrent_url)
