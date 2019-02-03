even = int(input()) % 2 == 0

str1 = input()
str2 = input()

if(even and str1 == str2):
    print("Deletion succeeded")
    exit()
elif(even and str1 != str2):
    print("Deletion failed")
    exit()

for i in range(0, len(str1)):
    if(str1[i:i+1] == str2[i:i+1]):
        print("Deletion failed")
        exit()
print("Deletion succeeded")