import requests


currency_cache = {}


def exchange_rates(currency):
    global currency_cache
    currency_cache[currency] = requests.get(f"http://www.floatrates.com/daily/{currency}.json").json()


def usd_eur_cache():
    currency_cache['usd'] = requests.get("http://www.floatrates.com/daily/usd.json").json()
    currency_cache['eur'] = requests.get("http://www.floatrates.com/daily/eur.json").json()


def check_cache(currency):
    if currency in currency_cache:
        return True
    return False


def in_cache():
    print("Oh! It is in the cache!")
    print_conversion()


def not_in_cache():
    print("Sorry, but it is not in the cache!")
    exchange_rates(conversion_currency)
    print_conversion()


def print_conversion():
    print(f"You received "
          f"{round(currency_cache[conversion_currency][user_currency]['inverseRate'] * money, 2)}"
          f" {conversion_currency}.")


user_currency = input().lower()
usd_eur_cache()

while True:
    conversion_currency = input().lower()
    if not conversion_currency:
        break

    money = float(input())
    print("Checking the cache...")

    if check_cache(conversion_currency):
        in_cache()
    else:
        not_in_cache()
