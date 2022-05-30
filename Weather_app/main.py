from get_weather import *
import requests
import json
from tryagain import *
from display_f import *
from display_c import *
from get_weather import *
from config import *
from convert import *
from config import *


def main():
    print("Welcome to the weather app\n"
          "Powered by openweatherAPI\n")
    location = input("Please enter the Zip Code or City Name here:  ")
    get_weather(location)


if __name__ == '__main__':
    main()
