import csv

import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
x = []
x1 = []
y = []
y1 = []

with open('附件1.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y.append(row)  # 将第一列数据添加到x列表
# print(y)
y = y[1:]


# y[0] = list(map(float, y[0]))
print(y[0])