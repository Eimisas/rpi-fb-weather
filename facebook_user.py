from fbchat import Client
from fbchat.models import *
import time
import random
import logging

class FB():

    def __init__(self, config):
        self.config = config

    def send_messages(self, message):
        all_user_conversations = self.__get_all_conversations()
        logging.info("Got all conversations")
        users_uid_to_send = self.__get_uid_from_conversations(
            all_user_conversations)
        logging.info("Got selected UID to send messages to")
        self.__send_message_to_users(users_uid_to_send, message)

    def login_client(self):
        self.client = Client(
            self.config["fbUsername"], self.config["password"])
        logging.info("Client successfully logged in!")

    def __get_all_conversations(self):
        return self.client.fetchAllUsers()

    def __get_uid_from_conversations(self, all_conversations):
        users_to_send = self.__get_users_to_send()
        out = []
        for user in all_conversations:
            if(user.name in users_to_send):
                out.append(user.uid)
        return out

    def __get_users_to_send(self):
        return self.config["usersToSend"]

    def set_users_to_send(self, users):
        self.config["usersToSend"] = users

    def __send_message_to_users(self, users_uid_to_send, message):
        for uid in users_uid_to_send:
            self.client.send(Message(text=message), thread_id=uid,
                        thread_type=ThreadType.USER)
        logging.info("All messages successfully sent")
    
    def logout(self):
        self.__delay()
        logging.info("Client logged out") if self.client.logout(
        ) else logging.debug("Something went wrong when logging client out!")

    ##Delay is used in order to simulate real user actions
    def __delay(self):
        random_time_span = random.randint(30, 145)
        logging.info("Delay started {}".format(random_time_span))
        time.sleep(random_time_span)
    
    
