import pandas as pd
import os
from management_data import *
from labeling import *
from make_dataset import *
from exist_check import *
from Model import *
from sampling import *
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def get_label_num(labeling) :
    return len(labeling.split('0')[-1]) + 1  

def main(args):
    print(args) # print arguments

    output_dir = args['output_dir'] # output path
    input_dir = args['input_dir'] # stock datas path
    is_v = args['volume']
    ma = args['moving_average']
    dp = args['day_period']
    train = args['train']
    validation = args['validation']
    test =args['test']
    fore = args['forecast']
    size = args['image_size']
    labeling = args['labeling'] # What labeling is chosen
    sample = args['sample']
    label_num = get_label_num(labeling)
    
    path = WholePath(input_dir, output_dir)
    train_date = Date(train[0], train[1], 'train')
    val_date = Date(validation[0], validation[1], 'validation')
    test_date = Date(test[0], test[1], 'test')
    dates = [train_date, val_date, test_date]
    sample_dic = sample_num(sample, train_date, val_date, test_date, label_num)
    
    path.set_path(labeling, label_num)
    path.make_dir()

    files = os.listdir(path.input) # stock datas list (list of '{ticker}.csv')
    stock = {}
    count = 1
    for file in files:
        ticker = file.split('.')[0] # ticker
        
        print('\nTicker {}/{}\t{}'.format(count, len(files), ticker))
        data_path = os.path.join(path.input, file)
        data = pd.read_csv(data_path)
        data = correction(data) # correct {ticker}.csv
        stock[ticker] = data
        process_labeling(path, dp, fore, data, ticker, labeling) # Labeling
        count += 1
        
    labeling_df = pd.read_csv(path.label + f'/{labeling}.csv')
    
    for date in dates :
        print(date.type)
        sampling(labeling_df, path, date, label_num, sample_dic)
        make_dataset(path, date.type, stock, dp, fore, size, is_v, ma, labeling)
        
if __name__=='__main__':
    args = {
        'input_dir' : 'C:/Users/Marisa/Documents/skku/3-1.5/server/7_12/sample',
        'output_dir' : 'C:/Users/Marisa/Documents/skku/3-1.5/server/7_12/output',
        'volume' : False,
        'moving_average' : [5, 20],
        'day_period' : 20,
        'train' : ['2006-01-01', '2017-12-31'],
        'validation' : ['2018-01-01', '2018-12-31'],
        'test' : ['2019-01-01', '2019-12-31'],
        'forecast' : 5,
        'image_size' : [50, 50],
        'labeling' : '5%_012',
        'sample' : 200
    }
    main(args)