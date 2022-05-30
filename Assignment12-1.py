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

apikey = '&appid=f7fc4159b1cadbe65b4aae2ae711030f'
country_code = 'US'


def K_to_F_conversion(temperature):
    converted = (temperature - 273.15) * 9 / 5 + 32
    return int(converted)


def miles_per_hour(wind):
    wind_in_mph = wind * 2.236936
    return int(wind_in_mph)


def wind_direction(wind_deg):
    val = int((wind_deg / 22.5) + .5)
    arr = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return arr[(val % 16)]


def display(converted_data):
    return print(f'Results Found for {converted_data["name"]}:\n'
                 f'Current Temp: {K_to_F_conversion(converted_data["temp"])}\N{DEGREE SIGN}F\n'
                 f'Current Humidity: {converted_data["humidity"]}%\n'
                 f'Cloud cover:  {converted_data["clouds"]}%\n'
                 f'Weather condition: {converted_data["weather_condition"]}\n'
                 f'Feels like: {K_to_F_conversion(converted_data["feels_like"])}\N{DEGREE SIGN}F\n'
                 f'High Temperature for the Day: {K_to_F_conversion(converted_data["temp_max"])}\N{DEGREE SIGN}F\n'
                 f'Low Temperature for the day: {K_to_F_conversion(converted_data["temp_min"])}\N{DEGREE SIGN}F\n'
                 f'Current wind speed is: {miles_per_hour(converted_data["wind_speed"])} MPH\n'
                 # f'Wind gusts: {miles_per_hour(converted_data["wind_gust"])} MPH\n'
                 f'Wind Direction: {wind_direction(converted_data["wind_direction"])}\n\n'),


def convert(response):
    data = json.dumps(response, indent=4, sort_keys=True)
    # print(data)
    converted_data = {
        "feels_like": response['main']['feels_like'],
        "name": response['name'],
        "humidity": response['main']['humidity'],
        "temp": response['main']['temp'],
        "clouds": response['clouds']['all'],
        "weather_condition": response['weather'][0]['description'],
        "temp_min": response['main']['temp_min'],
        "temp_max": response['main']['temp_max'],
        "wind_speed": response['wind']['speed'],
        # "wind_gust": response['wind']['gust'],
        "wind_direction": response['wind']['deg']
    }
    return converted_data


def connect_to_api(location):
    try:
        print("connecting...")
        url = f'https://api.openweathermap.org/data/2.5/weather?{location}{apikey}'
        request = requests.get(url)
        # if request.status_code
        status = request.status_code
        if status == 200:
            print("successful connection. \nFetching response: \n")
            response = request.json()
            display(convert(response))
            repeat()
        if status == 404:
            print("seems we could not find anything for that city, state or zip\n"
                  "Let us try again with a new city, state or zip code: ")
            try_again()
    except requests.ConnectionError as err1:
        print(f'Connection Error: {err1}')
    except requests.HTTPError as err2:
        print(f'HTTP Error: {err2}')
    except requests.Timeout as err3:
        print(f'Timeout error: {err3}')
    except requests.RequestException as err4:
        print(f'Request Exception: {err4}')


def repeat():
    choice = input("would you like to do another search?\n"
                   "enter yes for yes or no to quit:")
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
    location = input("where do you want to look up: ")
    get_weather(location)


def get_weather(location):
    if location.isdigit() is True:
        query = location
        connect_to_api(f'zip={query}')
    else:
        print("query q: ", location)

        # query = f''
        connect_to_api(f'q={location}')
    # choice = input("Do you want to search for a city or a zip code?")
    # if choice == 'zipcode':
    #     zipcode = int(input("What zipe code are you wanting to search? :"))
    # if choice == 'city':
    #     city_name = input("what city do you want to search for ?:")


def main():
    print("Welcome to the weather app\n"
          "Powered by openweatherAPI\n")
    # city = input()
    # state = input()
    # country = input()
    location = input("Please enter the Zip Code or City, Country:  ")
    get_weather(location)


if __name__ == '__main__':
    main()
