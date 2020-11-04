# -*- coding: utf-8 -*-
# 数据读取工具
import pandas as pd
import os

def data_read(data_path,file_name):
    df = pd.read_csv(os.path.join(data_path,file_name),delim_whitespace = True,header = None)
    ##变量重命名
    columns = ['status_account','duration','credit_history','purpose','amount','svaing_account',
               'present_emp','income_rate','personal_status','other_debtors','residence_info',
               'property','age','inst_plans','housing','num_credits','job','dependents',
               'telephone','foreign_worker','target']
    df.columns = columns
    df.target = df.target -1
    return df

df = data_read('/Users/wanggaojie/PycharmProjects/IntelligentRiskControl/code/chapter4/data','german.csv')

def category_continue_separation(df,feature_names):
    categorical_var = []
    numerical_var = []
    if 'target' in feature_names:
        feature_names.remove('target')
    ##先判断类型，如果是int或float直接作为连续变量
    numerical_var = list(df[feature_names].select_dtypes(include=['int','float','int32','float32','int64','float64']).columns.values)
    categorical_var = [x for x in feature_names if x not in numerical_var]
    return categorical_var,numerical_var

def add_str(x):
    str_1 = ['%',' ','/t','$',';','@']
    str_2 = str_1[np.random.randint(0,high = len(str_1)-1)]
    return x+str_2

df.status_account = df.status_account.Apply(add_str)

def add_time(num,style="%Y-%m-%d"):
    start_time = time.mktime((2010,1,1,0,0,0,0,0,0))
    stop_time = time.mktime((2015,1,1,0,0,0,0,0,0))
    re_time = []
    for i in range(num):
        rand_time = np.random.randint(start_time,stop_time)
        #将时间戳生成时间元组
        date_touple = time.localtime(rand_time)
        re_time.Append(time.strftime(style,date_touple))
    return re_time
df['Appliy_time'] = add_time(df.shape[0], "%Y-%m-%d")
df['job_time'] = add_time(df.shape[0],"%Y/%m/%d %H:%M:%S")








