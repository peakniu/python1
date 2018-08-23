import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
radar_labels = np.array(['useyears', 'purchaseprice', 'actualvalue'])  # 雷达标签,极角标签
nAttr = 3

#每一个横向量对应一个雷达标签，如[3.10, 4.64, 2.94]对应三类客户的useyears

data = np.array([[3.10, 4.64, 2.94],
[11.26, 8.97, 13.47],
[8.55, 5.62, 10.41]])

data = np.array([[3.10, 2.94],
[11.26,13.47],
[8.55,10.41]])

data_labels = ('家自车', '无车损险', '有百万三者')  # 图例标签
data_labels = ('家自车', '有百万三者')  # 图例标签
angles = np.linspace(0, 2 * np.pi, nAttr, endpoint=False)  # 弧度

data = np.concatenate((data, [data[0]]))  # 闭合
angles = np.concatenate((angles, [angles[0]]))  # 闭合

fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
plt.plot(angles, data, 'o-', linewidth=1, alpha=0.2)  # 极坐标的 plot的angles必须是弧度值,否则数据会显示异常
plt.fill(angles, data, alpha=0.25)
plt.thetagrids(angles * 180 / np.pi, radar_labels)
plt.figtext(0.52, 0.95, '车险客户分析', ha='center', size=20)

legend = plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)
plt.setp(legend.get_texts(), fontsize='large')
plt.grid(True)
plt.savefig('leidatu_100.jpg')

plt.show()