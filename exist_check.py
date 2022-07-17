from tkinter import Label
import pandas as pd
import os.path

def labeling_check(time_log, dp, fore, ticker, labeling):

    if time_log is None :
        return 0

    is_ticker = time_log['Ticker'] ==  ticker
    is_labeling = time_log['Labeling'] == labeling
    is_dp = time_log['DP'] == str(dp)
    is_fore = time_log['Fore'] == str(fore)
    is_labeling_finished = is_ticker & is_labeling & is_dp & is_fore

    if time_log[is_labeling_finished].empty :
        return 0
    elif time_log[is_labeling_finished]['Labeling Time'].tolist()[0] == 0 :
        return 0
    else :
        time = time_log[is_labeling_finished]['Labeling Time'].tolist()[0]
        return time


def candlestick_check(path) :
    file_exists = os.path.exists(path)
    return file_exists

def total_check(time_log, start_d, end_d, dp, tp, fore, size, is_v, ma, labeling, ticker) :
    if time_log is None :
        return -1

    is_ticker = time_log['Ticker'] == ticker
    is_labeling = time_log['Labeling'] == labeling
    is_start_d = time_log['Start Date'] == start_d
    is_end_d = time_log['End Date'] == end_d
    is_dp = time_log['DP'] == str(dp)
    is_tp = time_log['TP'] == str(tp)
    is_fore = time_log['Fore'] == str(fore)
    is_size = time_log['Size'] == str(size)
    is_vol = time_log['Volume'] == str(is_v)
    is_ma = time_log['MA'] == str(ma)

    is_total_finished = is_ticker & is_labeling & is_dp & is_fore & is_tp & is_size & is_vol & is_ma & is_start_d & is_end_d

    print(time_log[is_total_finished])
    if time_log[is_total_finished].empty :
        print('total is -1')
        return -1
    elif time_log[is_total_finished]['Total Time'].values == [0] :
        print('total is not')
        return time_log.index(time_log[is_total_finished])
    else :
        print('total is 2')
        return 2