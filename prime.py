
from math import sqrt
import numpy as np
N = 10**7
arr=np.arange(N)
file = open('prime.txt','w')
lst=[]
for i in range(2, N+1):
    for j in lst:
        if j > int((sqrt(i)) + 1):
            lst.append(i)
        if i % j == 0:
            break
    else:
        lst.append(arr[i])
        file.write(str(arr[i])+' ')
file.close()