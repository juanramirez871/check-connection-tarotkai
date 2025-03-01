import requests
import os
from dotenv import load_dotenv

load_dotenv("/src/.env")


def send_message(message):
    url = os.environ.get("URL_WHATSAPP")
    print(os.environ.get("RECEIVE_NUMBER"))
    headers = {
        "Authorization": f"Bearer {os.environ.get('TOKEN_WHATSAPP')}",
        "Content-Type": "application/json",
    }

    data = {
        "messaging_product": "whatsapp",
        "to": os.environ.get("RECEIVE_NUMBER"),
        "type": "text",
        "text": {"body": message},
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    print(response)
