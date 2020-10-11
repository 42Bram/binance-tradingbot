# IMPORTS
import pandas as pd
from binance.client import Client
from config import client
import matplotlib.pyplot as plt
import numpy as np
import time

def trading_data():
    ### API
    klines = client.get_klines(symbol='VETUSDT', interval=Client.KLINE_INTERVAL_5MINUTE)
    df = pd.DataFrame(klines,
                        columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades',
                                 'tb_base_av', 'tb_quote_av', 'ignore'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
    df.set_index('timestamp', inplace=True)
    pd.to_datetime(client.get_server_time()['serverTime'], unit='ms')
    df = df.tail(100)

    ### Moving averages
    df['MA7'] = df['close'].rolling(7).mean()
    pd.to_numeric(df['MA7'])
    df['MA25'] = df['close'].rolling(25).mean()
    pd.to_numeric(df['MA25'])

    ### Trends
    for index, row in df.iterrows():
        if row['MA25'] != "NaN":
            if row['MA7'] > row['MA25']:
                df.loc[index, 'direction'] = 'LONG'
            else:
                df.loc[index, 'direction'] = 'SHORT'
            df.loc[index, 'MA_ratio'] = row['MA7'] / row['MA25']
    current = df.tail(1)
    close_price = current.iloc[-1]['close']
    MA_ratio = current.iloc[-1]['MA_ratio']
    direction = current.iloc[-1]['direction']
    data = {"MA_ratio": MA_ratio, "direction": direction, "close_price": close_price}
    return (data)
