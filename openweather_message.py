import logging
import emoji


class MessageFormatter():

    @classmethod
    def create_message(cls, full_data, location):
        message_base = "Good morning! The weather today in {}:\n\n".format(
            location)
        time_span = ""
        for block in full_data["list"][:6]:
            time_span += "At {} the temperature will be {}°C with {} {} \n".format(
                cls.__get_time_of_forecast(block), cls.__get_temperature(block),
                 cls.__get_text_weather(block), cls.__emoji_by_id(block))
        logging.info('Message is formed')
        return message_base + time_span

    @classmethod
    def __get_temperature(cls, block):
        return int(block["main"]["temp"])

    @classmethod
    def __get_text_weather(cls, block):
        return block["weather"][0]["description"]

    @classmethod
    def __get_time_of_forecast(cls, block):
        return block["dt_txt"].split(" ")[1][:-3]

    @classmethod
    def __emoji_by_id(cls, block):
        icon_id = block["weather"][0]["id"]
        icon_id_first = str(block["weather"][0]["id"])[0]
        if icon_id_first == "2":
            return cls.__get_emoji(":zap:")
        elif icon_id_first == "3":
            return cls.__get_emoji(":sweat_drops:")
        elif icon_id_first == "5":
            return cls.__get_emoji(":umbrella:")
        elif icon_id_first == "6":
            return cls.__get_emoji(":snowflake:")
        elif icon_id_first == "7":
            return cls.__get_emoji(":foggy:")
        elif icon_id_first == "8":
            if icon_id == 800:
                return cls.__get_emoji(":sunny:")
            else:
                return cls.__get_emoji(":cloud:")
        else:
            return ""

    @classmethod
    def __get_emoji(cls, text_emj):
        return emoji.emojize(text_emj, use_aliases=True)
