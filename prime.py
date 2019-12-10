from math import sqrt
import numpy as np
N = 10000000
arr=np.arange(N)
lst=[2]
for i in range(3, N+1, 2):
    if (i > 10) and (i%10 == 5):
        continue
    for j in lst:
        if j > int((sqrt(i)) + 1):
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(arr[i])
with open("prime.txt", "w") as file:
    print(*lst, file=file)        
file.close()