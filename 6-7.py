from pandas import read_csv
# 计算数据的高斯偏离
filename='H:\MachineLearning-master\chapter06\pima_data.csv'
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
data=read_csv(filename,names=names)
print(data.skew())