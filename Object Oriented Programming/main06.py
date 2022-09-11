class User:
    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def check_name(self, name):
        # 파라미터로 받는 name이 유저의 이름과 같은지 불린으로 리턴하는 메소드
        return self.name == name

user1 = User()
user2 = User()

user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

user2.name = "강영훈"
user2.email = "younghoon@codeit.kr"
user2.password = "98765"

# check_name 메소드의 역할은 인스턴스의 name과 파라미터로 받은 name이 같은지 확인
# 인스턴스 변수와 파라미터의 이름이 둘 다 name으로 같음
# 이래도 될까?
# 사실 이 코드는 아무런 문제가 없음
# name 하나는 함수 내에서 사용하는 값, 다른 하나는 self의 name
# 어떤 인스턴스가 갖고 있는 인스턴스 변수 name
# 그냥 name과 self.name은 구분이 확실하기 때문에 이렇게 작성해도 아무런 문제가 없음
# 심지어 이런 식으로 작성하는 게 꽤나 일반적이기도 함

print(user1.check_name("김대위"))
# 지금 user1 인스턴스가 메소드를 직접 호출하면 그 인스턴스가 첫 번째 파라미터로 넘어감
# 그래서 첫 번째 파라미터 self에는 인스턴스 user1이 들어감
# 두 번째 파라미터로는 문자열 "김대위"가 들어감
# self.name도 문자열 "김대위", 파라미터 name도 문자열 "김대위"
# 불린값 True가 return됨

print(user1.check_name("강영훈"))
# user1의 name은 "김대위"인데 파라미터 name은 "강영훈"이기 때문에 False 출력