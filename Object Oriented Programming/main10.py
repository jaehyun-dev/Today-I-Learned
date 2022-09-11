class User:
    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드
        self.name = name
        self.email = email
        self.pw = pw

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    # line29 이후 추가
    # def __str__(self):
    #     return "사용자: {}, 이메일: {}, 비밀번호 ******".format(self.name, self.email)

user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "1q2w3e4r")

# User 클래스로 user1, user2 인스턴스 2개를 만듦

print(user1)
print(user2)


# <__main__.User object at 0x00000265F289BD90>
# <__main__.User object at 0x00000265F289AB90>

# 인스턴스가 어떤 클래스인지, 그리고 그 인스턴스가 저장돼있는 메모리 주소가 나옴
# 인스턴스를 출력할 때마다 정보가 이렇게만 나오면 큰 의미가 없음
# 우리가 원하는 내용이 출력되면 훨씬 좋음

# line12, line13 추가 후 실행

# 사용자: 강영훈, 이메일: younghoon@codeit.kr, 비밀번호 ******
# 사용자: 이윤수, 이메일: yoonsoo@codeit.kr, 비밀번호 ******