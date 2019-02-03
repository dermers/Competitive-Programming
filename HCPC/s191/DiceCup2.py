inp = [int(i) for i in input().split(" ")]

n = inp[0]
m = inp[1]

rolls = [0]*(n+m+1)
for x in range(1, n):
	for y in range(1, m):
		rolls[x+y] = rolls[x+y]+1

mx = max(rolls)
for i in range(0, n+m+1):
	if(rolls[i]==mx):
		print(i+1)