from DBConnection import DBConnection
import requests

if __name__ == "__main__":
    connection = DBConnection("popular_coins")
    connection.create_table()

    response = requests.get("https://api.coinranking.com/v2/coins").json()

    for coin in response["data"]["coins"]:
        connection.insert_data({
            'id': str(coin["uuid"]),
            'name': str(coin["name"]),
            'symbol': str(coin["symbol"]),
            'icon': str(coin["iconUrl"]),
            'price': str(coin["price"]),
            'total_score': 0,
            'number_of_reviews': 0,
        })
