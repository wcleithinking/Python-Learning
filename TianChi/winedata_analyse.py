import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
 
# 颜色
color = sns.color_palette()
# 数据print精度
pd.set_option('precision',4) 
df = pd.read_csv('winequality/winequality-red.csv',sep = ';')
df.head(5)