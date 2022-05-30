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

import requests
import json


apikey = '&appid=f7fc4159b1cadbe65b4aae2ae711030f'
country_code = 'US'


def K_to_F_conversion(temperature):
    converted = (temperature - 273.15) * 9 / 5 + 32
    return int(converted)


def connect_to_api(location):
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?{location}{apikey}'
        print(url)
        request = requests.get(url)
        response = request.json()
        print(json.dumps(response, indent=4, sort_keys=True))
    except requests.ConnectionError as err1:
        print(f'Connection Error: {err1}')
    except requests.HTTPError as err2:
        print(f'HTTP Error: {err2}')
    except requests.Timeout as err3:
        print(f'Timeout error: {err3}')
    except requests.RequestException as err4:
        print(f'Request Exception: {err4}')


def by_city(city):
    pass


def get_weather(location):
    if location.isdigit() is True:
        print("query zip: ", location)
        query = location
        connect_to_api(f'zip={query}')
    else:
        print("query q: ", location)
        city_state = location
        # query = f''
        connect_to_api(f'q={city_state}')
    # choice = input("Do you want to search for a city or a zip code?")
    # if choice == 'zipcode':
    #     zipcode = int(input("What zipe code are you wanting to search? :"))
    # if choice == 'city':
    #     city_name = input("what city do you want to search for ?:")


def main():
    location = input("where do you want to look up: ")

    get_weather(location)
    # zipcode = 'zip=68130'
    # connect_to_api(zipcode)


if __name__ == '__main__':
    main()