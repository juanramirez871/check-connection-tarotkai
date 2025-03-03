import requests
import os
from dotenv import load_dotenv

load_dotenv("/src/.env")


def send_message(message):
    try:
        url = os.environ.get("URL_WHATSAPP")
        number = os.environ.get("RECEIVE_NUMBER")
        params = {"number": number, "message": message}

        requests.get(url, params=params)

    except Exception as e:
        print("error whatsapp: ", e)
