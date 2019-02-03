n = int(input())

nums = input()
if(n == 1):
    print(nums)
    exit()
nums = nums.split(' ')
nums = list(map(int, nums))

counts = [0, 0, 0, 0, 0, 0]

for n in nums:
    counts[n - 1] += 1

max = -1
for i in range(len(nums)-1, -1, -1):
    if (counts[nums[i]-1] == 1):
        if(nums[i] > max):
            max = nums[i]

for i in range(len(nums)-1, -1, -1):
    if(nums[i] == max):
        print(i+1)
        exit()

print('none')
