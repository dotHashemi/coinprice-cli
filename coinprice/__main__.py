import sys
from .coins import BTC
from .call import API


def main():
    # try:
    coin = sys.argv[1]

    if coin == "bitcoin" or coin == "BTC":
        BTC.price()
    elif coin == "ping":
        API.ping()
    else:
        print("help should be here!")
    # except:
    #     print("help file should be here!")


if __name__ == "__main__":
    main()
