#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:13:40 2024

@author: peter68
"""

import csv

def append_csv(main_file, new_file):
    # 打開主要的檔案
    with open(main_file, 'r', newline='', encoding='utf-8') as main_csvfile:
        main_reader = csv.reader(main_csvfile)
        main_data = list(main_reader)
    try:
        


        # 打開新的檔案
        with open(new_file, 'r', newline='', encoding='utf-8') as new_csvfile:
            new_reader = csv.reader(new_csvfile)
            new_data = list(new_reader)[2:]

        # 把新的檔案 加入到 主要檔案中
        main_data.extend(new_data)

        # 把合併後的資料寫入主要檔案中
        with open(main_file, 'w', newline='', encoding='utf-8') as combined_csvfile:
            writer = csv.writer(combined_csvfile)
            writer.writerows(main_data)

        print("成功。")

    except FileNotFoundError:
        print("文件不存在。")

if __name__ == "__main__":
    main_file = input("舊CSV文件的路徑：")
    new_file = input("新CSV文件的路徑：")
    append_csv(main_file, new_file)