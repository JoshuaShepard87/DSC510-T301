
# Joshua Burden
# Assignment 9.1
# DSC510-T302 Introduction to Programming (2223-1)
# Michael Eller
# Bellevue University
# 05/15/2022

# For this week we will modify our Gettysburg processing program from week 8
# in order to generate a text file from the output rather than printing to the screen.
# Your program should have a new function called process_file which prints to the file
# (this method should almost be the same as the pretty_print function from last week.
# Keep in mind that we have print statements in main as well.
# Your program must modify the print statements from main as well.


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


def Process_file(dictionary, filename):
    # Opening the file in append mode as data was already written to it in main method
    output_file = open(filename, 'a')
    word_count = len(dictionary)
    output_file.write(f'\nLength of the dictionary: {word_count}\n')
    output_file.write('Word            Count\n')
    output_file.write('-----------------------\n')
    for key, value in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
        length = len(key)
        output_file.write('{:15s}{:3d}'.format(key, value))
        output_file.write('\n')
    output_file.close()


# define a dictionary array and then process line by line the file into the Process_line
# and then write the outcome to the file
def main():
    dictionary = {}
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        Process_line(line, dictionary)
    Pretty_print(dictionary)
    filename = input("Enter the file name: ")
    output_file = open(filename, 'w')
    output_file.close()
    Process_file(dictionary, filename)


if __name__ == '__main__':
    main()
