import json
import pip._vendor.requests 

# Define the base URL for the MediaWiki API
base_url = "https://en.wikipedia.org/w/api.php"

# Define the parameters to send with the API request
params = {
    "action": "query",
    "format": "json",
    "titles": f"File:Flag of United Kingdom.svg",
    "prop": "imageinfo",
    "iiprop": "url"
}

# Send the API request
response = pip._vendor.requests.get(base_url, params=params)

# Parse the JSON response
DATA = json.loads(response.text)

# Extract the URL of the flag image in SVG format
PAGES = DATA['query']['pages']
for page_id, page_info in PAGES.items():
    if 'imageinfo' in page_info:
        flag_url = page_info['imageinfo'][0]['url']
        break

print("URL of the United Kingdom flag in SVG format:", flag_url)