from pandas import read_csv
# 数据分类分布统计
filename='H:\MachineLearning-master\chapter06\pima_data.csv'
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
data=read_csv(filename,names=names)
print(data.groupby('class').size())