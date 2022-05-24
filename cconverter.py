import requests

currency_cache = {}


def exchange_rates(currency):
    global currency_cache
    currency_cache[currency] = requests.get(f"http://www.floatrates.com/daily/{currency}.json").json()


def check_cache(currency):
    if currency in currency_cache:
        return True
    return False


def in_cache():
    print_conversion()


def not_in_cache():
    exchange_rates(conversion_currency)
    print_conversion()


def print_conversion():
    print(f"You will receive "
          f"{round(currency_cache[conversion_currency][user_currency]['inverseRate'] * money, 2)}"
          f" {conversion_currency} for {money} {user_currency}.\n")


user_currency = input("Enter the currency you have: ").lower()
money = float(input("Enter the amount you have: "))

while True:
    conversion_currency = input("Enter the currency you want to convert to: ").lower()
    if not conversion_currency:
        break

    if check_cache(conversion_currency):
        in_cache()
    else:
        not_in_cache()
