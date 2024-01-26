import sys
from pathlib import Path

def invert_sentence(sentence):
    if len(sentence) == 1:
        return sentence
    else:
        return sentence[-1] + invert_sentence(sentence[0:-1])


def read_file(file_name):
    current_directory = Path.cwd()
    file_path = current_directory / file_name
    # print(current_directory)
    cypher_list = []
    with file_path.open("r") as text_file:
        for line in text_file:
            get_sentence = line.strip()
            cypher_list.append(invert_sentence(get_sentence))
    print(cypher_list)
    return cypher_list
    

def main():
    a_file = "oldtext.txt"
    cypher_list = read_file(a_file)

main()
