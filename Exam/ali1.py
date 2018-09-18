# _*_ coding: utf-8 _*_
#! /usr/bin/python2

# get N and M
N = int(raw_input())
M = int(raw_input())
dim = raw_input()    # need to be removed

# get the map
map = []
for i in range(N):
    current_row = list([int(d) for d in raw_input().split()])
    map.append(current_row)

# copy the map matrix into d_matrix_now and d_matrix_old
# 一维列表深拷贝用list()
# 二维列表深拷贝用[list(x) for x in d_matrix_now]
# 三维列表深拷贝用[[list(i) for i in x] for x in d_matrix_now]
d_matrix_now = [list(row) for row in map]
d_matrix_old = [list(row) for row in map]
# compute the d_matrix_now matrix
for k in range(M - 1):     # 共循环m-1轮，每一次循环后的dp矩阵元素代表i和j之间的长度为m的最短路径
    for i in range(N):
        for j in range(N):
            # the distance list of path: i-->x-->j, x!=i and x!=j
            temp = [d_matrix_old[i][l] + map[l][j]
                    for l in range(N) if l != i and l != j]
            # the minimum distance from i to j
            d_matrix_now[i][j] = min(temp)
    # copy the updated d_matrix_now for the next iteration
    d_matrix_old = [list(row) for row in d_matrix_now]

#print d_matrix_now
for i in range(N):
    for j in range(N):
        if j < N-1:
            print d_matrix_now[i][j],
        else:
            print d_matrix_now[i][j]