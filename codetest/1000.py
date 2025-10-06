from functools import reduce

result = reduce(lambda a, b: a + b, list(map(int, input().split())))
print(result)  # 15


