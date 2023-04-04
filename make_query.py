import requests
from print_data import trending_data_print, print_query_data

def get_top_7():
    print(".....................Trending Seven.......................")
    top_7 = requests.get("https://api.coingecko.com/api/v3/search/trending")
    trending_data_print(top_7.json())


def search_crypto():
    print("..........Search for a certain Crypto Currency..........")
    query = input("Enter the coin you are looking for: ").strip()
    query_data = requests.get(f"https://api.coingecko.com/api/v3/search?{query}")
    print_query_data(query_data.json())


def get_curr_list():

    print("..........Here is the list of currency. You might need it to make currency exchange..........")
    query = requests.get("https://api.coingecko.com/api/v3/simple/supported_vs_currencies").json()

    for curr in query:
        print(curr,end='\t')

    print()