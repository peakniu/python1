#将apriori算法产生的关联规则的最后一个kindcode提取出来，作为单独一列

from __future__ import print_function
import pandas as pd

inputfile = './tmp_company/apriori_car_kind.xls' #结果文件
outputfile = './tmp_company/apriori_car_kind_split.xls' #结果文件
data = pd.read_excel(inputfile, header = None)
print(data.iloc[1,0])

data1=data.iloc[1:,:]
#data2=pd.DataFrame(columns = ["k"]) #创建一个空的dataframe
data1['k']='1'#增加一列，初始化为1
print(len(data1))

data1.columns = ['r','s','c','k']#重命名列

#data1.iloc[0,3]=data1.iloc[0,3].replace('1','2')
#将k列置为r列分词后的最后一个kindcode
for i in range(len(data1)):
    #data2 = data2.append(data1.iloc[i,0].split('---')[0])
    data1.iloc[i,3]=data1.iloc[i,3].replace('1',data1.iloc[i,0].split('---')[len(data1.iloc[i,0].split('---'))-1])#逐行分词取最后个kindcode
    #print(data1.iloc[i,3])
print(data1)
data1.to_excel(outputfile) #保存结果


