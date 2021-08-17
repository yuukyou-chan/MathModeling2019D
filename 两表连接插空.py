# 将两个csv文件按列合并为一个csv
import pandas as pd
import os
import csv
import numpy as np
from pandas.core.frame import DataFrame

csv_1 = "自建整点.csv"
csv_2 = "国控点时间.csv"
csv_fiil = "合并.csv"


def merge(csv_1, csv_2):
    csv_1 = pd.read_csv(csv_1)
    csv_2 = pd.read_csv(csv_2)
    hb = pd.merge(csv_1, csv_2, how="right")
    hb.to_csv("合并.csv")


def csvToDataframe():
    tmp_lst = []
    with open('合并.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            tmp_lst.append(row)
    df = pd.DataFrame(tmp_lst[1:], columns=tmp_lst[0])
    print(df)
    return df


def fill(df):
    for i in df.columns:  # 遍历列
        if np.any(pd.isnull(df[i])) == True:  # 如果此列有NaN值
            df[i].fillna(value=df[i].mean(), inplace=True)
            np.any(pd.isnull(df))  # 检测是否替换完成
    df.to_csv("补充国控整点值.csv")


merge(csv_1, csv_2)
# fill(csvToDataframe())