import requests
import os
from dotenv import load_dotenv

load_dotenv("/src/.env")


def send_message(message):
    try:
        i = 1
        url = os.environ.get("URL_WHATSAPP")

        while True:
            number = os.environ.get(f"RECEIVE_NUMBER_{i}")

            if not number:
                break

            params = {"number": number, "message": message}
            requests.get(url, params=params)
            i += 1

    except Exception as e:
        print("error whatsapp: ", e)
