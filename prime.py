def eratosthenes(n):    
    sieve = list(range(n + 1))
    sieve[1] = 0    
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve

sieve = eratosthenes(10**7)
f=open("prime.txt","w")
for i in range (2,10**7):
	if(sieve[i]!=0):
		f.write(str(sieve[i]))
		f.write("\n")