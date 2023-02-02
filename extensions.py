import requests
import json
from config import keys


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты "{quote}".')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Валюты "{base}" нет в "допустимых" или в названии валюты "{base}" опечатка.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Валюты "{quote}" нет в "допустимых" или в названии валюты "{quote}" опечатка.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество "{amount}".')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = amount * json.loads(r.content)[keys[quote]]

        return total_base