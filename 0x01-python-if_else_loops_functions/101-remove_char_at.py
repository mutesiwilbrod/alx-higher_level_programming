#!/usr/bin/python3

def remove_char_at(str, n):
    """ function that create a copy of a str """
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
