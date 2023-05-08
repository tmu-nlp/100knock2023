import gzip
import json
import re

filename = './song/chapter03/enwiki-country.json.gz'

# Define a regular expression to match media file links
media_regex = r'\[\[File:([^\[\]\|\{\}]+)' #This pattern ensures that we match the filename only, and not any additional information such as captions or alternative text.

# Open the compressed JSON file
with gzip.open(filename, 'rt') as file:
    # Read each line and parse it as Json
    for line in file:
        data = json.loads(line)

        # Check if the article is about the United Kingdom
        if data['title'] == 'United Kingdom':
            # Extract the media file links
            media_links = re.findall(media_regex, data['text'])

            # Print the media file links
            for link in media_links:
                print(link)
            break