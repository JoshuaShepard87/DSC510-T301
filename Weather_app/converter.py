import json


# converts the response back to a new array where the key can be called for display easier
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

