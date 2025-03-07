import re
import os
import json


def validate_url(url):
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// o https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"  # IP (v4)
        r"\[?[A-F0-9]*:[A-F0-9:]+\]?)"  # IP (v6)
        r"(?::\d+)?"  # port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )

    return re.match(regex, url) is not None


def update_count_mistakes(file_path, key, new_value, key2, new_value2):
    if os.path.exists(file_path):
        with open(file_path, "r+") as json_file:
            data = json.load(json_file)

            old_value = get_value_from_json(file_path, key)
            data[key] = (old_value + new_value) * new_value

            old_value2 = get_value_from_json(file_path, key2)
            data[key2] = (old_value2 + new_value2) * new_value2

            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            json_file.truncate()
    else:
        data = {key: new_value}
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        update_count_mistakes(file_path, key, new_value, key2, new_value2)


def get_value_from_json(file_path, key):
    if os.path.exists(file_path):
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            return data.get(key, f"'{key}' no exist in the JSON")
    else:
        return f"The File {file_path} no exist"


{"count_mistakes": 0}
