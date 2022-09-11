class User:
    count = 0

    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1


user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "abcdef")
user3 = User('서혜린', "lisa@codeit.kr", "123abc")

# line36 이후 추가 및 실행
user1.count = 5
# line50 이후 line18을 line 20으로 수정 후 실행
User.count = 5

print(User.count)

# 만약 클래스 이름 대신 인스턴스 이름을 쓰면 어떻게 될까?



print(user1.count)
print(user2.count)
print(user3.count)

# 3
# 3
# 3

# 클래스 변수의 값을 설정하는 것도 이렇게 할 수 있을까?
# line18 추가 및 실행

# 3
# 5
# 3
# 3

# user1의 count만 5로 출력, 나머지는 3으로 출력
# user.count = 5은 인스턴스 변수를 설정할 때 사용하던 문법
# 이렇게 쓰면 user1 인스턴스에 count라는 인스턴스 변수가 생기고, 그 값이 5로 설정됨
# 이 코드는 클래스 변수의 값을 설정하는 게 아니라, 같은 이름의 인스턴스 변수를 추가하는 것
# 같은 이름의 클래스 변수와 같은 이름의 인스턴스 변수가 있으면 인스턴스 변수가 읽어짐
# 그래서 user1.count는 클래스 변수 count가 아니라 user1의 인스턴스 변수 count를 나타내는 것
# 헷갈릴 수 있기에 클래스 변수에 값을 설정할 때는 클래스 이름으로만 해야 함

# line20 추가 후 실행

# 5
# 5
# 5
# 5

# 다 똑같이 5로 출력
# 클래스 변수가 잘 설정된 것

# 클래스 변수: 한 클래스의 모든 인스턴스가 공유하는 속성
# 클래스 변수의 값 읽는 법?
# 1. 클래스 이름.클래스 변수 이름
# 2. 인스턴스 이름. 클래스 변수 이름

# 클래스 변수의 값 설정하기?
# 1. 클래스 이름.클래스 변수 이름