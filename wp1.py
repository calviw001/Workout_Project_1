import sys
from pathlib import Path

def get_user_inputs():
    try:
        assert len(sys.argv) == 3
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        return input_file, output_file
    except AssertionError:
        print("Usage: python wp1.py input_file_name output_file_name")
        sys.exit()


def invert_sentence(sentence):
    if len(sentence) == 1:
        return sentence
    else:
        return sentence[-1] + invert_sentence(sentence[0:-1])


def read_file(file_name):
    current_directory = Path.cwd()
    cypher_list = []
    try:
        file_path = current_directory / file_name
        # print(current_directory)
        cypher_list = []
        with file_path.open("r") as text_file:
            for line in text_file:
                get_sentence = line.strip()
                cypher_list.append(invert_sentence(get_sentence))
        # print(cypher_list)
        return cypher_list
    except FileNotFoundError:
        print("Your input file does not exist!!")
        sys.exit()
    

def write_into_file(cypher_list, file_name):
    current_directory = Path.cwd()
    file_path = current_directory / file_name
    with file_path.open("w") as text_file:
        for i in range((len(cypher_list)-1), -1, -1):
            text_file.write(f"{cypher_list[i]}\n")
    

def main():
    # input_file = "oldtext.txt"
    # output_file = "newtext.txt"
    input_file, output_file = get_user_inputs()
    cypher_list = read_file(input_file)
    write_into_file(cypher_list, output_file)

main()
