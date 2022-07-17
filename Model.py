import os
from datetime import datetime

class WholePath :
    def __init__(self, input, output) :
        self.input = input
        self.output = output
        
    def set_path(self, labeling, label_num) :
        # Floor 1
        self.label = self.output + '/label'
        self.dataset = self.output + '/dataset'
        # Floor 2
        self.setbylabel = self.dataset + f'/{labeling}'
        # Floor 3
        self.train = self.setbylabel + '/train'
        self.val = self.setbylabel + '/validation'
        self.test = self.setbylabel + '/test'
        # Floor 4
        self.train_label = []
        self.val_label = []
        self.test_label = []
        for label in range(label_num) :
            self.train_label.append(self.train + f'/{label}')
            self.val_label.append(self.val + f'/{label}')
            self.test_label.append(self.test + f'/{label}')
        self.label_dic = {'train': self.train_label, 'validation': self.val_label, 'test': self.test_label}
            
    def make_dir(self) :
        os.makedirs(self.label, exist_ok=True)
        for label in range(len(self.train_label)) :
            os.makedirs(self.train_label[label], exist_ok=True)
            os.makedirs(self.val_label[label], exist_ok=True)
            os.makedirs(self.test_label[label], exist_ok=True)
    
    def image_name(self, ticker, date, volume, ma, dp, fore, labeling, label) :
        ma = list(map(str, ma))
        if volume :
            is_vol = 'O'
        else :
            is_vol = 'X'
        if ma == [-1] :
            is_ma = 'X'
        else :
            is_ma =  ",".join(ma)
        name = f'/{ticker}_{date}_vol({is_vol})_ ma({is_ma})_{dp}_{fore}_({labeling})_{label}.png'
        return name

class Date:
    def __init__(self, start, end, type) :
        self.start = start
        self.end = end
        self.type = type
        self.days = self.calculate_day(self.start, self.end)
    
    def calculate_day(self, start_date, end_date) :
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, '%Y-%m-%d')
        date_diff = end - start
        return date_diff.days
    