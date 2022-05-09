# Joshua Burden
# Assignment 8.1
# DSC510-T302 Introduction to Programming (2223-1)
# Michael Eller
# Bellevue University
# 04/30/2022
from operator import itemgetter


def add_wrd(wrd, dictionary):
    if wrd in dictionary.keys():
        dictionary[wrd] = dictionary[wrd] + 1
    else:
        dictionary[wrd] = 1


def Process_line(line, dictionary):
    for wrd in line.split():
        add_wrd(wrd, dictionary)


def Pretty_print(dictionary):
    print('\nLength of the dictionary:', len(dictionary))
    print('Word            Count')
    print('-----------------------')
    for key, value in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
        length = len(key)
        print('{:15s}{:3d}'.format(key, value))


def main():
    dictionary = {}
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        Process_line(line, dictionary)
    Pretty_print(dictionary)


if __name__ == '__main__':
    main()
