import re


def validate_url(url):
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// o https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"  # IP (v4)
        r"\[?[A-F0-9]*:[A-F0-9:]+\]?)"  # IP (v6)
        r"(?::\d+)?"  # puerto
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )

    return re.match(regex, url) is not None
