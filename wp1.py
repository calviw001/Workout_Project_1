import sys


def invert_sentence(sentence):
    if len(sentence) == 1:
        return sentence
    else:
        return sentence[-1] + invert_sentence(sentence[0:-1])

def read_file(file_name):
    pass
    

def main():
    a_file = "oldtext.txt"
    read_file(a_file)

main()
