n = int(input())
nums = sorted([int(x) for x in input().split()])

sequence = 1
for i in range(1, n + 1):
    if i < n and nums[i - 1] == nums[i] - 1:
        sequence += 1
    else:
        if sequence > 2:
            print(str(nums[i - sequence]) + '-' + str(nums[i - 1]), end=(" " if i < n else "\n"))
        else:
            for j in range(sequence):
                print(nums[i - sequence + j], end=(" " if i < n else "\n"))
        sequence = 1