# программа выводит в файл 'prime.txt' все  простые числа до 10**7
import numpy as np

def simple_num(num, list):
    ''' функция проверяет являетс число простым 
    на вход число и список всех предшествующих простых чисел тип целые
    на выходе         True - да,       False - нет
    '''
    if list.size == 0 :
        return True
    list2 = num % list
    m = min(list2)
    return bool(m)
    
def main(N):
    '''функция сторит список из всех простых чисел меньших N и выводит их в файл 'prime.txt'
    '''
    list = np.array([])    #список всех предыдущих простых чисел
    n = 2
    file = open('prime.txt', 'w')
    while (n <= N):
        if simple_num(n, list):
            file.write(str(n) +'\n')
            list = np.append(list,[n])
        n += 1
    file.close()

main(10**7)
