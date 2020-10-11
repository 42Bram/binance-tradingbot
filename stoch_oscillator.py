# IMPORTS
import pandas as pd
from binance.client import Client
import matplotlib.pyplot as plt
import numpy as np

### API
binance_api_key = '9gEbfoHDcwqzeMHKKXZ6iXYt8sCqeyYOHk3UtWuYWHosMeowGJpD41mQjqgxq8LZ'    #Enter your own API-key here
binance_api_secret = '38afIXlCdYonYvCmTlcUNsWIKj1HFiXD8EPEo7VF1z1pxnVZXkq12aThrmel1WHa' #Enter your own API-secret here

client = Client(binance_api_key, binance_api_secret)

klines = client.get_klines(symbol='VETUSDT', interval=Client.KLINE_INTERVAL_5MINUTE)
df = pd.DataFrame(klines,
                    columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades',
                             'tb_base_av', 'tb_quote_av', 'ignore'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
pd.to_datetime(client.get_server_time()['serverTime'], unit='ms')
df.set_index('timestamp', inplace=True)
pd.to_numeric(df['high'])
pd.to_numeric(df['low'])
df['STOKmin'] = df['low'].rolling(5).min()
df['STOKmax'] = df['high'].rolling(5).max()
pd.to_numeric(df['STOKmin'])
pd.to_numeric(df['STOKmax'])

for index, row in df.iterrows():
    #Stochastic Oscillator
    df.loc[index, 'STOK'] = (float(row['close']) - row['STOKmin']) / (row['STOKmax'] - row['STOKmin']) * 100
df['STOD'] = df['STOK'].rolling(3).mean()
df['20level'] = 20
df['80level'] = 80
plotdata = df.tail(100)
plt.figure(figsize=(15, 6))
plt.legend(loc=2)
plt.plot(plotdata.index, plotdata['STOK'], label="STOK")
plt.plot(plotdata.index, plotdata['STOD'], label="STOD")
plt.plot(plotdata.index, plotdata['20level'], label="20")
plt.plot(plotdata.index, plotdata['80level'], label="80")
plt.legend(loc=2)
