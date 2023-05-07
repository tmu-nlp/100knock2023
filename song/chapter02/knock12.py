# Open input file for reading
with open('/home/nevucide/100knock2023/song/chapter02/popular-names.txt', 'r') as file:
    # Open output files for writing
    with open('col1.txt', 'w') as col1_file, open('col2.txt', 'w') as col2_file:
        # Loop through each line in the input file
        for line in file:
            # Split line into columns based on whitespace
            columns = line.split()
            
            # Write the first column to col1.txt
            col1_file.write(columns[0] + '\n')
            # Write the second column to col2.txt
            col2_file.write(columns[1] + '\n')
            