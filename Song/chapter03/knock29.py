import json
import pip._vendor.requests 

# Define the base URL for the MediaWiki API
base_url = "https://en.wikipedia.org/w/api.php"

# Define the name of the country whose flag we want to retrieve
country_name = "United Kingdom"

# Define the parameters to send with the API request
params = {
    "action": "query",
    "format": "json",
    "titles": f"File:Flag of {country_name}.svg",
    "prop": "imageinfo",
    "iiprop": "url"
}

# Send the API request
response = pip._vendor.requests.get(base_url, params=params)

# Parse the JSON response
json_data = json.loads(response.text)

# Extract the URL of the flag image in SVG format
pages = json_data['query']['pages']
for page_id, page_info in pages.items():
    if 'imageinfo' in page_info:
        flag_url = page_info['imageinfo'][0]['url']
        break

print("URL of the United Kingdom flag in SVG format:", flag_url)