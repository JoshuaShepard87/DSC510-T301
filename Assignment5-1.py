
# Joshua Burden
# Assignment 5.1
# DSC510-T302 Introduction to Programming (2223-1)
# Michael Eller
# Bellevue University
# 04/17/2022


# Your program must have a header. 
# Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
# This program will perform various calculations (addition, subtraction, multiplication, division, and average calculation)
# This program will contain a variety of loops and functions.
# The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
# Define a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
# This function will perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
# This function will print the calculated value for the end user.
# Define a function named calculateAverage which takes no parameters.
# This function will ask the user how many numbers they wish to input.
# This function will use the number of times to run the program within a for loop in order to calculate the total and average.
# This function will print the calculated average.
# This program will have a main method which contains a while loop. The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
# The main method should prompt the user for the operation they wish to perform.
# The main method should evaluate the entered data using if statements.
# The main method should call the necessary function to perform the calculation.


def performCalculation(symbol):
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    result = 0
    if symbol == '+':
        result = num1+num2
    elif symbol == '-':
        result = num1 - num2
    elif symbol == '*':
        result = num1 * num2
    elif symbol == '/':
        result = num1 / num2
    print(f"result = {result}")


def calculateAverage():
    n = int(input("How many numbers do you want to compare to find the Average? \n"))
    total = 0
    for i in range(n):
        x = float(input("Please enter number: \n"))
        total += x
    average = round((total / n), 2)
    print(f"The average of the {n} numbers is: {average}")


def main():
    choice = input("What operation are you wanting to perform or type end to quit? (+, -, *, /, average) \n")
    while choice != "stop":  # While loop to have the program keep asking for inputs.
        if choice == "+":
            performCalculation("+")
        if choice == "-":
            performCalculation("-")
        if choice == "*":
            performCalculation("*")
        if choice == "/":
            performCalculation("/")
        if choice == "average":
            calculateAverage()
        else:
            choice = "stop"  # Else statement to end the program should that be entered into console.
        choice = input("What operation are you wanting to perform? type stop to quit. (+, -, *, /, average) \n")


if __name__ == '__main__':
    main()