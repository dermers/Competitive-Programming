t = int(input())

for i in range(0, t):
	d, m = [int(x) for x in input().split(' ')]
	spent = 0
	count = 0
	for n in [int(x) for x in input().split(' ')]:
		if n >= 13 and spent%7 == 0:
			count += 1
		spent += n

	print(count)
