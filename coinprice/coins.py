from .call import API


class BTC:
    __COIN = "bitcoin"

    def __init__(self):
        pass

    def price():
        api = API()
        return api.call(BTC.__COIN)
