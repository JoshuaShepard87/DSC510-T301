# Joshua Burden
# Assignment 11.1
# DSC510-T302 Introduction to Programming (2223-1)
# Michael Eller
# Bellevue University
# 05/22/2022

# Your program must have a header.
# Your program must have a welcome message for the user.
# Your program must have one class called CashRegister.
# Your program will have an instance method called addItem which takes one parameter for price. The method should also keep track of the number of items in your cart.
# Your program should have two getter methods.
# getTotal – returns totalPrice
# getCount – returns the itemCount of the cart
# Your program must have a properly defined main function and a call to main.
# Your program must create an instance of the CashRegister class within your main function.
# Your program should have a loop in main which allows the user to continue to add items to the cart until they request to quit.
# Your program should print the total number of items in the cart.
# Your program should print the total $ amount of the cart.
# The output should be formatted as currency. Be sure to investigate the locale class. You will need to call locale.setlocale and locale.currency.
# Your program should adhere to PEP8 guidelines especially as it pertains to variable names.


# main.py
import locale


# CashRegister class
class CashRegister:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add_item(self, price):
        self.total += price
        self.count += 1

    def get_total(self):
        return self.total

    def get_count(self):
        return self.count

    def show_cart(self):
        locale.setlocale(locale.LC_ALL, 'en_US')
        total = locale.currency(self.total)
        count = self.count
        print(f'\n-------- Cart Shown ---------------------------\n'
              f'| Total number of items in cart: {count}            |\n'
              f'| Total price: {total}                        |\n'
              f'-----------------------------------------------')

    def clear_cart(self):
        #  set values back to 0
        self.total = 0
        self.count = 0
        print(f'\n--------Cart Cleared---------\n'
              f'|       Item Count: {self.count}       |\n'
              f'|       Total Price: ${self.total}     |\n'
              f'-----------------------------')

    def cash_heartbeat(self):
        print("\nWelcome to the Cash register")
        while True:
            n = input("Enter a 1 to add an item to the cart and the word quit to exit: ")
            if n == '1':
                price = float(input("Enter the price of the item: $"))
                self.add_item(price)
            elif n == 'quit':
                break
            else:
                print("Invalid entry.")
        self.show_cart()

    def try_again(self):
        n = input("\nWould you like to start a new cart? Enter a 1 to restart or quit to shutdown the program: ")
        if n == '1':
            self.clear_cart()
            self.cash_heartbeat()
        elif n == 'quit':
            print("good bye")
            exit()
        else:
            print("Invalid entry. Please try again.")
            self.try_again()


# main method
def main():
    cart = CashRegister()
    cart.cash_heartbeat()
    cart.try_again()


if __name__ == '__main__':
    main()
