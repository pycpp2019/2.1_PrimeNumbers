from math import sqrt
def func(n):
    lst = []
    for i in range(3, n+1, 2):
        if (i > 10) and (i%10==5):
            continue
        for j in lst:
            if j > int((sqrt(i)) + 1):
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst
my_lst = func(10000000)
my_string = ', '.join(str(e) for e in my_lst)
f = open('prime.txt', 'w')
f.write(my_string)
f.close()
