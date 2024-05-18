#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 17:53:41 2024

@author: peter68
"""
#沒有限制版本

import csv
import numpy as np
import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt
import my_module as mm
import matplotlib




with open('S2330_202301.csv','r') as f:

    r = csv.reader(f) # 讀取
    sk_df = pd.DataFrame(list(r)[2:]) # 選取有效資料範圍
    sk_df2 = sk_df.drop([9],axis = 1) # 刪除 axis = 1是 欄，把最後一欄（無用資料），刪除
    sk_df2.columns = ['日期', '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']
    
    
    
    # 選取本次要用的項目，日期為必要條件
    print('Select 2 columns: 成交股數/成交金額/開盤價/最高價/最低價/收盤價/漲跌價差/成交筆數 (以 / 隔開)')
    allowed_indices = ['成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']
    while True:
        columns_input = ('收盤價/成交金額/成交筆數').split('/')#input('2 columns').split('/')
        

        if all(columns in allowed_indices for columns in columns_input):
            columns_input.insert(0, '日期') 
            print(columns_input)
            break
        else:
                print("錯誤的輸入，請確認是有效的index。")  
    date_df = sk_df2[columns_input]
    print(date_df)

    
    start_date = '112/01/03'
    end_date = '113/04/24'
    date_df = mm.get_date_df(date_df, start_date, end_date)
    print(date_df)
    '''
    #以日期為單位，選定資料範圍
    count = 0
    input_msg = ["請輸入開始日期或quit", "請輸入結束日期或quit"]
    user_in = input(input_msg[count]).lower()
    values = []
    while user_in != "quit":
        try:
            values.append(user_in)
            if count % 2 == 1:
                start_date = values[0]
                end_date = values[1]
                date_df = mm.get_date_df(date_df, start_date, end_date)
                if date_df is not None:
                    print(f"{start_date}到{end_date}的{date_df.columns}是:")
                    print(date_df)    
                values = []
                count = 0
            else:
                count += 1
        except Exception as e:
            print(e)
        user_in = input(input_msg[count])
    '''


    for col in date_df.columns:
        if col != '日期' and col != '漲跌價差':
            date_df.loc[:, col] = date_df[col].apply(mm.convert_to_float)    
        
        if col == '漲跌價差':
            date_df['漲跌價差'] = date_df['漲跌價差'].replace('X0.00', '0')
            
            date_df['漲跌價差'] = date_df['漲跌價差'].str.replace('+', '').astype(float)
    #測試
    '''
    fig, ax1 = plt.subplots(figsize=(18, 12))  # Create a single subplot
    ax2 = ax1.twinx()  # Create a secondary y-axis that shares the same x-axis
    
    # Plot '收盤價' data on the primary y-axis (ax1)
    ax1.plot(date_df['日期'], date_df['收盤價']/date_df['收盤價'].max(), color='blue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('收盤價')
    ax1.tick_params(axis='x', rotation=45)
    
    # Plot '成交金額' data on the secondary y-axis (ax2)
    ax2.plot(date_df['日期'], date_df['成交金額']/date_df['成交金額'].max(), color='red')
    ax2.set_ylabel('成交金額')
    
    plt.tight_layout()
    plt.show()

    fig, axs = plt.subplots(1, 1, figsize=(18, 12))
    axs = np.atleast_1d(axs)
    for i, ax in enumerate(axs):
        
        ax.plot(date_df['日期'], date_df[date_df.columns[i+1]]/date_df[date_df.columns[i+1]].max(), color='blue')
        ax.set_xlabel('Date')
        ax.set_ylabel(date_df.columns[i+1])

        ax.tick_params(axis='x', rotation=45)
        ax.grid()
        
    plt.twinx()
    plt.tight_layout()
    plt.show()
    '''
    
    '''
    fig, axs = plt.subplots(len(date_df.columns[1:]), 1, figsize=(18, 12))
    axs = np.atleast_1d(axs)
  
    for i, ax in enumerate(axs):
        number = pd.Series(date_df.columns[i+1])
        ax.plot(date_df['日期'], date_df[date_df.columns[i+1]], color='blue')
        ax.set_xlabel('Date')
        ax.set_ylabel(date_df.columns[i+1])
        ax.set_title(date_df.columns[i+1])
        ax.tick_params(axis='x', rotation=45)
        ax.grid()
    plt.savefig('/Users/peter68/Desktop/test1.png',transparent=True)
  
    plt.tight_layout()
    plt.show()
    '''
    
    
    

    count = 0
    input_msg = ["請輸入要運算的第一個index", "請輸入要運算的第二個index"]
    operation = input("輸入操作 (+, -, *, /): ")
    user_in = input(input_msg[count])
    user_in_list = []
    values = []
    if operation != 'quit':
        while user_in != "quit":
            try:
                
                values.append(date_df[user_in])
                user_in_list.append(user_in)
                if count % 2 == 1:
                    if operation == '+':
                        result = values[0] + values[1]
                    elif operation == '-':
                        result = values[0] - values[1]
                    elif operation == '*':
                        result = values[0] * values[1]
                    elif operation == '/':
                        result = np.where(values[1] != 0, values[0] / values[1], np.nan)
                    
                    date_df[f'{user_in_list[0]} {operation} {user_in_list[1]}']= result
                    print(f"结果为：{date_df}")

                    values = []
                    count = 0
                else:
                    count += 1
            except Exception as e :
                print(e)
            finally:
                user_in = input(input_msg[count])
            
    else:
        pass
    

    
    
    
    fig, axs = plt.subplots(len(date_df.columns[1:]), 1, figsize=(18, 12))
    axs = np.atleast_1d(axs)
  
    for i, ax in enumerate(axs):
        ax.plot(date_df['日期'], date_df[date_df.columns[i+1]], color='blue')
        ax.set_xlabel('Date')
        ax.set_ylabel(date_df.columns[i+1])
        ax.set_title(date_df.columns[i+1])
        ax.tick_params(axis='x', rotation=45)
        ax.grid()
    plt.savefig('/Users/peter68/Desktop/test1.png',transparent=True)
    plt.tight_layout()
    plt.show()

    cycle = input('5=週 ,20=月 ,120＝半年,240=年,或quit')
    while cycle != "quit":

        cycle_df = date_df.iloc[::int(cycle)]
        
        print(cycle_df)
        print(f'是否要計算指定週期 {cycle}筆的平均，y or n')
        averages_check = 'y'#input('y or n').lower()
        cycle_list=[]
        count = ''
        if averages_check == 'y':
            try:
                for column in list(date_df.columns)[1:]:
                    averages = []
                    for i in range(0, len(date_df[column]), int(cycle)):
                        if i + int(cycle) <= len(date_df[column]):
                            avg = sum(date_df[column][i:i+int(cycle)]) / int(cycle)
                            averages.append(avg)                
                                 
    
                        else:
                            remaining = len(date_df[column]) - i
                            count = 1
                            print(f"Only {remaining} elements left")
                    cycle_list.append(averages)
                    print(f'{column}平均值： ',averages)
                print(cycle_list)
                if count == 1:
                            
                    fig, axs = plt.subplots(len(cycle_df.columns[1:]), 1, figsize=(18, 12))
            
                    axs = np.atleast_1d(axs)
                            
                            
                    for i, ax in enumerate(axs):
                            ax.plot(cycle_df['日期'][:-1], cycle_list[i], color='blue')
                            ax.set_xlabel('Date')
                            ax.set_ylabel(cycle_df.columns[i+1])
                            ax.set_title(cycle_df.columns[i+1])
                            ax.tick_params(axis='x', rotation=45)
                            ax.grid()
                    plt.savefig('/Users/peter68/Desktop/test2.png',transparent=True)        
                    plt.tight_layout()
                    plt.show()
                else:
                    fig, axs = plt.subplots(len(cycle_df.columns[1:]), 1, figsize=(18, 12))
            
                    axs = np.atleast_1d(axs)
                        
                        
                    for i, ax in enumerate(axs):
                        ax.plot(cycle_df['日期'], cycle_list[i], color='blue')
                        ax.set_xlabel('Date')
                        ax.set_ylabel(cycle_df.columns[i+1])
                        ax.set_title(cycle_df.columns[i+1])
                        ax.tick_params(axis='x', rotation=45)
                        ax.grid()
                    plt.savefig('/Users/peter68/Desktop/test2.png',transparent=True)
                    plt.tight_layout()
                    plt.show()
            except Exception as e:
                print(e)
            
                

        else:
            break
        cycle = input('5=週 ,20=月 ,120＝半年,240=年')
    
    
    
    
    
    # 時間週期，產出有週期性的Dataframe，指定5=週 ,20=月 ,120＝半年,240=年為間隔
    

         
'''
            fig, ax= plt.subplots(1,1,figsize=(18, 12))  # Create a single subplot

            # Create a secondary y-axis that shares the same x-axis
                
            # Plot '收盤價' data on the primary y-axis (ax1)
            ax.plot(cycle_df['日期'], [x / max(cycle_list[0]) for x in cycle_list[0]], color='blue')
            ax.set_xlabel('Date')
            ax.set_ylabel('收盤價')
            ax.tick_params(axis='x', rotation=45)
                
            # Plot '成交金額' data on the secondary y-axis (ax2)
            ax.plot(cycle_df['日期'], [x / max(cycle_list[1]) for x in cycle_list[1]], color='red')
            ax.set_xlabel('Date')
            ax.set_ylabel('成交金額')
            ax.tick_params(axis='x', rotation=45)
            
            plt.twinx()
            plt.tight_layout()
            plt.show()
''' 
    

        

    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        