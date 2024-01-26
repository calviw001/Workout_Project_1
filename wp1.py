import sys


def invert_sentence(sentence):
    if len(sentence) == 1:
        return sentence
    else:
        return sentence[-1] + invert_sentence(sentence[0:-1])


def read_file(file_name):
    cypher_list = []
    with open(file_name) as text_file:
        for line in text_file:
            get_sentence = line.strip()
            cypher_list.append(invert_sentence(get_sentence))
    print(cypher_list)
    return cypher_list
    

def main():
    a_file = "oldtext.txt"
    cypher_list = read_file(a_file)

main()
