#n = int(input("n="))
n=10**7
prime = set(range(1,n+1))
for i in range(2,n+1):
    for j in range(i**2, n+1, i):
            prime.discard(j)
#print (prime)
f = open('prime.txt', 'w')
for index in prime:
    f.write(str(index) + '\n')
f.close()