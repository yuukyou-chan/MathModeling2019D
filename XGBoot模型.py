# 导入包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb

# 导入数据
from xgboost import plot_importance

data = pd.read_excel('合并.xls')
data.head()

# 切分数据集
feas = data.columns

feas_var = feas[0:11]  # 输入变量
feas_lab = feas[12]  # 输出变量

X = data[feas_var]
Y = data[feas_lab]

from sklearn.model_selection import train_test_split

x_train, x_valid, y_train, y_valid = train_test_split(X, Y, test_size=0.3, random_state=90)

# 训练模型
xgb_model = xgb.XGBRegressor(n_estimators=1000, random_state=50, verbosity=1, max_depth=15, min_child_weight=4, gamma=0.6)

xgb_model.fit(x_train, y_train, eval_metric='mae', eval_set=[(x_valid, y_valid)], early_stopping_rounds=100)

# 模型评价
from sklearn.metrics import mean_absolute_error, mean_squared_error, accuracy_score

xgb_pred = xgb_model.predict(x_valid)
print(np.corrcoef(xgb_pred, y_valid)[0, 1] ** 2)    # 相关系数
print(mean_squared_error(xgb_pred, y_valid))        #均方误差
print(mean_absolute_error(xgb_pred, y_valid))       #平均绝对误差

# 准确率
# accuracy = accuracy_score(y_valid,xgb_pred)
# print('accuarcy:%.2f%%'%(accuracy*100))

# 显示重要特征
plot_importance(xgb_model)
plt.show()