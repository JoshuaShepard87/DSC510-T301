
# Joshua Burden
# Assignment 4.1
# DSC510-T302 Introduction to Programming (2223-1)
# Michael Eller
# Bellevue University
# 04/10/2022


# This week we will modify our IF Statement program to add a function to do the heavy lifting.
# Modify your IF Statement program to add a function. This function will perform the cost calculation. 
# The function will have two parameters (feet and price). When you call the function, you will pass two arguments to the function; 
# feet of fiber to be installed and the cost (remember that price is dependent on the number of feet being installed). 
# You should have the following:
# Your program must have a header. 
# Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
# A welcome message.
# A function with two parameters.
# A call to the function.
# The application should calculate the cost based upon the number of feet being ordered.
# A printed message displaying the company name and the total calculated cost.
# All costs should display in USD Currency Format Ex: $123.45.
# Your program must have a properly defined main method and a properly defined call to main.

def main():
    user = input('what is your name?')
    print(f'Welcome, {user}!')
    company = input('Where you work?')
    
    # To make certain a number is entered for calculation, a try/except block is utilized
    while True:
        try:
            feet = int(input('How much feet do you need of that cable, yo?'))
            break
        except ValueError:
            print('You did not enter a number.')

    def bulk_rate():
        # Return the installation cost rate depending on the number of feet of cable needed
        if feet > 500:
            install_cost = .50
        elif feet > 250:
            install_cost = .70
        elif feet > 100:
            install_cost = .80
        else:
            install_cost = .87  # standard installation rate, no discount applied
        return float(install_cost)

    def total_cost(feet, price):
        # Return the calculated total cost of the cable installation
        return print('Total Cost: $', format((feet * price), '.2f'))

    # Print receipt for the user including company name, number of feet of fiber installed, calc_cost, total_cost
    print(f"Company Name: {company}")
    print(f"Fiber Optic cable: {feet} feet")
    print('Your cost per foot: $', format(bulk_rate(), '.2f'))
    total_cost(feet, bulk_rate())


if __name__ == '__main__':
    main()
    
    
