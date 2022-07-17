from datetime import datetime
import pandas as pd
from Model import *

def sample_num(sample, train_date, val_date, test_date, label_num) :
    days = [train_date.days, val_date.days, test_date.days]
    
    total = sum(days)
    sample_per_days = [(sample * x) // total for x in days]
    sample_per_days[0] += sample - sum(sample_per_days)
    
    sample_per_label = [(x // label_num, x % label_num) for x in sample_per_days]
    sample_dic = {'train': sample_per_label[0], 'validation': sample_per_label[1], 'test': sample_per_label[2]}
    print(sample_dic)
    return sample_dic

def sampling(labeling_df, path, date, label_num, sample_dic) :
    num = [sample_dic[date.type][0] for i in range(label_num)]
    num[0] += sample_dic[date.type][1]
    
    for label in range(label_num) :
        condition = (labeling_df['Label'] == label) & (labeling_df['Date'] >= date.start) & (labeling_df['Date'] <= date.end)
        
        try :
            sample = labeling_df[condition].sample(num[label])
        except ValueError:
            sample = labeling_df[condition]

        if label == 0 :
            labeling_sample_df = sample
        else :
            labeling_sample_df = pd.concat([labeling_sample_df, sample])
    
    labeling_sample_df.to_csv(path.label + f'/{date.type}_label.csv')