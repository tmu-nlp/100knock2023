import os

filename_input = "./song/chapter04/neko.txt.mecab"

# Path to output file for verb surface forms
filename_output = "./song/chapter04/surface.txt"

# Open input file and output file
with open(filename_input, "r") as input_file, open(filename_output, "w") as output_file:
    # Loop through each line in the input file
    for line in input_file:
        # Split the line by tab characters to get the columns
        columns = line.strip().split("\t")
        
        # If the line has at least two columns
        if len(columns) >= 2:
            # Get the part of speech tag from the second column
            pos = columns[1].split(",")[0]
            
            # If the part of speech tag is a verb
            if pos == "動詞":
                # Get the surface form from the first column
                surface_form = columns[0]
                
                # Write the surface form to the output file
                output_file.write(surface_form + "\n")

# Print a message to indicate that the operation is complete
print("Verb surface forms extracted and written to " + os.path.abspath(filename_output))