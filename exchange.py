import requests


def get_exchange():
    print(".....................Exchange Rate....................")
    currency_from = input("Enter currency to convert from: ").strip().lower()
    currency_to = input("Enter currency to convert to: ").strip().lower()  
    print(get_exchange_rate(currency_from, currency_to))

def get_exchange_rate(convert_from, convert_to):
    data = requests.get("https://api.coingecko.com/api/v3/exchange_rates").json()["rates"]
    price = int(data[convert_from]["value"])
    price_conversion = float(data[convert_to]["value"])/price

    return f"1 {convert_from} = {price_conversion} {convert_to}"