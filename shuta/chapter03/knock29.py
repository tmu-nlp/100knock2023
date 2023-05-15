#29
import requests

S = requests.Session()
URL = 'https://en.wikipedia.org/w/api.php'

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:{}".format('Flag of the United Kingdom.svg'),
    "iiprop": "url" 
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    print(v['imageinfo'][0]['url'])