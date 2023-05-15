filename = "/home/nevucide/komachi_lab/100knock2023/song/chapter04/neko.txt.mecab"

mecab_dictionary = []

# Open input file and output file
with open(filename, "r") as input_file:
    # Loop through each line in the input file
    for line in input_file:
        # Split the line by tab characters to get the columns
        columns = line.strip().split("\t")
              # If the line has at least two columns
        if len(columns) >= 2:
        # Get the part of speech tag from columns
            surface = columns[0]

            pos = columns[1].split(',')[0]
            pos1 = columns[1].split(',')[1]
            base = columns[1].split(',')[5]
        
            inform = {'surface':surface,
                      'base' : base,
                      'pos' : pos,
                     'pos1' : pos1
                      }
            mecab_dictionary.append(inform)
            
            print(mecab_dictionary)