col1 = '/home/nevucide/100knock2023/song/chapter02/col1.txt'
col2 = '/home/nevucide/100knock2023/song/chapter02/col2.txt'
join_column = '/home/nevucide/100knock2023/song/chapter02/join_column.txt'

# Open col1.txt and col2.txt for reading
with open(col1, 'r') as col1_file, open(col2, 'r') as col2_file:
    # Open output file for writing
    with open(join_column, 'w') as output_file:
        # Loop through each line in both input files simultaneously
        for col1_line, col2_line in zip(col1_file, col2_file):
            # Remove newline characters from both lines
            col1_line = col1_line.strip()
            col2_line = col2_line.strip()
            # Write the two columns separated by a tab character to the output file
            output_file.write(col1_line + '\t' + col2_line + '\n')
