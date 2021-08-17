import csv
import matplotlib
from datetime import datetime
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False  ## 设置正常显示符号
x = []  # 国控点

y = []  # 自建点

with open('附件2.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y.append(row)  # 将第一列数据添加到x列表
# print(y)
# 切片将表头去除
y = y[1:]

with open('附件1.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row)
x = x[1:]

# 将二位数组y中的字符串类型数据转换成浮点数
for i in range(4200):
    for j in range(6):
        x[i][j] = float(x[i][j])

# 将二位数组y中的字符串类型数据转换成浮点数
for i in range(234717):
    for j in range(11):
        y[i][j] = float(y[i][j])
# print(y)

# 转换时间类型字符串
for i in range(234717):
    y[i][11] = datetime.strptime(y[i][11], '%Y/%m/%d %H:%M')
    # print(y[i][6].year)

PMx = []  # 国控pM2.5
PMy = []  # 自建pM2.5

hour = 10
for i in range(234717):
    if hour < 24:
        if int(y[i][11].hour) == hour:
            PMy.append(y[i][0])
            hour += 1
            with open("自建整点.csv", "a+", encoding="utf-8", newline="") as openFile:
                PM2 = y[i][0]
                PM10 = y[i][1]
                CO = y[i][2]
                NO2 = y[i][3]
                SO2 = y[i][4]
                O3 = y[i][5]
                win = y[i][6]
                P = y[i][7]
                rain = y[i][8]
                T = y[i][9]
                shidu = y[i][10]
                time = y[i][11]
                data = [PM2, PM10, CO, NO2, SO2, O3, win, P, rain, T, shidu, time]
                csv.writer(openFile).writerow(data)
    else:
        hour = 0

# print(PM)

for i in range(4200):
    PMx.append(x[i][0])


PMx = PMx[300:600]
PMy = PMy[300:600]

plt.plot(PMy, label=u'自建点PM2.5整点数据')
plt.plot(PMx, label=u'国控点PM2.5整点数据')
plt.xlabel("附件2的数据记录号")  # X轴标签
plt.ylabel("PM2.5值")  # Y轴标签
plt.title("PM2.5整点值分析")  # 标题
plt.legend()
plt.show()
