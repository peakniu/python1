#-*- coding: utf-8 -*-
#画投保比例概率提升对比图
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
N = 6
menMeans = (6,20,29,25,20,35)
menStd = (1, 1, 1, 1, 1,1)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
#rects1 = ax.bar(ind, menMeans, width, color='b', yerr=menStd)
rects1 = ax.bar(ind, menMeans, width, color='b')
womenMeans = (58,67,82,37,29,44)
womenStd = (1,1,1,1,1,1)
#rects2 = ax.bar(ind + width, womenMeans, width, color='y', yerr=womenStd)
rects2 = ax.bar(ind + width, womenMeans, width, color='y')
# add some text for labels, title and axes ticks
ax.set_ylabel('百分比')
ax.set_title('概率和置信度')
ax.set_xticks(ind + width)
plt.xticks(rotation=0)
ax.set_xticklabels(('车身划痕->玻璃破碎','自燃->盗抢','驾驶人->乘客', '玻璃破碎->百万三者','车损->盗抢', '车损->驾驶人'))
ax.legend((rects1[0], rects2[0]), ('概率', '置信度'))
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()


'''
#二维线图plot
plt.figure(num=1)
x=np.linspace(0,2*np.pi,50)
y=np.sin(x)
plt.plot(x,y,'bp--')
#plt.show()

#饼图pie
plt.figure(num=2)
labels='Frogs','Hogs','Dogs','Logs'#定义标签
sizes=[15,30,45,10] #每一块的比例
colors=['yellowgreen','gold','lightskyblue','lightcoral'] #每一块的颜色
explode=(0,0.1,0,0) #突出显示第二块（'Hogs'）
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal') #显示为圆（避免比例压缩为椭圆）
#plt.show()

#直方图hist
plt.figure(num=3)
x=np.random.randn(1000)
plt.hist(x,10)
plt.show()
'''



