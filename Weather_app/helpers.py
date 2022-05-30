import requests
import json


# convert Kelvin to Celsius
def K_to_C_conversion(temperature):
    converted_c = temperature - 273.15
    return int(converted_c)


# convert Kelvin to Fahrenheit
def K_to_F_conversion(temperature):
    converted_f = (temperature - 273.15) * 9 / 5 + 32
    return int(converted_f)


# wind comes back in meters
# convert to MPH
def miles_per_hour(wind):
    wind_in_mph = wind * 2.236936
    return int(wind_in_mph)


# converts meteorological wind direction
def wind_direction(wind_deg):
    val = int((wind_deg / 22.5) + .5)
    arr = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return arr[(val % 16)]
