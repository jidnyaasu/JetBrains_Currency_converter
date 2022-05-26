import requests

currency_cache = {}


def exchange_rates(currency):
    try:
        return requests.get(f"http://www.floatrates.com/daily/{currency}.json").json()
    except requests.JSONDecodeError:
        return False


def print_conversion():
    print(f"You will receive "
          f"{round(currency_cache[user_currency][conversion_currency]['rate'] * money, 2)}"
          f" {conversion_currency} for {money} {user_currency}.\n")


while True:
    user_currency = input("Enter the currency you have: ").lower()
    currency_cache[user_currency] = exchange_rates(user_currency)
    if currency_cache[user_currency]:
        money = float(input("Enter the amount you have: "))
        break
    else:
        print("Enter valid currency code")

while True:
    conversion_currency = input("Enter the currency you want to convert to: ").lower()
    if not conversion_currency:
        break

    try:
        if currency_cache[user_currency][conversion_currency]:
            print_conversion()
    except KeyError:
        print("Enter valid currency code")
