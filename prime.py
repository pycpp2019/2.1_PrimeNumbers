from math import sqrt
N = 10000000
prime = [2, 3]
file = open ('prime.txt', 'w')
file.write(str('2 3 '))
def func():
    for i in range(5, N, 2):
        for j in prime:
            if j > int(sqrt(i) + 1):
                prime.append(i)
                file.write(str(prime[len(prime) - 1]) + ' ')
                break
            if (i % j == 0):
                break
        else:
            prime.append(i)
            file.write(str(prime[len(prime) - 1]) + ' ')
file.close
func()