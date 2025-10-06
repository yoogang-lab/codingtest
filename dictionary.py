# 딕셔너리 생성 및 초기화
from list import another_list

my_dict = {"name": "Alice", "age": 25, "city": "New York", "job": "designer"}

# 요소 추가 및 수정
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

for key in keys:
    print(key)

keys_list = list(keys)
values_list = list(values)
items_list = list(items)

my_dict_copy = my_dict.copy()

another_dict = {3.14: "PI", ("흥부", "놀부") : "brothers"}
my_dict.update(another_dict)
print(another_dict[("흥부", "놀부")])

my_dict.clear()

pass