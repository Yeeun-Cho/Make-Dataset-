import pandas as pd
import numpy as np

labeling_df = pd.read_csv('5%_01.csv')

labeling_list = (labeling_df['Date'].to_numpy() + ' ' +labeling_df['Ticker'].to_numpy()).tolist()
# print(labeling_list)
for temp in labeling_list :
    date, ticker = temp.split(' ')
    