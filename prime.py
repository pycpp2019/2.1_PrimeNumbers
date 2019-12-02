n = 10000000
file = open("prime.txt", 'w')
list = [2]
for i in range(3, n + 1, 2):
	if (i > 10) and (i % 10 == 5):
		continue
	for j in list:
		if j * j - 1 > i:
			list.append(i)
			break
		if (i % j == 0):
			break
	else:
		list.append(i)
file.write(' '.join(map(str, list)))