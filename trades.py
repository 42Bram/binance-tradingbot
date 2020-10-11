from binance.enums import *
from config import client


def market_buy(quantity):
    print("\nBuy order")
    order = client.order_market_buy(
        symbol='VETUSDT',
        quantity=quantity)
    print(order)
    price = order['fills'][0]['price']
    print(price)
    return price

def limit_sell(price):
    print("\nSell order")
    price = float(price) * 1.006
    price = round(price, 5)
    vet = float(client.get_asset_balance(asset='VET')['free'])
    order = client.order_limit_sell(
        symbol='VETUSDT',
        quantity= int(vet),
        price= price)
    print(order)

