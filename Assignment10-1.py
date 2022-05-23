# Joshua Burden
# Assignment 10.1
# DSC510-T302 Introduction to Programming (2223-1)
# Michael Eller
# Bellevue University
# 05/22/2022

# Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
# The program will receive a JSON response which includes various pieces of data. You should parse the JSON data to obtain the “value” key. 
# The data associated with the value key should be displayed for the user (i.e., the joke).
# Your program should allow the user to request a Chuck Norris joke as many times as they would like. 
# You should make sure that your program does error checking at this point. 
# If you ask the user to enter “Y” and they enter y, is that ok? Does it fail? 
# If it fails, display a message for the user. There are other ways to handle this. Think about included string functions you might be able to call.
import json

import requests
from requests import HTTPError


def get_joke():
    try:
        url = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(url)
        output = json.loads(response.text)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'API down! Error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print(json.dumps(output["value"]))


def get_next():
    # TODO get next Joke
    second = str(input('Would you like to get the next joke, Yes or No? ')).lower().strip()
    # while loop to allow for a yes selection or to exit the program (and to catch input errors)
    while not (second == 'yes' or second == 'no'):
        second = str(input('You did not use Yes or No, Please either use Yes or No only\n Try again!\n'
                           'Please enter Yes or No to continue: ')).lower().strip()
    if second == 'yes':
        print('Chuck Norris approves...')
        get_joke()
        print('')
        main()
    if second == 'no':
        print('Chuck Norris knows your location and is on the way to beat you up... GLHF....')


def main():
    first = str(input('Would your like to read a chuck norris joke, Yes or No? ')).lower().strip()
    while not (first == 'yes' or first == 'no'):
        first = str(input('You did not use Yes or No, Please either use Yes or No only!\n Try again!\n'
                          'Please enter Yes or No to continue: ')).lower().strip()
    if first == 'yes':
        get_joke()
        print('')
        get_next()
    if first == 'no':
        print('Chuck Norris knows your location and is on the way to beat you up... GLHF....')


if __name__ == '__main__':
    main()
