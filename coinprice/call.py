import requests
import json
from datetime import datetime


class API:
    """ ..............................................
        this script use https://www.coingecko.com/ api
        ..............................................
    """
    __API_BASE_URL = "https://api.coingecko.com/api/v3/"

    def __init__(self):
        pass

    def __request(self, url, coin):
        """ ............................................
            for making call to api with requests package
            ............................................
        """
        try:
            response = requests.get(url)
            response = json.loads(response.content)
            today = str(datetime.now())
            price = str(response[coin]['usd'])
            print(today + " :: Price is " + price + " USD")
        except:
            print("somethings wrong!")

    def call(self, coin):
        url = self.__API_BASE_URL + \
            "simple/price?ids={coin}&vs_currencies=usd".format(coin=coin)
        return self.__request(url, coin)

    def ping():
        """ ........................
            for check the connection
            ........................
        """
        ping = "https://api.coingecko.com/api/v3/ping"

        r = requests.get(ping)

        if r.status_code == 200:
            print("Up to the Moon!")
        else:
            print("Server is Down!")
