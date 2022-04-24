# Joshua Burden
# Assignment 6.1
# DSC510-T302 Introduction to Programming (2223-1)
# Michael Eller
# Bellevue University
# 04/24/2022

# This week we will create a program which works with lists. Your goal is to create a program which contains a list of temperatures.
# Your program will populate the list based upon user input. Your program will determine the number of temperatures in the program, 
# determine the largest temperature, and the smallest temperature.
from functools import reduce


# uses lambda function to return the average of all the temps
# use reduce to reduce the list values into a single value and then divide by the length of the list
def Average(temperature):
    return reduce(lambda a, b: a + b, temperature) / len(temperature)


# added this because why not
# takes the temp and converts to celcius
def f_to_c(temp):
    return (temp - 32) * 5 / 9


def main():
    # empty list
    temperature = list()
    # while loop with exit flag
    while 1:
        print("\nIf you want to leave, enter -1000.")
        temp = int(input("enter the temperature in F: "))
        # exit flag conditionally set to -1000
        if temp == -1000:
            print('Good bye')
            break
        else:
            # append new input to list
            temperature.append(temp)
            # empty array
            largest = temperature[0]
            # empy array
            smallest = temperature[0]
            # for traversing list of temp
            for x in temperature:
                # finds the largest entered into the list
                if x > largest:
                    largest = x
                    # find the smallest in list
                    if x < smallest:
                        smallest = x
            # calls the Average method and passes list to it
            average = Average(temperature)
            # callse the f_to_C method and passes temp to it
            celcius = f_to_c(temp)
        # Self-explanatory
        print("\nthe largest is: ", largest, " degrees Fahrenheit")
        print("\nThe smallest is: ", smallest, " degrees Fahrenheit")
        print("\nNumber of temps entered: ", len(temperature), " degrees Fahrenheit")
        print("\n Average Temperature entered: ", round(average, 2), " degrees Fahrenheit")
        print(f"the temperature {temp} degrees Fahrenheit is {celcius} degrees celsius")


if __name__ == '__main__':
    main()
