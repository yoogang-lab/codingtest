import sys

# 빠른 입력
input = sys.stdin.readline
n = int(input())
# data = list(map(int, input().split()))
stacklist = []

def checkEmpty (list) :
    return len(list) == 0

def inputCommand (command, inputting) :
    match command:
        case "push":
            stacklist.append(inputting)
        case "pop":
            print (-1 if  checkEmpty(stacklist) else stacklist.pop())

        case "size":
            print(len(stacklist))
        case "empty":
            print( 1  if checkEmpty(stacklist) else 0)
        case "top":
            print( -1 if checkEmpty(stacklist) else stacklist[len(stacklist)-1])

while n > 0:
    inputData = input().split()
    # print(inputData)

    input_command = inputData[0]
    input_num = -1
    if len(inputData) > 1:
        input_num = int(inputData[1])  # Convert to integer
    inputCommand(input_command, input_num)
    n -=1


#
# top = 0
#
# stacklist.append(1)
# top +=1
#
# stacklist.append(4)
# top +=1
#
# print("pop ", stacklist.pop())
# print("pop ", stacklist.pop())
# print("isEmpty ",isEmpty(stacklist))
# top -=1

# print(data)

# 빠른 출력
# sys.stdout.write("결과 출력\n")