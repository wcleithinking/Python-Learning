n,m,k = raw_input().split(' ')
n = int(n)
m = int(m)
k = int(k)
list = []
for i in range(n):
    for j in range(m):
        list.append((i+1)*(j+1))

list.sort()
print(list[k-1])