#！/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy

file_train = open("TianChi/data/weibo/weibo_train_data.txt", "r")

data_train = []
for line in file_train:
    data_train.append(line.strip().split('\t'))


for i in range(10):
    print(int(data_train[i][0],16), end="\t")
    print(int(data_train[i][1],16), end="\t")
    print(data_train[i][2], end="\t")
    print(int(data_train[i][3]), end="\t")
    print(int(data_train[i][4]), end="\t")
    print(int(data_train[i][5]), end="\n")