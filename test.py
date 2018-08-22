# _*_ coding: utf-8 _*_
#! /usr/bin/python
'''
    Code from https://blog.csdn.net/qq_31629761/article/details/81079293
    阿里编程题——光明小学之完全图
    Modified by Wenchao Lei
'''
if __name__=='__main__':

    # get N and M
    n = int(input())
    m = int(input())
    #x = input()    # removed
    
    # get the map
    map = []
    for i in range(n):
        line = [int(x) for x in input().split()]
        map.append(list(line))

    # copy the map matrix into dp and last_dp
    # 一维列表深拷贝用list()
    # 二维列表深拷贝用[list(x) for x in dp]
    # 三维列表深拷贝用[[list(i) for i in x] for x in dp]
    dp = [list(i_row) for i_row in map]   
    last_dp = [list(i_row) for i_row in dp]
    # compute the dp matrix
    for k in range(m - 1):     # 共循环m-1轮，每一次循环后的dp矩阵元素代表i和j之间的长度为m的最短路径
        for i in range(n):
            for j in range(n):
                # the distance list of path: i-->x-->j, x!=i and x!=j
                tmp = [last_dp[i][x] + map[x][j] for x in range(n) if x != i and x != j]
                # the minimum distance from i to j
                dp[i][j] = min(tmp)
        # copy the updated dp for the next iteration
        last_dp = [list(x) for x in dp]

    #print(dp)
    for i in range(n):
           print(dp[i])
