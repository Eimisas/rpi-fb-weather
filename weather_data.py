import requests
import datetime as dt
import logging
import emoji
from openweather_message import MessageFormatter

class OpenWeather():

    def __init__(self, url, location, api_key):
        self.url = url
        self.location = location
        self.api_key = api_key

    def parse_and_form_message(self):
        full_data = self.__get_weather_data_from_api()
        message = self.__form_message_from_data(full_data)
        return message

    def __get_weather_data_from_api(self):
        url = "{}q={}&units=metric&appid={}".format(
            self.url, self.location, self.api_key)
        r = requests.get(url)
        logging.info('Got weather information from API')
        return r.json()

    ##Message creation is handled by MessageFormatter
    def __form_message_from_data(self, full_data):
        return MessageFormatter.create_message(full_data, self.location)
    
