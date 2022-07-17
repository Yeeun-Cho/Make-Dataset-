import matplotlib.dates as mdates
import pandas as pd
import os
import warnings
from tqdm import trange
from Model import *
warnings.filterwarnings("ignore", category=RuntimeWarning) 

def process_labeling(path, dp, fore, df, ticker, labeling) :
    save = path.label + f'/{labeling}.csv'
    date = df['Date']
    
    print('\nLabeling')
    for i in trange(len(df)):
        c = df.iloc[i:i + int(dp), :]
        try:
            f = df.iloc[i+int(dp)+fore-1, :]
        except IndexError :
            continue
        
        starting = 0
        endvalue = 0
        label = ""

        if len(c) == int(dp):
            if labeling == '5%_012':
                starting = c["Close"].iloc[-1] 
                endvalue = f["Close"]
            
                if starting * 0.95 >= endvalue:
                    label = 1
                elif starting * 1.05 <= endvalue:
                    label = 2
                else:
                    label = 0

            elif labeling == '5%_01' :
                starting = c["Close"].iloc[-1] 
                endvalue = f["Close"]
            
                if endvalue >= 1.05 * starting:
                    label = 1
                else:
                    label = 0

            elif labeling == 'High_Low_01' :
                starting = c["High"].iloc[-1] 
                endvalue = f["Low"]
            
                if endvalue > starting:
                    label = 1
                else:
                    label = 0

            elif labeling == '0123' :
                label_row = f
                candle = label_row["Close"] - label_row["Open"]
                line = label_row["High"] - label_row["Low"]

                if candle <= 0.0:
                    label = 0
                    if abs(candle) / line >= 0.7:
                        label = 1
                else:
                    label = 2
                    if abs(candle) / line >= 0.7:
                        label = 3
            else :
                print('Please Select Correct Labeling!\n')
                quit()
            
            labeling_row = pd.DataFrame({'Date': [date[i]], 'Ticker': [ticker], 'Label': [label]})

            if not os.path.exists(save):
                labeling_row.to_csv(save, index=False, mode='w', encoding='utf-8')
            else:
                labeling_row.to_csv(save, index=False, mode='a', encoding='utf-8', header=False)
            