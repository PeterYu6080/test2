#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 18:06:39 2024

@author: peter68
"""
import numpy as np

def str_date_tf(string_date): # 調整日期格式，讓日期具有數字特性，做比較
    return int(''.join(string_date.split('/')))
    
def get_date_df (df, start_date, end_date): # 確認輸入日期，是不是存在於df內
    if start_date not in df['日期'].values or end_date not in df['日期'].values:
        print("錯誤：輸入日期不再範圍內")
        return None
    else:
        st = np.array([str_date_tf(i)for i in df['日期']],dtype = 'i')
        date_df = df.loc[(st >= str_date_tf(start_date)) & (st <= str_date_tf(end_date))]
        return date_df
    
    
def convert_to_float(x):
    try:
        return float(x.replace(',', ''))
    except ValueError:
        return x  # 如果无法转换为float，则保留原始值
