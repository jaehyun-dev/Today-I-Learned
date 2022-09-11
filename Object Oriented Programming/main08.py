class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


user1 = User("Young", "young@codeit.kr", "123456")


user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")


user3 = User("Taeho", "taeho@codeit.kr", "123abc")


user4 = User("Lisa", "lisa@codeit.kr", "abc123")


print(user1.email)
print(user2.name)
print(user3.password)
print(user4.email)

# initialize 메소드를 쓰면 새 인스턴스 만들 때마다 코드 두 줄만 쓰면 됨
# user 인스턴스를 생성하는 줄 하나, 인스턴스 변수의 초기값을 설정하는 줄 하나
# 생성할 때마다 두 줄만 쓰면 되니 나쁘지 않기는 한데, 아예 한 줄로 줄이는 방법도 있음
# initialize를 __init__로 바꾸면 됨
# magic method 또는 special method(특수 메소드)라고 함
# 특정 상황에서 자동으로 호출되는 메소드

# 이닛 메소드는 인스턴스가 생성될 때 자동으로 호출
# initialize() 괄호 안의 파라미터들을 User() 괄호에 넣으면 됨


# user1 = User("Young", "young@codeit.kr", "123456")
# 1. User 인스턴스 생성
# 2. __init__메소드 자동 호출
#
#
# def __init__(self, name, email, password):
#     self.name = name
#     self.email = email
#     self.password = password
# 첫 번째 파라미터 self에는 방금 막 생성된 User 인스턴스가 들어감
# 그리고 괄호 안에 있는 값들이 순서대로 들어감
# 이닛 메소드는 인스턴스 변수돌의 초기값을 설정해줌

# 이닛 메소드를 사용하면 인스턴스 생성과 인스턴스 변수 초기값 설정을 한 줄에 할 수 있음
# 이런 장점 때문에 클래스에는 보통 이닛 메소드를 꼭 작성함