iterable_list = [1, 2, 3]
iterable_tuple = (4, 5, 6)
iterable_string = "abc"

# iterable_list.sort()
# iterable_list.reverse()


# 이터레이터(iterator)를 만드는 방법
# iterator_list = iter(iterable_list)
# iterator_tuple = iter(iterable_tuple)
# iterator_string = iter(iterable_string)
#
# lst_val_0 = next(iterator_list)
# tpl_val_0 = next(iterator_tuple)
# str_val_0 = next(iterator_string)
#
# lst_val_1 = next(iterator_list)
# tpl_val_1 = next(iterator_tuple)
# str_val_1 = next(iterator_string)

def simple_generator():
    yield 1
    yield 2
    yield 3


# 제너레이터 함수 사용
gen = simple_generator()
gen_type = type(gen).__name__

def counter_generator(start, end) :
    current = start
    while current <= end :
        yield current
        current += 1
for number in counter_generator(1, 5) :
    print(number)

    #sorted(_iterator_)
    #reversed(_iterator_)

add = lambda x, y : x + y
print(add(3,5))

# 리스트 정렬 시 키로 사용
numbers = [(1, 2), (3, 1), (5, 0)]
sorted_numbers = sorted(numbers, key=lambda x: x[1])
print(sorted_numbers)  # 출력: [(5, 0), (3, 1), (1, 2)]


pass