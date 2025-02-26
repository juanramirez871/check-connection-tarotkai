import requests
import os


def send_message(message):
    url = os.environ.get("URL_WHATSAPP")
    headers = {
        "Authorization": f"Bearer {os.environ.get('TOKEN_WHATSAPP')}",
        "Content-Type": "application/json",
    }

    data = {
        "messaging_product": "whatsapp",
        "to": os.environ.get("RECEIVE_NUMBER"),
        "type": "template",
        "text": {"body": message},
    }
    requests.post(url, headers=headers, json=data)
