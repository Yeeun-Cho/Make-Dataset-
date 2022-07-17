import pandas as pd
from management_data import *
from make_candlestick import *

# SettingWithCopyWarning ignore
pd.set_option('mode.chained_assignment',  None)

def make_dataset(path, type, stock, dp, fore, size, is_vol, MAs, labeling) :
    labeling_df = pd.read_csv(path.label + f'/{type}_label.csv')
    labeling_df['Label'] = labeling_df['Label'].map(str)
    labeling_list = (labeling_df['Date'].to_numpy() + ' ' + labeling_df['Ticker'].to_numpy() + ' ' + labeling_df['Label'].to_numpy()).tolist()
    for temp in labeling_list :
        date, ticker, label = temp.split(' ')
        label = int(label)
        df = stock[ticker]
        make_candlestick(path, type, ticker, date, label, labeling, dp, fore, size, is_vol, MAs, df)
    print('Create dataset finished.')