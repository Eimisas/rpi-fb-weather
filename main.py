from weather_data import OpenWeather
from facebook_user import FB
import random
import sys
from project_configuration import Config
from logger import Log

def print_mock_message(mock_message):
    print(mock_message)

def main():
    config = Config()
    flag_arguments = config.setup_and_parse_flags()
    logger = Log('logs/logs.log')
    logger.log_start_end('started')
    try:
        config = config.load_config()
        fb_bot = FB(config)
        fb_bot.login_client()
        open_weather = OpenWeather(config["url"], config["defaultCity"], config["appKey"])
        weather_data = open_weather.parse_and_form_message()
        fb_bot.send_messages(
            weather_data) if flag_arguments.environment == 'prod' else print_mock_message(weather_data)
        fb_bot.logout()
    except:
        error = sys.exc_info()
        logger.log_error(error)
        fb_bot.logout()
        logger.log_start_end('finished')
main()
