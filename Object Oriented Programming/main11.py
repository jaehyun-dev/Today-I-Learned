class User:
    count = 0

    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드
        self.name = name
        self.email = email
        self.pw = pw

        # line20 후에 추가
        User.count += 1

# 클래스 변수는 클래스 이름 밑에 쓰면 됨
# User.count = 1
# print(User.count)
# line 11 추가 후 삭제

# 클래스 변수 count가 유저 인스턴스 개수를 정확히 나타내도록 하려면?
# user 인스턴스가 생성될 때마다 실행되는 것은 __init__ 메소드
# 이닛 메소드에서 count의 값을 올려주면 됨

user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "abcdef")
user3 = User('서혜린', "lisa@codeit.kr", "123abc")

print(User.count)