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

    # @classmethod
    # def number_of_users(cls):
    #     print("총 유저 수는: {}입니다".format(cls.count))

    def number_of_users(self):
        print("총 유저 수는: {}입니다.".format(User.count))

user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "abcdef")
user3 = User('서혜린', "lisa@codeit.kr", "123abc")

# 클래스 메소드 사용
# User.number_of_users()
# user1.number_of_users()

# 인스턴스 메소드 사용
User.number_of_users(user1)
user1.number_of_users()

# 처음에 왜 인스턴스 메소드가 아니라 클래스 메소드로 만든 걸까?
# number_of_users가 인스턴스 변수를 안 쓰기 때문
# number_of_users에서는 인스턴스 변수를 읽거나 설정하지 않기 때문
# number_of_users는 self 파라미터 사용하지 않음
# 인스턴스 변수 사용하지 않으니 self에 접근할 필요 없음
# 반면 클래스 변수 User.count는 사용하고 있음
# 인스턴스 변수 말고 클래스 변수만 사용하는 메소드라면 클래스 메소드로 작성해야 함

# 클래스 메소드를 사용할 때?
# 인스턴스 변수 사용: 인스턴스 메소드
# 클래스 변수 사용: 클래스 메소드

# 클래스 변수와 인스턴스 변수 둘 다 쓴다면?
# 인스턴스 메소드!
# 인스턴스 변수, 클래스 변수 모두 사용 가능!
# 인스턴스 변수는 self를 통해, 클래스 변수는 클래스 이름에 . 붙여 가져오면 됨
# 하지만 클래스 메소드는 인스턴스 변수를 가져올 수 없음
# 클래스가 자동 전달되는 cls를 통해 클래스 변수는 가져올 수 있지만 인스턴스 변수는 가져올 수 없음
# 인스턴스 변수, 클래스 변수 둘 다 필요할 때는 인스턴스 메소드를 사용해야 함

# 인스턴스 없이도 필요한 정보가 있다면?
# 클래스 메소드
# ex) User.count: 인스턴스가 하나도 없더라도 필요

# 클래스 메소드 사용하면 user 인스턴스 0개여도 User.count 출력 가능
# 인스턴스가 하나도 없을 때에도 사용할 가능성이 있으면 클래스 메소드로 만들어야 함