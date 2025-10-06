x = 6
y = 5

match x:
    case 0:
        print("Case A")
    case  1 | 2 | 3:
        print("Case B")
    case 4 if x < y:
        print("Case C")
    case _ if x > y:
        print("Case D")
    case _:
        print("Case E")

var = "1"
match var:
    case bool():
        print("불리언입니다.")
    case int(): #int가 bool보다 뒤에 있어야함 booldl int에포함
        print("정수입니다.")
    case float():
        print("실수입니다.")
    case str():
        print("문자열입니다.")
    case _:
        print("기타 자료형입니다.")


# my_list = []
my_list = ["apple"]
my_list = ["apple", "banana"]
# my_list = ["apple", "banana", "orange", "mango"]

match my_list:
    case []:
        print("빈 리스트")
    case [p]:
        print(f"한 요소: {p}")
    case [a, b]: #요소 갯수
        print(f"두 요소: {a}, {b}")
    case [a, *rest]: # 💡 이후 이터러블 배운 뒤 다시 살펴볼 것
        print(f"첫 요소: {a}, 나머지: {rest}")

# point = (0, 0)
# point = (2, 0)
# point = (0, 3)
point = (4, 5)
point = 1

match point:
    case (0, 0):
        print("원점")
    case (x, 0):
        print(f"X={x}")
    case (0, y):
        print(f"Y={y}")
    case (x, y):
        print(f"X={x}, Y={y})")
    case _:
        print("좌표가 아닙니다.")

my_dict = {}
my_dict = {"name": "홍길동", "age": 30}
my_dict = {"school": "엄석대", "major": "컴퓨터공학"}
# my_dict = {"job": "개발자", "position": "팀장", "years": "5"}

match my_dict:
    case {"name": name, "age": age}:
        print(f"인적 정보 - {name}({age})세")
    case {"school": school, "major": major}:
        print(f"학력 정보 - {school} 졸업 ({major} 전공)")
    case {"job": job, **rest}: # 이터러블 배운 뒤 다시 살펴볼 것
        print(f"직업 정보 - {job}")
    case {}:
        print("빈 딕셔너리")