from tradingdata import trading_data
import time
from orders import buy, sell
from datetime import datetime
from config import client
from trades import market_buy, limit_sell


def monitor_long():
    hold = True
    while hold == True:
        data = (trading_data())
        if data['MA_ratio'] < 1:
            sell()
            time.sleep(180)
            monitor_short()
            hold = False
        else:
            print(data)
        time.sleep(2)

def monitor_short():
    hold = False
    while hold == False:
        data = (trading_data())
        if data['MA_ratio'] > 1:
            buy(price = data['close_price'])
            time.sleep(180)
            monitor_long()
            hold = True
        else:
            print(data)
        time.sleep(2)

def write_positions():
    with open ('positions.txt', 'a+') as file:
        time = datetime.now()
        vet = client.get_asset_balance(asset='VET')
        usd = client.get_asset_balance(asset='USDT')
        positions = (f'{time}, {vet}, {usd}\n')
        file.write(positions)

# When running the script it prints the current positions and writes them to a text file for monitoring purposes
print(client.get_open_orders(symbol='VETUSDT'))
write_positions()

# By using below strategy coins are bought at a certain price level and a limit sell is create simultaneously
price = market_buy(250000)
limit_sell(price)
print(f"VET: {client.get_asset_balance(asset='VET')}")
print(f"USD: {client.get_asset_balance(asset='USDT')}")



