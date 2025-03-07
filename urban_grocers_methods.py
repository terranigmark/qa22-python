import data
from configuration import BASE_URL, KITS
import requests


def get_all_kits():
    response = requests.get(BASE_URL + KITS + data.card_id_1)
    return response
