class User:
    pass


user1 = User()
user2 = User()
user3 = User()


# 인스턴스에 속성을 추가하는 방법은?
# 변수와 굉장히 비슷하다

# 변수 사용법
# name = "김대위"

# 인스턴스 변수 정의하기
# 인스턴스 이름.속성이름(인스턴스 변수) = "속성에 넣을 값"
user1.name = "김대위"
# user1 인스턴스에 name이라는 속성을 추가했고 속성값으로 문자열 "김대위"를 넣음
user1.email = "captain@codeit.kr"
user1.password = "12345"
# user1 인스턴스의 이메일 속성과 비밀번호 속성이 생긴 것
# user2, user3 인스턴스에도 마찬가지로 속성 추가해보자

user2.name = "강영훈"
user2.email = "younghoon@codeit.kr"
user2.password = "98765"

user3.name = "최지웅"
user3.email = "jiwoong@codeit.kr"
user3.password = "78945"

# 각 user 인스턴스는 같은 이름의 속성을 갖고 있어도 서로 다른 값을 갖고 있음
# user1, user2, user3가 속성을 공유하는 게 아니라 각자 개인적으로 갖고 있음
# 이렇게 인스턴스가 개인적으로 갖고 있는 속성을 인스턴스 변수라고 함
# name, email, password는 모두 인스턴스 변수

# 인스턴스 변수 사용하기
# 인스턴스 이름.인스턴스 변수 이름
print(user1.email)
print(user2.password)

# 추가하지 않은 인스턴스 변수를 사용하면 어떻게 될까?
# print(user1.age)
# AttributeError: 'User' object has no attribute 'age'
# age라는 인스턴스 변수를 정의한 적 없기 때문에 오류가 남
# 인스턴스 변수를 사용하려면 꼭 그 전에 미리 정의해놔야 함