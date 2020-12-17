from pandas import read_csv
# 显示数据的前10行
filename='H:\MachineLearning-master\chapter06\pima_data.csv'
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
data=read_csv(filename,names=names)
peek=data.head(10)
print(peek)
print(data.shape)
print(data.dtypes)