# Joshua Burden
# Assignment 12.1
# DSC510-T302 Introduction to Programming (2223-1)
# Michael Eller
# Bellevue University
# 05/22/2022

# Create a header for your program just as you have in the past.
# Create a Python Application which asks the user for their zip code or city (Your program must perform both a city and a zip lookup).
# You must ask the user which they want to perform with each iteration of the program.
# Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
# Display the weather forecast in a readable format to the user. Do not display the weather data in Kelvin, since this is not readable to the average person.
# You should allow the user to choose between Celsius and Fahrenheit and ideally also Kelvin.
# Use comments within the application where appropriate in order to document what the program is doing. Comments should add value to the program and describe important elements of the program.
# Use functions including a main function and a properly defined call to main. You should have multiple functions.
# Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
# Validate whether the user entered valid data.
# If valid data isn’t presented notify the user.
# Your program should never crash with bad user input.
# Use the Requests library in order to request data from the webservice.
# Use Try blocks to ensure that your request was successful. If the connection was not successful display a message to the user.
# Use Python 3
# Use try blocks when establishing connections to the webservice.
# You must print a message to the user indicating whether or not the connection was successful.
# You must have proper coding convention including proper variable names (See PEP8).
from collections import namedtuple

import requests
import json
from Weather_app.config import apikey
from Weather_app.display_c import *
from Weather_app.display_f import *
from Weather_app.helpers import *
from Weather_app.converter import *


# connects to the api and returns the results

def connect_to_api(location):
    try:
        print("connecting...")
        url = f'https://api.openweathermap.org/data/2.5/weather?{location}{apikey}'
        request = requests.get(url)
        # if request.status_code
        status = request.status_code
        if status == 200:
            print(f'successful connection with status code: {status}')
            choice = input('Do you want your measurements in F or C?\n'
                           'Enter F for Fahrenheit or C for Celsius: ')
            if choice == 'F':
                print(f'Fetching response: \n')
                response = request.json()
                display_f(convert(response))
                repeat()
            elif choice == 'C':
                print(f'successful connection with status code: {status} \n\nFetching response: \n')
                response = request.json()
                display_c(convert(response))
                repeat()
            else:
                print("You must pick either C for Celsius or F for Fahrenheit\n")
                try_again()
        if status == 404:
            print(f'seems we could not find anything for that city, state or zip as we got back status code: '
                  f'{status} from OpenWeather API\n'
                  f'You might need to append the country code to your search if you are using city/state\n'
                  f'such as looking up Dallas, TX you will have to also add the country code: Dallas, TX, US\n'
                  f'Or... just enter the city name\n'
                  f'If you are searching abroad you can add the city and the country such as: London, UK\n\n'
                  f'Let us try again with a new city, state or zip code: ')
            try_again()
    except requests.ConnectionError as err1:
        print(f'Connection Error: {err1}')
        try_again()
    except requests.HTTPError as err2:
        print(f'HTTP Error: {err2}')
        try_again()
    except requests.Timeout as err3:
        print(f'Timeout error: {err3}')
        try_again()
    except requests.RequestException as err4:
        print(f'Request Exception: {err4}')
        try_again()


# just repeats the process
def repeat():
    choice = input("would you like to do another search?\n"
                   "Enter yes for yes or no to quit: ")
    if choice == 'yes':
        try_again()
    elif choice == 'no':
        print("Good bye")
        exit(0)
    else:
        print("seems something went wrong. \n"
              "Trying again...\n")
        repeat()


def try_again():
    location = input("\nPlease enter the Zip Code or City Name here:  ")
    get_weather(location)


def get_weather(location):
    if location.isdigit() is True:
        query = location
        connect_to_api(f'zip={query}')
    else:
        connect_to_api(f'q={location}')


def main():
    print("Welcome to the weather app\n"
          "Powered by openweatherAPI\n")
    location = input("Please enter the Zip Code or City Name here:  ")
    get_weather(location)


if __name__ == '__main__':
    main()
