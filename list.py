# 리스트 초기화
my_list = [10, 20, 30, 40, 50, 60]

empty_list = []

list_type = str(type(my_list))
list_size = len(my_list)

print(list_size)
print(list_type)


# 단일 요소 접근
single_element = my_list[1]

print(single_element)


# 슬라이싱으로 부분 리스트 가져오기
sub_list = my_list[1:3]

print(sub_list)
# 음수 인덱스로 끝에서부터 요소에 접근
negative_index_element = my_list[-1]

print(negative_index_element)

# 단계별 슬라이싱
step_slicing_1 = my_list[::2] #처음부터 끝까지 : :
print(step_slicing_1)
step_slicing_2 = my_list[::3]
print(step_slicing_2)
step_slicing_3 = my_list[1::2]
print(step_slicing_3)

items_moved = my_list[:]
another_list = my_list
print(another_list)
# 리스트의 특정 요소 수정
my_list[0] = 15
my_list[2] = 35

# 리스트 정의
list_1 = [1, 2, 3]
list_1_b = [1, 2, 3]
list_2 = [4, 5, 6]

# + : 연결
combined_list = list_1 + list_2  # 123456

# * : 반복
repeated_list = list_1 * 2 #123123

# del : 항목 삭제
del combined_list[4] #12346

# 💡 == : 비교 ('내용이' 동일한지)
is_equal = list_1 == list_1_b #false

# 💡 is : 비교 (같은 리스트인지 : 메모리상 같은 위치인지)
is_same = list_1 is list_1_b

# != : 리스트 비교 (다른지)
is_not_equal = list_2 != [4, 5, 6] #

# in : 포함 여부
in_list_1_a = 3 in list_1
in_list_1_b = 4 in list_1
in_list_1_c = 4 not in list_1

# 리스트 초기화
# 💡 여러 자료형 포함 가능
exp_list = [1, 2.0,"a","a", "삼", [4, 5]] # 🔴 스텝오버하며 디버깅

# append: 리스트 끝에 항목 추가
exp_list.append(6)

# extend: 다른 리스트의 모든 항목을 추가
exp_list.extend([7, 8, 9])

# insert: 지정된 위치에 항목 삽입
exp_list.insert(1, 'a')

# remove: 리스트에서 항목 제거
exp_list.remove('a')

# pop: 리스트의 마지막 항목을 제거하고 그 항목을 반환
pop_result = exp_list.pop()

# clear: 리스트의 모든 항목 제거
exp_list.clear()

num_list = [1, 4, 2, 4, 3, 4, 5]

# index: 항목의 첫 위치 반환
index_result = num_list.index(3) # 없는 값일 시 오류

# count: 리스트에서 항목의 개수 반환
count_result = num_list.count(4)

pass

# sort: 리스트 정렬
# 💡 해당 리스트 자체를 정렬 : 이후 배울 sorted와 다름
num_list.sort()
sort_result = num_list

# reverse: 리스트 항목 순서를 역순으로 배치
# 역시 이후 배울 reversed와 다름
num_list.reverse() # ⭐️ sort_result의 내용 확인

# copy: 리스트 복사
copy_result = num_list.copy()

num_list.reverse() # ⭐️ 여기부터 sort_result와 copy_result의 내용 확인
num_list.append(6)
num_list.clear()

pass


# join : 문자열의 리스트를 하나의 문자로
str_list = ["a", "b", "c", "d", "efg"]

str_join = "".join(str_list)
str_join_w_sp = " ".join(str_list)
str_join_w_cm = ", ".join(str_list)

pass