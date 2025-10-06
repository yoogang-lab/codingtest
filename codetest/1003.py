import sys

input = sys.stdin.readline
count = int(input())
oneCount = 0
zeroCount = 0

def fibonacci(n) :
    if n == 0 :
        # print(0)
        global zeroCount
        zeroCount += 1
        return 0
    elif n == 1 :
        # print(1)
        global oneCount
        oneCount += 1
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)

while count > 0 :
    num = int(input())
    fibonacci(num)
    print(zeroCount  ,  oneCount)
    oneCount = 0
    zeroCount = 0
    count -=1


