mutable_object = [1, 2, 3]
immutable_object = (1, 2, 3)

mutable_object[0] = 4
print(mutable_object)    # [4, 2, 3]
# 리스트 인스턴스는 생성되고 나서도 그 속성을 바꿀 수 있음

# immutable_object[0] = 4
# print(immutable_object)
##     immutable_object[0] = 4
## TypeError: 'tuple' object does not support item assignment

# 튜플은 불변 타입. 한 번 인스턴스 생성하면 그 이후로는 속성을 바꿀 수 없음.
# 불변 타입 객체 속성을 바꿀 수 없지만 변수가 가리키는 객체 자체는 바꿀 수 있음.


tuple_x = (6, 4)
# tuple_x[0] = 4
# tuple_x[1] = 1
# print(tuple_x)

##     tuple_x[0] = 4
## TypeError: 'tuple' object does not support item assignment

# 오류남.

tuple_x = (6, 4)
tuple_x = (4, 1)
tuple_x = (4, 1, 7)

print(tuple_x)    # (4, 1, 7) 잘 출력됨.


# 같은 변수로 속성이 다른 튜플을 사용하고 싶으면, 기존 튜플의 속성을 바꾸는 게 아니라 새로운 튜플 인스턴스를 생성하고 변수가 새로운 인스턴스를 가리키게 하면 됨



list_x = []
list_x.append(4)
list_x.append(1)
list_x.append(7)

print(list_x)    # [4, 1, 7]

# 가변: list, dict
# 불변: bool, int, float, str, tuple

# 직접 작성하는 클래스는 가변 타입
# 인스턴스 변경 시 원래 인스턴스 속성을 바꾸면 됨