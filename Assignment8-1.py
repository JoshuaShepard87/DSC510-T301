# Joshua Burden
# Assignment 8.1
# DSC510-T302 Introduction to Programming (2223-1)
# Michael Eller
# Bellevue University
# 04/30/2022
from operator import itemgetter


# goes through and adds a count to those words in the dictionary taht are + 1 else, it leaves it as is
def add_wrd(wrd, dictionary):
    if wrd in dictionary.keys():
        dictionary[wrd] = dictionary[wrd] + 1
    else:
        dictionary[wrd] = 1


# Process the dictionary by line splits and then
def Process_line(line, dictionary):
    for wrd in line.split():
        add_wrd(wrd, dictionary)


# Pretty print the text
def Pretty_print(dictionary):
    print('\nLength of the dictionary:', len(dictionary))
    print('Word            Count')
    print('-----------------------')
    for key, value in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
        length = len(key)
        print('{:15s}{:3d}'.format(key, value))


# define a dictionary array and then process line by line the file into the Process_line
# and then pretty print the outcome
def main():
    dictionary = {}
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        Process_line(line, dictionary)
    Pretty_print(dictionary)


if __name__ == '__main__':
    main()
