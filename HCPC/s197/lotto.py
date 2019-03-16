import itertools

nums = [int(x) for x in input().split(' ')]
while nums[0] != 0:
	nums = nums[1:]
	ans = []
	for e in set(itertools.combinations(nums, 6)):
		ans.append(str(e).replace(",","")[1:-1])
	ans.sort()
	for e in ans:
		print(e)
	nums = [int(x) for x in input().split(' ')]
	if nums[0] != 0:
		print()
