class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        return "사용자: {}. 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    # 클래스 변수 count를 출력하는 메소드를 인스턴스 메소드가 아닌 클래스 메소드로 만들어볼 것
    @classmethod
    def number_of_users(cls):   # 클래스 메소드의 특별한 규칙: 첫 번째 파라미터의 이름은 꼭! cls로 쓰기
        print("총 유저 수는: {}입니다".format(cls.count))

user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "abcdef")
user3 = User('서혜린', "lisa@codeit.kr", "123abc")

# 클래스로 클래스 메소드 호출하기
User.number_of_users()

# 인스턴스로 클래스 메소드 호출하기
user1.number_of_users()

# 인스턴스 메소드 사용 vs 클래스 메소드 사용
# 인스턴스 메소드 사용
# User.say_hello(user1)
# user1.say_hello()
# 인스턴스를 통해서 인스턴스 메소드를 호출하면 인스턴스 자신이 첫 번째 파라미터로 자동 전달!

# 클래스 메소드 사용
# User.number_of_users()
# user1.number_of_users()
# 두 가지 방법 모두 첫 번째 파라미터로 클래스 자동 전달!
# 클래스가 자동 전달되는 이유는, classmethod 데코레이터로 nunmber_of_users를 클래스 메소드로 만들어줬기 때문