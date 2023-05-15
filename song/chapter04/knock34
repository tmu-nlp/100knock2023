filename = "/home/nevucide/komachi_lab/100knock2023/song/chapter04/neko_noen.txt.mecab"

sentence = []

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
            sentence.append(inform)
            
def extract_longest_noun_phrase(sentence):
    noun_phrase = []
    longest_noun_phrase = []

    for word in sentence:
        if word['pos'] == '名詞':
            noun_phrase.append(word)
        else:
            if len(noun_phrase) > len(longest_noun_phrase):
                longest_noun_phrase = noun_phrase
            noun_phrase = []

    # Check if the last noun phrase is the longest
    if len(noun_phrase) > len(longest_noun_phrase):
        longest_noun_phrase = noun_phrase

    return longest_noun_phrase

def extract_and_strip_values(dictionary_list):
    stripped_values = []

    for dictionary in dictionary_list:
        if dictionary:
            first_value = next(iter(dictionary.values()))
            stripped_value = first_value.strip()
            stripped_values.append(stripped_value)

    return stripped_values

def extract_and_join_elements(input_list):
    joined_string = ''.join(str(element) for element in input_list)
    return joined_string

dic = extract_longest_noun_phrase(sentence)
stripped_values = extract_and_strip_values(dic)
result = extract_and_join_elements(stripped_values)

print(result)



