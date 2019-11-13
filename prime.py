def isPrime (val):
	num = 2
	limit = val ** 0.5

	while num <= limit:
		if val % num:
			num += 1
		else:
			return False
	return True


file = open('prime.txt', 'w')

cur_num = 2

while cur_num < 10 ** 7:
	if isPrime(cur_num):
		file.write(str(cur_num) + '\n')
	cur_num += 1