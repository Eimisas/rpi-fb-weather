import logging
import datetime

class Log():

    def __init__(self, log_path, log_level=logging.DEBUG):
        logging.basicConfig(filename=log_path, level=log_level)

    def __current_time(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


    def log_start_end(self, status):
        logging.info(
            "{} : ------ Application {} ------".format(self.__current_time(), status))

    def log_error(self, error):
        logging.error(error)