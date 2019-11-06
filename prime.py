import numpy as np

N = 10**7 

file = open('prime.txt', 'w')

arr = np.zeros(N)
lim = N**0.5

j = 2
while (j <= lim):
    i = 2
    while (j*i < len(arr)):
        arr[j*i] = 1
        i += 1
    j += 1

for i in range(2,N):
    if (arr[i] == 0):
       file.write(str(i)+' ')
file.close()