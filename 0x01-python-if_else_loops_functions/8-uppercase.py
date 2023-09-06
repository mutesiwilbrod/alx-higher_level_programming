#!/usr/bin/python3
def uppercase(str):
    word = list(str)
    for i in range(len(word)):
        if (ord(word[i]) > 96 and ord(word[i]) < 123):
            word[i] = chr(ord(word[i]) - 32)
    print("{}".format("".join(word)))
