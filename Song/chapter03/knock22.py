import gzip
import json

filename = './song/chapter03/enwiki-country.json.gz'

# Open the compressed JSON file
with gzip.open(filename, 'rt') as file:
    # Read each line and parse it as JSON
    for line in file:
        data = json.loads(line)
        
        # Check if the article is about the United Kingdom
        if data['title'] == 'United Kingdom':
            # Extract the categories
            categories = []
            for line in data['text'].split('\n'):
                if line.startswith('[[Category:'):
                    categories.append(line[11:-2])
            
            # Print the categories
            print('Categories:', categories)
            break #Stop looping after finding the article