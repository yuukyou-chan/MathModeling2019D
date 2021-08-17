import csv
import matplotlib
from datetime import datetime
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

x = []

with open('附件1.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row)

hour = 10
for i in range(234717):
    if hour < 23:
        if int(x[i][11].hour) == hour:
            x.append(x[i][0])
            hour += 1
    else:
        hour = 0

# 将二位数组y中的字符串类型数据转换成浮点数
for i in range(4200):
    for j in range(6):
        x[i][j] = float(x[i][j])