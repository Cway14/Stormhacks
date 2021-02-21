# Python program to find current
# weather details of texas
# using openweathermap api

# import required modules
import requests
import json


class Weather:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self):
        # Enter your API key here
        api_key = "a7b37fc8fa9faed677e7e0bd192282ed"

        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # Give city name
        city_name = "texas"

        # complete_url variable to store
        # complete url address
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        # get method of requests module
        # return response object
        response = requests.get(complete_url)

        # json method of response object
        # convert json format data into
        # python format data
        data = response.json()
        weather = data["weather"][0]["description"]
        if data["weather"][0]["main"].lower() != "clear":
            return f"It is {weather} right now! Be careful!"
        else:
            return f"It is {weather} right now! Be free!"


app = Weather("a7b37fc8fa9faed677e7e0bd192282ed")
