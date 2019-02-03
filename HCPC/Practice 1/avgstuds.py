n = int(input())
for i in range(0, n):
    nums = [int(x) for x in input().split()]
    c = nums[0]
    nums = nums[1:]
    sum = 0
    for e in nums:
        sum += e
    avg = sum / c
    s = 0
    for e in nums:
        if e > avg:
            s += 1
    print(str(round((s / c)*100, 3)) + '%')