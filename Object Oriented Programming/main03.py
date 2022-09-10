class User:
    def say_hello(some_user):
    # 이 메소드는 some_user라는 파라미터를 받는데, some_user에는 user1 등 인스턴스를 넣어주면 됨
        # 인사 메세지 출력 메소드
        print("안녕하세요! 저는 {}입니다!".format(some_user.name))
        # 만약 user1을 파라미터로 넘기면, some_user 부분이 user1으로 바뀐다고 생각하면 됨
        # user1 인스턴스 변수 name은 김대위
        # 따라서 "안녕하세요! 저는 김대위입니다!" 출력

    # say_hello 메소드는 name이라는 인스턴스 변수를 사용
    # 따라서 say_hello는 "인스턴스 메소드"라고 할 수 있음


user1 = User()
user2 = User()
user3 = User()

user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

user2.name = "강영훈"
user2.email = "younghoon@codeit.kr"
user2.password = "98765"

user3.name = "최지웅"
user3.email = "jiwoong@codeit.kr"
user3.password = "78945"

# 클래스.인스턴스 메소드(파라미터)
User.say_hello(user1)
User.say_hello(user2)
User.say_hello(user3)