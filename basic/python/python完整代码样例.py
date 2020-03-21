#!/usr/bin/env python
# coding: utf-8
# 注释版良性 恶性 乳腺癌肿瘤预测
# 导入pandas工具包，并且更名为pd
import pandas as pd

# 调用pandas工具包的read_csv函数/模块，传入训练文件地址参数，并获得返回的数据并且存置变量df_train;
df_train = pd.read_csv('../Datasets/Breast-Cancer/breast-cancer-train.csv')
df_test = pd.read_csv('../Datasets/Breast-Cancer/breast-cancer-test.csv')

# 选取'Clump Thickness', 'Cell Size' 作为特征，构建测试集中的正负分类样本。
df_test_negative = df_test.loc[df_test['Type'] == 0][['Clump Thickness', 'Cell Size']]
df_test_positive = df_test.loc[df_test['Type'] == 1][['Clump Thickness', 'Cell Size']]

# 导入matploitlib工具包中的pyplot并命名为plt
import matplotlib.pyplot as plt

# 绘制图1-2中的良性肿瘤样本点，标志为红色的o
plt.scatter(df_test_negative['Clump Thickness'],df_test_negative['Cell Size'], marker = 'o', s=200, c='red')
# 绘制图1-2 中的恶性肿瘤样本点，标志为黑色的x
plt.scatter(df_test_positive['Clump Thickness'],df_test_positive['Cell Size'], marker = 'x', s=150, c='black')
#绘制xy轴的说明
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
#展示图1-2
plt.show()


#导入numpy并命名为np
import numpy as np

#利用numpy中的random函数随机采样直线的微距和系数
intercept = np.random.random([1])
coef = np.random.random([2])

lx = np.arange(0, 12)
ly = (-intercept - lx * coef[0]) / coef[1]
#绘制一条随机直线
plt.plot(lx, ly, c='yellow')

#绘制图1-3
plt.scatter(df_test_negative['Clump Thickness'],df_test_negative['Cell Size'], marker = 'o', s=200, c='red')
plt.scatter(df_test_positive['Clump Thickness'],df_test_positive['Cell Size'], marker = 'x', s=150, c='black')
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
plt.show()



# 导入sklearn中的逻辑斯蒂回归分类器


from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

# 使用前失调训练样本学习直线的系数和截距
lr.fit(df_train[['Clump Thickness', 'Cell Size']][:10], df_train['Type'][:10])
print 'Testing accuracy (10 training samples):', lr.score(df_test[['Clump Thickness', 'Cell Size']], df_test['Type'])


# In[7]:


intercept = lr.intercept_
coef = lr.coef_[0, :]
# 原本这个分类面应该是lx * coef[1] +interface = 0。映射到二维平面上之后，应该是：
ly = (-intercept - lx * coef[0]) / coef[1]
# 绘制图1-4
plt.plot(lx, ly, c='green')
plt.scatter(df_test_negative['Clump Thickness'],df_test_negative['Cell Size'], marker = 'o', s=200, c='red')
plt.scatter(df_test_positive['Clump Thickness'],df_test_positive['Cell Size'], marker = 'x', s=150, c='black')
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
plt.show()



lr = LogisticRegression()
# 使用所有训练样本学习直线的系数和截距
lr.fit(df_train[['Clump Thickness', 'Cell Size']], df_train['Type'])
print 'Testing accuracy (all training samples):', lr.score(df_test[['Clump Thickness', 'Cell Size']], df_test['Type'])


#


intercept = lr.intercept_
coef = lr.coef_[0, :]
ly = (-intercept - lx * coef[0]) / coef[1]

#绘制图1-5
plt.plot(lx, ly, c='blue')
plt.scatter(df_test_negative['Clump Thickness'],df_test_negative['Cell Size'], marker = 'o', s=200, c='red')
plt.scatter(df_test_positive['Clump Thickness'],df_test_positive['Cell Size'], marker = 'x', s=150, c='black')
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
plt.show()
