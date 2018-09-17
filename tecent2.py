import math

def getnum(x,scorelist):
    count = 0
    rem = x - int(scorelist[0])
    if rem >0:
        count += 1
        count += getnum(rem,scorelist[1:])
    else:
        if rem == 0:
            count += 1
        else:   
            count += getnum(x,scorelist[1:])
    return count
            
x,y = input().split(' ')
x = int(x)
y = int(y)
all = x + y
n = math.floor(math.sqrt(all*2))
if (all != n*(n+1)/2):
    print(-1)
else:
    scorelist = list(reversed([i+1 for i in range(n)]))
    print(getnum(x,scorelist))
