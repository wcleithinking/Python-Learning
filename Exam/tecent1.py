def getsub(A,k):
    results = []
    for i_start in range(len(A)-k+1):
        if A[i_start:i_start+k] not in results:
            results.append(A[i_start:i_start+k])
    return results

def getsubnum(B,Asub):
    count = 0
    for i in range(len(B)-1):
        if B[i:i+len(Asub)] == Asub:
            count += 1
    return count

k = int(input(''))
A = input('')
B = input('')
#Asub = getsub(A,k)
count = 0
results = []
for i_start in range(len(A)-k+1):
    if A[i_start:i_start+k] not in results:
        Asub = A[i_start:i_start+k]
        count += getsubnum(B,Asub)
        results.append(Asub)    
print(count)
