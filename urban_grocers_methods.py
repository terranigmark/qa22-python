import data
from configuration import *
import requests


def get_all_kits(card_id: str):
    response = requests.get(BASE_URL + KITS + CARD_ID_PARAM + card_id)
    return response
