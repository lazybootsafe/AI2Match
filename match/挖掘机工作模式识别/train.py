# 解压
!ls ../input/*/*.zip | xargs -n1 unzip -d /home/workspace/
# 安装环境

!pip install tqdm
!pip install lightgbm

# 数据和特征的处理 
from tqdm import tqdm
import pandas as pd
import os
import sys

origin_cols = ['receive_time', 'serial_no', 'action_code', 'alarm_code', 'altitude',
       'auto_idling', 'avg_fuel_consumption', 'battery_voltage',
       'cooling_water_temperature', 'day_fuel_consumption',
       'displacement_direction', 'displacement_speed', 'engine_output_power',
       'engine_output_torque', 'engine_speed', 'fuel_level',
       'fuel_temperature', 'gear', 'hydraulic_oil_temperature',
       'intake_temperature', 'oil_pressure', 'pump1_current', 'pump1_flow',
       'pump1_pressure', 'pump2_current', 'pump2_flow', 'pump2_pressure',
       'pump_total_absorbed_power', 'pump_total_absorbed_torque',
       'realtime_fuel_consumption', 'total_idle_time', 'workmode']

def get_features(data):
    data = data.sort_values('receive_time')
    for f in ['action_code', 'alarm_code', 'auto_idling', 'workmode', 'intake_temperature', 'gear', 'fuel_temperature', 'displacement_speed']:
        data[f'{f}_nunique'] = data[f].nunique()
    
    data['count'] = len(data)
    for f in ['altitude', 'avg_fuel_consumption', 'cooling_water_temperature', 'battery_voltage', 'day_fuel_consumption', 'displacement_direction', 'engine_output_power', 'engine_speed',
             'fuel_level', 'hydraulic_oil_temperature', 'intake_temperature', 'oil_pressure', 'pump1_current', 'pump1_flow', 'pump1_pressure', 'pump_total_absorbed_power', 'pump_total_absorbed_torque',
              'realtime_fuel_consumption', 'total_idle_time'
             ]:
        data[f'{f}_max'] = data[f].max()
        data[f'{f}_mean'] = data[f].mean()
        data[f'{f}_min'] = data[f].min()
        data[f'{f}_std'] = data[f].std()
        data[f'{f}_skew'] = data[f].skew()
    return data.drop_duplicates('serial_no').drop(origin_cols, axis=1)

print(os.path)
print(sys.path)
print(os.getcwd())#目录信息
mode1_list = os.listdir('/home/workspace/train/mode1') #相对路径../train/mode1 --> /home/workspace
mode2_list = os.listdir('/home/workspace/train/mode2')

data = None
for path in tqdm(mode1_list):
    d = pd.read_csv('/home/workspace/train/mode1/' + path)
    d = get_features(d)
    d['label'] = 1
    data = pd.concat([data, d])
    
for path in tqdm(mode2_list):
    d = pd.read_csv('/home/workspace/train/mode2/' + path)
    d = get_features(d)
    d['label'] = 0
    data = pd.concat([data, d])
    
features = data.columns
features = features.drop('label')

# 模型构建

import lightgbm as lgb
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score, precision_score, recall_score
import warnings


warnings.filterwarnings('ignore')

X_train, X_test = data[~data['label'].isna()], data[data['label'].isna()]
y = X_train['label']
KF = StratifiedKFold(n_splits=5, shuffle=True, random_state=2021)
params = {#这内容对应run.py内容，可查看
    'verbose':-1,
    'num_leaves':64,
    'max_depth':10,
    'learning_rate':0.01,
    'n_estimators':10000,
    'subsample':0.8,
    'feature_fraction':0.8,
    'reg_alpha':0.5,
    'reg_lambda':0.5,
    'random_state':2021,
    'metric':'auc'
}

oof_lgb = np.zeros(len(X_train))

for fold_, (trn_idx, val_idx) in enumerate(KF.split(X_train.values, y.values)):
    print("fold n°{}".format(fold_))
    trn_data = lgb.Dataset(X_train.iloc[trn_idx][features],label=y.iloc[trn_idx])    
    val_data = lgb.Dataset(X_train.iloc[val_idx][features],label=y.iloc[val_idx])
    num_round = 10000
    clf = lgb.train(
        params,
        trn_data,
        num_round,
        valid_sets = [trn_data, val_data],
        verbose_eval=500,
        early_stopping_rounds=100,  #这个值可以相应调小
        
    )
        
    oof_lgb[val_idx] = clf.predict(X_train.iloc[val_idx][features], num_iteration=clf.best_iteration)
    clf.save_model(f'model/model_{fold_}.txt')
    
print("AUC score: {}".format(roc_auc_score(y, oof_lgb)))
print("F1 score: {}".format(f1_score(y, [1 if i >= 0.5 else 0 for i in oof_lgb])))
print("Precision score: {}".format(precision_score(y, [1 if i >= 0.5 else 0 for i in oof_lgb])))
print("Recall score: {}".format(recall_score(y, [1 if i >= 0.5 else 0 for i in oof_lgb])))