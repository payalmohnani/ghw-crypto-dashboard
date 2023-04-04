

def trending_data_print(trending_response):
    data = trending_response["coins"]
    for each_item in data:
        print(
            f"""
                Score : {each_item["item"]["score"]}
                Name : {each_item["item"]["name"]}
                Symbol : {each_item["item"]["symbol"]}
                Market_cap_rank : {each_item["item"]["market_cap_rank"]}
                Value : {each_item["item"]["price_btc"]} btc
            """
        )


def print_query_data(query_response):
    data = query_response["coins"]
    i = 0
    for each_item in data:
        print(
            f"""
                Name : {each_item["name"]}
                Symbol : {each_item["symbol"]}
                Market_cap_rank : {each_item["market_cap_rank"]}
            """
        )
        i+=1
        if i == 5:
            break