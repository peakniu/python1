#-*- coding: utf-8 -*-
#画预估保费提升图
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
N =3
menMeans = (132,757,391)
menStd = (1, 1, 1)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars



fig, ax = plt.subplots()

rects1 = ax.bar(ind, menMeans, width, color='r')

# add some text for labels, title and axes ticks
ax.set_ylabel('提升保费')
ax.set_title('预估保费提升值(万元)')
ax.set_xticks(ind )
plt.xticks(rotation=0)
ax.set_xticklabels(('车身划痕->玻璃破碎','自燃->盗抢','驾驶人->乘客'))
#ax.legend((rects1[0]), ('保费提升值'))
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)

plt.show()


