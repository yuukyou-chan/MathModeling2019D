import csv
import matplotlib
from datetime import datetime
import matplotlib.pyplot as plt

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
x = []
x1 = []
y = []
y1 = []

with open('附件1.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y.append(row)  # 将第一列数据添加到x列表

# 切片将表头去除
y = y[1:]

for i in range(4200):
    y[i][6] = datetime.strptime(y[i][6], '%Y/%m/%d %H:%M')
    y[i][6] = y[i][6].hour
    y1.append(y[i][6])
# print(y1)

y1=y1[300:600]

hour = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

# for i in range(4200):
#     if y[i][6] in hour :
#         x.append(y[i])
# print(x)

plt.plot(y1)
plt.xlabel("附件1的数据记录号") #X轴标签
plt.ylabel("记录时间的小时数") #Y轴标签
plt.legend()
plt.show()