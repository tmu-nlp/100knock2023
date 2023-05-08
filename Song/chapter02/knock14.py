def head(file_path, num_lines):
    #Prints the first num_lines lines of a file to the console.
    with open(file_path, 'r') as f:
        # Loop through the specified number of lines or until the end of the file is reached
        for i in range(num_lines):
            line = f.readline()
            # Print the current line to the console
            print(line.strip())
            
        return
    
head('/home/nevucide/100knock2023/song/chapter02/col2.txt',5)