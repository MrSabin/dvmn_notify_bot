import logging
import time

import requests
import telegram
from environs import Env


def send_message(attempt, bot_token, chat_id):
    bot = telegram.Bot(token=bot_token)

    lesson_title = attempt["lesson_title"]
    is_negative = attempt["is_negative"]
    lesson_url = attempt["lesson_url"]

    if is_negative:
        bot_message = f"У вас проверили работу '{lesson_title}' ({lesson_url}). К сожалению, в работе нашлись ошибки."
    else:
        bot_message = f"У вас проверили работу '{lesson_title}' ({lesson_url}). Преподавателю все понравилось, можно приступать к следующему уроку!"

    bot.send_message(text=bot_message, chat_id=chat_id)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Bot started")
    env = Env()
    env.read_env()
    dvmn_token = env.str("DVMN_TOKEN")
    bot_token = env.str("TG_BOT_TOKEN")
    chat_id = env.str("TG_CHAT_ID")

    url = "https://dvmn.org/api/long_polling/"
    headers = {"Authorization": dvmn_token}
    timestamp = None

    while True:
        try:
            payload = {"timestamp": timestamp}
            response = requests.get(
                url, headers=headers, params=payload, timeout=90
            )
            response.raise_for_status()
            review_status = response.json()
            if review_status.get("status") == "found":
                for attempt in review_status.get("new_attempts"):
                    send_message(attempt, bot_token, chat_id)
            if review_status.get("timestamp_to_request"):
                timestamp = review_status.get("timestamp_to_request")
            else:
                timestamp = review_status.get("last_attempt_timestamp")
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            print("Connection lost, retry in 10 seconds...")
            time.sleep(3)


if __name__ == "__main__":
    main()
