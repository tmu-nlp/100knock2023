filename = 'neko.txt.mecab'

def extract_phrases(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    phrases = []
    for i in range(1, len(lines)):
        current_line = lines[i - 1].split()
        previous_line = lines[i - 2].split()  
        post_line = lines[i].split() if i > 0 else []

        if current_line[0] == 'の' and current_line[1].split(',')[0] == '助詞':
            if previous_line[1].split(',')[0] == '名詞' and post_line[1].split(',')[0] == '名詞':
                phrase = (previous_line[0], current_line[0], post_line[0].strip())
                phrases.append(phrase)

    with open('phrase.txt', 'w') as output_file:
        for phrase in phrases:
            output_file.write(f"{phrase[0]} {phrase[1]} {phrase[2]}\n")

    print("Extraction complete. Phrases saved in 'phrase.txt'.")


# Usage example
extract_phrases(filename)