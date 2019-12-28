import numpy as np
import math
N=10**7
A=np.arange(N)

for i in range(math.ceil(N/2)):
    j=i+2
    if (A[j]!=0):
        while j<N-i-2:
            A[j+i+2]=0
            j+=i+2
file = open('prime.txt', 'w')
A[1]=0
for i in range(N):
    if A[i]!=0:
        file.write(str(A[i])+' ')
file.close()
