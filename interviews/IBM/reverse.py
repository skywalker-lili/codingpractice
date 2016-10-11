# Reverse words
import sys

def reverse_word(string):
    return "".join([string[i].lower() for i in range(len(string)-1, -1, -1)])

for line in sys.stdin:
    splited = line.split()
    for i in range(len(splited)):
        splited[i] = reverse_word(splited[i])
    splited = splited[::-1] # reverse the list of words
    first_word = splited[0]
    first_word = first_word[0].upper() + first_word[1:]
    splited[0] = first_word
    print(" ".join(splited))