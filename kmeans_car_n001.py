#-*- coding: utf-8 -*-
#使用K-Means算法聚类家自车投保商业险的保单中未投保车损险的保单,分析山东2017年家自车商业险保单
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors
import sklearn.datasets as ds
from sqlalchemy import create_engine

# 解决oracle中文乱码问题
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
outputfile = './tmp_company/apriori_car_kind.xls' #结果文件
#读200数据库，数据从分省库先导到200
engine = create_engine(
    'oracle+cx_oracle://sdclic:password@9.216.6.200:1521/SDORACLE')

data = pd.read_sql('SELECT * FROM nzz_test_kmeans ', engine)

del data['policyno'] #删除保单号，只剩车辆属性
'''数据初探
describe()函数自动计算的字段有count（非空值数）、unique（唯一值数）、top（频数最高者）、freq（最高频数）、mean（平均值）、std（方差）、min（最小值）、50%（中位数）、max（最大值）'''
explore = data.describe(percentiles = [], include = 'all').T
print(explore)
#对数据做删选，剔除小概率数据，提升聚类效果
data=data[(data['purchaseprice']<50)&(data['actualvalue']<50)]

k = 3 #聚类的类别
iteration = 1000 #聚类最大循环次数
data_zs = 1.0*(data - data.mean())/data.std() #数据标准化
print(data_zs)

from sklearn.cluster import KMeans
model = KMeans(n_clusters = k,max_iter = iteration) #分为k类，去掉并发
model.fit(data_zs) #开始聚类

#print(pd.Series(model.labels_))
#简单打印结果
r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
r = pd.concat([r2, r1], axis = 1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
r.columns = list(data.columns) + [u'类别数目'] #重命名表头
print(r)

#详细输出原始数据及其类别
r = pd.concat([data, pd.Series(model.labels_, index = data.index)], axis = 1)  #详细输出每个样本对应的类别
r.columns = list(data.columns) + [u'聚类类别'] #重命名表头
#r.to_excel(outputfile) #保存结果

print(r)
r0=r[r['聚类类别']==0]
r1=r[r['聚类类别']==1]
r2=r[r['聚类类别']==2]

print(r0)
print(r0['purchaseprice'])
'''
print(r0.iloc[:,0])
print(r0.iloc[:,1])
print(r0.iloc[:,2])
'''

#将聚类结果写入数据库

import os
from sqlalchemy import create_engine
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

engine = create_engine(
    'oracle+cx_oracle://sdclic:password@9.216.6.200:1521/SDORACLE')
r.to_sql('nzz_kmeans_car_n001', engine, index=0, if_exists='replace')#replace 删除整表重新插入  append 保留原数据，后续插入

#画概率密度图
def density_plot(data): #自定义作图函数
  import matplotlib.pyplot as plt
  plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
  plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
  p = data.plot(kind='kde', linewidth = 2, subplots = True, sharex = False)
  [p[i].set_ylabel(u'密度') for i in range(k)]
  plt.legend()
  return plt

pic_output = './tmp/pd_kmeans' #概率密度图文件名前缀
for i in range(k):
    plt.figure(num=i)
    density_plot(data[r[u'聚类类别']==i]).savefig(u'%s%s.png' %(pic_output, i)) #概率密度图

#画三维散点图，聚类可视化
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
#  将数据点分成三部分画，在颜色上有区分度
ax.scatter(r0.iloc[:,0], r0.iloc[:,1], r0.iloc[:,2], c='y')  # 绘制数据点
ax.scatter(r1.iloc[:,0], r1.iloc[:,1], r1.iloc[:,2], c='r')
ax.scatter(r2.iloc[:,0], r2.iloc[:,1], r2.iloc[:,2], c='g')

ax.set_zlabel('Z')  # 坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()

'''
#TENSE：提供一种有效地数据降维的方式，在2维或者3维展示聚类结果。
#-*- coding: utf-8 -*-
#接k_means.py
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

tsne = TSNE()
tsne.fit_transform(data_zs) #进行数据降维

tsne = pd.DataFrame(tsne.embedding_, index = data_zs.index) #转换数据格式
plt.figure(num=6)
#不同类别用不同颜色和样式绘图
d = tsne[r[u'聚类类别'] == 0]
print(d)
plt.plot(d[0], d[1], 'r.')
d = tsne[r[u'聚类类别'] == 1]
plt.plot(d[0], d[1], 'go')
d = tsne[r[u'聚类类别'] == 2]
plt.plot(d[0], d[1], 'b*')
plt.show()
'''



'''
data = np.random.randint(0, 255, size=[40, 40, 40])
x, y, z = data[0], data[1], data[2]
'''

