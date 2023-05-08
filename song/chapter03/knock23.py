import gzip
import json

filename = './Song/chapter03/enwiki-country.json.gz'

# Open the compressed JSON file
with gzip.open(filename, 'rt') as file:
    # Read each line and parse it as JSON
    for line in file:
        data = json.loads(line)
        
        # Check if the article is about the United Kingdom
        if data['title'] == 'United Kingdom':
            # Extract the section names and levels
            sections = []
            for line in data['text'].split('\n'):
                if line.startswith('='):
                    level = line.count('=') // 2 - 1 # Calculate the section level dividing by 2 (since each section level has two = symbols), and subtracting 1 (since the top-level section has no = symbols).
                    name = line.strip('= ') # Remove the leading and trailing equal signs and spaces
                    sections.append((name, level))

            # Print the section names and levels
            for name, level in sections:
                print('Level {}: {}'.format(level, name))
            break