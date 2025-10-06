import sys

input = sys.stdin.readline
count = int(input())

fiboArr0 = [0] * 41
fiboArr1 = [0] * 41

def fibonacci0(n) :
    if n == 0 :
        # print(0)
        return 1
    elif n == 1 :
        # print(1)
        return 0
    else :
        if fiboArr0[n] == 0 :
            fiboArr0[n] = fibonacci0(n - 1) + fibonacci0(n - 2)
    return fiboArr0[n]

def fibonacci1(n) :
    if n == 0:
        # print(0)
        return 0
    elif n == 1:
        # print(1)
        return 1
    else:
        if fiboArr1[n] == 0:
            fiboArr1[n] = fibonacci1(n - 1) + fibonacci1(n - 2)
    return fiboArr1[n]

while count > 0 :
    num = int(input())
    fiboArr0 = [0] * 41
    fiboArr1 = [0] * 41
    zeroCount = fibonacci0(num)
    oneCount =  fibonacci1(num)
    print(zeroCount  ,  oneCount)
    oneCount = 0
    zeroCount = 0
    count -=1


