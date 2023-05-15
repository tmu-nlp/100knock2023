import gzip
import json
import re

filename = './song/chapter03/enwiki-country.json.gz'

# Define a regular expression to match the Infobox "country"
infobox_regex = r'{{Infobox country([\s\S]+?)}}'# Matches a string that starts with {{Infobox country and ends with }},

# Define a regular expression to match field names and values
field_regex = r'\|\s*(.+?)\s*=\s*(.+?)\s*(?=\||$)'

# Open the compressed JSON file
with gzip.open(filename, 'rt') as file:
    # Read each line and parse it as JSON
    for line in file:
        data = json.loads(line)

        # Check if the article is about the United Kingdom
        if data['title'] == 'United Kingdom':
            # Extract the Infobox "country"
            infobox_match = re.search(infobox_regex, data['text'])
            
            # Create a dictionary to store the field names and values
            fields = {}

            # Extract the field names and values from the Infobox "country"
            if infobox_match:
                field_matches = re.findall(field_regex, infobox_match.group(1))
                for field_match in field_matches:
                    field_name = field_match[0].strip()
                    field_value = field_match[1].strip()
                    fields[field_name] = field_value

            # Print the dictionary object
            print(fields)
            break   # Stop looping after finding the article