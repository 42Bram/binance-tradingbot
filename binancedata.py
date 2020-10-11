# IMPORTS
import pandas as pd
from binance.client import Client
import matplotlib.pyplot as plt

### API
binance_api_key = '9gEbfoHDcwqzeMHKKXZ6iXYt8sCqeyYOHk3UtWuYWHosMeowGJpD41mQjqgxq8LZ'    #Enter your own API-key here
binance_api_secret = '38afIXlCdYonYvCmTlcUNsWIKj1HFiXD8EPEo7VF1z1pxnVZXkq12aThrmel1WHa' #Enter your own API-secret here

client = Client(binance_api_key, binance_api_secret)

klines = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_1MINUTE)
data = pd.DataFrame(klines,
                    columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades',
                             'tb_base_av', 'tb_quote_av', 'ignore'])
data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')

print(data)

