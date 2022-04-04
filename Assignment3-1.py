# Joshua Burden
# DSC510-T301 Introduction to Programming (2225-1)
# Michael Eller
# Bellevue University
# 04/03/2022

# This week we will implement “if statements” in a program. 
# Your program will calculate the cost of fiber optic cable installation by multiplying the number of feet needed by $0.87. 
# We will also evaluate a bulk discount. 
# You will prompt the user for the number of fiber optic cable they need installed. 
# Using the default value of $0.87 calculate the total expense. 
# If the user purchases more than 100 feet they are charged $0.80 per foot. 
# If the user purchases more than 250 feet they will be charged $0.70 per foot. 
# If they purchase more than 500 feet, they will be charged $0.50 per foot.
# Your program must have a header. See below for an example of what must be included with each assignment. 
# Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
# Display a welcome message for your program.
# Get the company name from the user.
# Get the number of feet of fiber optic cable to be installed from the user.
# Evaluate the total cost based upon the number of feet requested.
# Display the calculated information including the number of feet requested and company name.


def main():
    default_rate = float(.87)
    disc_rate_100 = 100
    disc_rate_100_cost = float(.80)
    disc_rate_250 = 250
    disc_rate_250_cost = float(.70)
    disc_rate_500 = 500
    disc_rate_500_cost = float(.50)

    # print("Hello World")
    # display welcome message
    print("Hello and welcome!")

    # Retrieve Company name input
    company_name = input("What is your company's Name?")

    # Calculate the install cost of fiber optic cable by total_cost(in feet) * $0.87
    feet = int(input("How many feet of fiber optic do you need for your project?"))

    if feet >= disc_rate_500:
        default_rate = disc_rate_500_cost
    elif feet >= disc_rate_250:
        default_rate = disc_rate_250_cost
    elif feet >= disc_rate_100:
        default_rate = disc_rate_100_cost
    elif feet < 100:
        return default_rate 

    # Print receipt for the user including company name, number of feet of fiber installed, calc_cost, total_cost
    total_cost = '${:,.2f}'.format(feet * default_rate)
    print(f"Company Name: {company_name}")
    print(f"Fiber Optic cable: {feet} feet")
    print("Your discount: " + "${:,.2f}".format(default_rate))
    print(f"Total Cost: {total_cost}")


if __name__ == '__main__':
    main()