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
    # print(cypher_list)
    return cypher_list
    

def write_into_file(cypher_list, file_name):
    current_directory = Path.cwd()
    file_path = current_directory / file_name
    with file_path.open("w") as text_file:
        for i in range((len(cypher_list)-1), -1, -1):
            text_file.write(f"{cypher_list[i]}\n")
    

def main():
    b_file = "oldtext.txt"
    a_file = "newtext.txt"

    cypher_list = read_file(a_file)
    write_into_file(cypher_list, b_file)

main()
