# -*- coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv
import scipy.signal
import numpy as np
import pylab

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
x = []
x1 = []
y = []
y1 = []

with open('附件1.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y.append(row[0])  # 将第一列数据添加到x列表
        # x.append(row[6])

# x轴数据
for i in range(4200):
    x.append(i)

# 把第一行描述行删除，切片
y1 = y[1:]

y2 = []  # 临时变量
for n in y1:
    y2.append(float(n))
y1 = y2

pylab.plot(x, y1, 'o')
z = np.polyfit(x, y1, 1)
p = np.poly1d(z)
pylab.plot(x, p(y1), "r")
plt.show()
