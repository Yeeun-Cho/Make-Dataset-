import pandas as pd
from datetime import datetime
import numpy as np

column = set(['date', 'Date', 'open', 'Open', 'high', 'High', 'Low', 'low', 'Close', 'close', 'Volume', 'volume', 'ma_5', 'ma_20', 'ma_60', 'ma_120', 'ma_240'])



def correction(data):
    data = data.replace(0, np.NaN)
    data = data.dropna()
    data = data.reset_index()
    columns = set(data)
    delete_col = columns - column
    for i in delete_col:
        del data[i]
    
    try :
        data.columns = ['Date', 'Open', 'High' ,'Low' ,'Close', 'Volume', 'ma_5', 'ma_20', 'ma_60', 'ma_120', 'ma_240']
    except ValueError:
        data.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    data['Date'] = data['Date'].map(correct_date)
    # print(data)
    return data

def correct_date(date):
    date = str(date)
    date = date[:4] + '-' + date[4:6] + '-' + date[6:]
    return date

