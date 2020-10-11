from binance.enums import *
from config import client

def buy(price):
    quantity = (float(client.get_asset_balance(asset='USDT')['free']) / float(price)) * 0.995
    print(client.order_market_buy(
        symbol='VETUSDT',
        quantity=int(quantity)))
    print(f"Bought {quantity} VET")
    print(f"VET: {client.get_asset_balance(asset='VET')}")
    print(f"USD: {client.get_asset_balance(asset='USDT')}")


def sell():
    quantity = (float(client.get_asset_balance(asset='VET')['free']))
    print(client.order_market_sell(
        symbol='VETUSDT',
        quantity=int(quantity)))

    print(f"Sold {quantity} VET")
    print(f"VET: {client.get_asset_balance(asset='VET')}")
    print(f"USD: {client.get_asset_balance(asset='USDT')}")