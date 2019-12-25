# прогамма выводит в файл 'prime.txt' все  простые числа до 10**

def simple_num(num, list):
	''' функция проверяет являетс число простым 
	на вход число и список всех предшествующих простых чисел тип целые
	на выходе 		1 - да,		0 - нет
	'''
	for x in list:
		if (num % x == 0):
			return 0
	return 1
	
def main(N):
	'''функция сторит список из всех простых чисел меньших N и выводит их в файл 'prime.txt'
	'''
	list = [] #list of pervious simple numbers
	n = 2
	file = open('prime.txt', 'w')
	while (n <= N):
		if simple_num(n, list):
			file.write(str(n) +'\n')
			list = list + [n]
		n += 1
	file.close()

main(10**7)
