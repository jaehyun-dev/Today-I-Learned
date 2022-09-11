# 실습과제
#
# 인스턴스 변수는 항상 사용하기 전에 미리 설정해야 합니다.
# User 클래스의 인스턴스를 4개 만들고 각 인스턴스에 인스턴스 변수를 설정해봅시다.
#
#
# class User:
#     pass
#
#
# user1 = User()
# user1.name = "Young"
# user1.email = "young@codeit.kr"
# user1.password = "123456"
#
# user2 = User()
# user2.name = "Yoonsoo"
# user2.email = "yoonsoo@codeit.kr"
# user2.password = "abcdef"
#
# user3 = User()
# user3.name = "Taeho"
# user3.email = "taeho@codeit.kr"
# user3.password = "123abc"
#
# user4 = User()
# user4.name = "Lisa"
# user4.email = "lisa@codeit.kr"
# user4.password = "abc123"
#
#
# print(user1.name, user1.email, user1.password)
# print(user2.name, user2.email, user2.password)
# print(user3.name, user3.email, user3.password)
# print(user4.name, user4.email, user4.password)
#
#
# 위 코드를 실행하면 아래와 같이 출력됩니다.
#
# 실행 결과
# Young young@codeit.kr 123456
# Yoonsoo yoonsoo@codeit.kr abcdef
# Taeho taeho@codeit.kr 123abc
# Lisa lisa@codeit.kr abc123
#
#
# 그런데 지금 코드의 길이가 너무 긴데요.
# 지금처럼 인스턴스 변수를 하나씩 설정하지 않고 인스턴스 변수 전부를 한번에 설정할 수 있는 인스턴스 메소드를 User 클래스에 정의해봅시다.
# initialize라는 이름으로 인스턴스 메소드를 작성해보세요.


class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password




user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
User.initialize(user3, "Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
User.initialize(user4, "Lisa", "lisa@codeit.kr", "abc123")



print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)



# 과제 해설
# 과제에서 initialize 메소드를 호출하는 코드를 보면 user1과 user2는 인스턴스를 통해서 인스턴스 메소드를 호출하고 있습니다.
# 다음 코드처럼 initialize 메소드를 호출하면
# user1.initialize("Young", "young@codeit.kr", "123456")
# User 클래스의 initialize 메소드가 실행되고, 첫 번째 파라미터인 self로 인스턴스 user1이 자동으로 넘어갑니다.
# 그래서 initialize 메소드를 호출할 때 user1 인스턴스를 직접 넘겨주지 않아도 됩니다.
# 위 코드처럼 쓰면 "Young", "young@codeit.kr", "123456"이 self 다음에 정의된 2, 3, 4번째 파라미터로 넘어갑니다.
#
# user1, user2와 달리 user3와 user4는 클래스를 통해서 인스턴스 메소드를 호출하고 있습니다.
# User.initialize(user3, "Taeho", "taeho@codeit.kr", "123abc")
# 이 코드처럼 클래스를 통해 인스턴스 메소드를 호출할 경우 첫 번째 파라미터로 인스턴스가 자동으로 전달되지 않기 때문에 user3 인스턴스를 첫 번째 파라미터로 직접 넘겨줘야 합니다.
# 이 코드를 호출하면 initialize 메소드가 호출되고, 첫 번째 파라미터로 메소드의 호출 대상인 user3 인스턴스, 그리고 "Taeho", "taeho@codeit.kr", "123abc" 이 각각 그 다음 파라미터로 넘어갑니다.
#
# 인스턴스 메소드를
# - 인스턴스로 호출하는 방법과
# - 클래스로 호출하는 방법
# 사이에 어떤 차이가 있는지 알겠죠?
# 그러니까 아래 코드 2줄은 같은 동작을 2가지 방법으로 작성한 겁니다.
# 그 의미는 같구요.
#
# user1.initialize("Young", "young@codeit.kr", "123456")
# User.initialize(user1, "Young", "young@codeit.kr", "123456")
#
# 메소드의 헤더(header) 부분
# 자, 이제 initialize 메소드를 정의해봅시다.
# initialize 메소드에는 파라미터 4개를 정의해야 합니다.
# 첫번째로 메소드를 호출하는 인스턴스가 자동 전달되는 self를 적고 그 다음에는 순서대로 나머지 파라미터들인 name, email, password를 적어야 합니다.
# 그러니까 initialize 메소드의 헤더 부분은 이렇게 쓰면 됩니다.
#
# class User:
#     def initialize(self, name, email, password):
#
# 메소드의 바디(body) 부분
# initialize 메소드의 헤더 부분을 완성했으니 이제 바디 부분을 완성해볼까요?
# 바디 부분에서는 파라미터 self를 갖고 인스턴스 변수를 설정하면 됩니다.
# 바로 이 self로 user1같은 인스턴스들이 넘어오는 거니까 user1 인스턴스의 경우에 self.name=name은 user1.name=name과 같은 뜻이 되는 겁니다.
#
# class User:
#     def initialize(self, name, email, password):
#         self.name = name
#
# 같은 방식으로 '이메일'과 '비밀번호'에 해당하는 인스턴스 변수도 설정해봅시다.
#
# class User:
#     def initialize(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password
#
# 이렇게 하면 모든 인스턴스 변수를 initialize 메소드로 한번에 설정할 수 있겠죠?
# 드디어 initialize 메소드를 모두 완성했습니다.
#
# User 클래스를 사용하는 코드를 다시 실행해보면
#
# # 샘플 유저 생성
# user1 = User()
# user1.initialize("Young", "young@codeit.kr", "123456")
#
# user2 = User()
# user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
#
# user3 = User()
# user3.initialize("Taeho", "taeho@codeit.kr", "123abc")
#
# user4 = User()
# user4.initialize("Lisa", "lisa@codeit.kr", "abc123")
#
# # 유저 정보 출력
# print(user1.name, user1.email, user1.password)
# print(user2.name, user2.email, user2.password)
# print(user3.name, user3.email, user3.password)
# print(user4.name, user4.email, user4.password)
#
# 실행 결과
# Young young@codeit.kr 123456
# Yoonsoo yoonsoo@codeit.kr abcdef
# Taeho taeho@codeit.kr 123abc
# Lisa lisa@codeit.kr abc123
#
# initialize 메소드로 설정한 인스턴스 변수들의 값이 잘 출력됩니다.
# 이런 식으로 인스턴스 변수들을 메소드 하나로 한번에 설정하면 코드의 길이도 줄고, 인스턴스 변수를 한 눈에 파악할 수 있어서 좋습니다.