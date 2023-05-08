filename = "popular-names.txt"

# Open the file for reading
with open(filename, 'r') as file:
    # Read the contents of the file
    contents = file.read()

# Replace all occurrences of tab characters with spaces
contents = contents.replace('\t', ' ')

# Open the file for writing
with open(filename, 'w') as file:
    # Write the modified contents back to the file
    file.write(contents)

with open(filename, "r") as file:
    read = file.read()
    
print(read)