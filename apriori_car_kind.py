#-*- coding: utf-8 -*-
#使用Apriori算法挖掘家自车险别关联规则
from __future__ import print_function
from sqlalchemy import create_engine
import pandas as pd
from apriori111 import * #导入自行编写的apriori函数，最后的排序由sort改为sort_values
# 解决oracle中文乱码问题
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
outputfile = './tmp_company/apriori_car_kind.xls' #结果文件
#读200数据库，数据从分省库先导到200
engine = create_engine(
    'oracle+cx_oracle://sdclic:password@9.216.6.200:1521/SDORACLE')
df = pd.read_sql('SELECT * FROM nzz_test_apriori ', engine)
print(df)
data=df.fillna(0)#将空值置为0，得到0-1矩阵
print(data)
del data['policyno'] #删除保单号，只剩kindcode
support = 0.01 #最小支持度
confidence = 0.2 #最小置信度
ms = '---' #连接符，默认'--'，用来区分不同元素，如A--B。需要保证原始表格中不含有该字符

result=find_rule(data, support, confidence, ms)
result1=result[result['confidence']<0.99]
result1.to_excel(outputfile) #保存结果
print(result1)





