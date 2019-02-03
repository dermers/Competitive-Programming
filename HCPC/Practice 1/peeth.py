from fractions import Fraction
from math import log
n = abs(int(input()))
while(n!=0):
    ans = 1
    for i in range (2, int(log(n, 2))+1):
        fn = Fraction(n)
        den = '1/' + str(i)
        x = Fraction(den)
        temp = fn**x
        if temp % 1 == 0 and i > ans:
            ans = i
    print(int(ans))
    n = abs(int(input()))
