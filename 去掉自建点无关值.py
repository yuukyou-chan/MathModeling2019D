import csv

x = []
y = []
with open('合并.csv') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])

for i in range(234717):
    if x[i][3] is not None:
        y.append(x[i])
print(y)

