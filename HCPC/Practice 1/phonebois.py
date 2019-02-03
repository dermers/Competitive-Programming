n = int(input())

for i in range(0, n):
    p = int(input())
    good = True
    pn = []
    for j in range(0, p):
        c = input()
        for let in range(1, len(c)+1):
            #print(c+' ! '+c[0:let])
            if(c[0:let] in pn):
                print('NO')
                good = False
                break
        pn.append(c)
    pn.reverse()
    pn2 = []
    if(good):
        for j in range(0, p):
            c = pn[j]
            for let in range(1, len(c)+1):
                #print(c+' ! '+c[0:let])
                if(c[0:let] in pn2):
                    print('NO')
                    good = False
                    break
            pn2.append(c)
    if(good):
        print('YES')