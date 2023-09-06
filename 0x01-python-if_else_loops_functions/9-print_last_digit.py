#!/usr/bin/python3
def print_last_digit(number):
    word = int(repr(number)[-1])
    print("{}".format(word), end="")
    return word
