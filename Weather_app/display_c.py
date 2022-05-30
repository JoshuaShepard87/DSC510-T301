from Weather_app.helpers import *


def display_c(converted_data):
    return print(f'Results Found for {converted_data["name"]}:\n'
                 f'Current Temperature: {K_to_C_conversion(converted_data["temp"])}\N{DEGREE SIGN}C\n'
                 f'Current Temperature in Kelvin: {int(converted_data["temp"])}\N{DEGREE SIGN}K\n'
                 f'Current Humidity: {converted_data["humidity"]}%\n'
                 f'Cloud cover:  {converted_data["clouds"]}%\n'
                 f'Weather condition: {converted_data["weather_condition"]}\n'
                 f'Feels like: {K_to_C_conversion(converted_data["feels_like"])}\N{DEGREE SIGN}F\n'
                 f'High Temperature for the Day: {K_to_C_conversion(converted_data["temp_max"])}\N{DEGREE SIGN}C\n'
                 f'Low Temperature for the day: {K_to_C_conversion(converted_data["temp_min"])}\N{DEGREE SIGN}C\n'
                 f'Current wind speed is: {miles_per_hour(converted_data["wind_speed"])} MPH\n'
                 # removed because some country responses do not have wind gust information returned
                 # f'Wind gusts: {miles_per_hour(converted_data["wind_gust"])} MPH\n' 
                 f'Wind Direction: {wind_direction(converted_data["wind_direction"])}\n\n'),

