# for i in range(5):
#     print(f"기본 사용 :")
#
# for i in range(2, 6):
#     print(f"기본 사용", {i})
# # 증가폭 지정: 0부터 10까지 2씩 증가하며 숫자 반복
# for i in range(0, 11, 2):
#     # i는 0부터 시작하여 2씩 증가하며 10까지 이동
#     print(f"증가폭 지정: {i}")
# # 감소하는 범위: 5부터 1까지 역순으로 숫자 반복
# for i in range(5, 0, -1):
#     # i는 5부터 시작하여 1씩 감소하며 1까지 이동
#     print(f"감소하는 범위: {i}")
#
# # 딕셔너리 키 순회
# person = {"이름": "홍길동", "나이": 30, "키": 179.9}
# for key in person:
#     print(f"{key}: {person[key]}")
#
# # 튜플과 셋에서도 사용 가능
#
# my_tuple = (1, 2, 3, 4, 5)
# for item in my_tuple:
#     print(item)
#
# my_set = {1, 2, 3, 4, 5}
# listed = list(my_set)
# for item in my_set:
#     print(item)

my_list = ["ABC", (1, 2, 3), {4, 5}, {6: 7, 8: 9}]

for sublist in my_list:
    for item in sublist:
        print(item)