n = int(input().split()[0])
nums = [int(x) for x in input().split()]
nums.append(0)
nums.append(n)
nums.sort(reverse=True)
#print(nums)
ans = set()
for i in range(0, len(nums)):
    for j in range(i, len(nums)):
        if(abs(nums[i]-nums[j]) != 0):
            ans.add(abs(nums[i]-nums[j]))
sorted(nums)

s = ''
for e in ans:
    s += str(e) + ' '

print(s[0:len(s)-1])