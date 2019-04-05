"""
File used for storing commonly used functions.
"""

from hashlib import sha1
from base64 import urlsafe_b64encode

from .models import URL


def generate_url_shortcut(text):
    """
    Function returning hashed used, provided as an argument.
    To ensure avoiding collisions, there is a prefix (<id_to_be>_) added
    to every hash.
    :param text: provided URL.
    :return: hashed URL with prefix.
    """
    hasher = sha1(text.encode())
    next_id = len(URL.objects.all()) + 1
    url_hash = str(next_id) + '_' + urlsafe_b64encode(
        hasher.digest())[:10].decode()
    return url_hash
