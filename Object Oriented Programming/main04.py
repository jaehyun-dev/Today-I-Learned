class User:
    def say_hello(some_user):
        print("안녕하세요! 저는 {}입니다!".format(some_user.name))

    def login(some_user, my_email, my_password):    # 세 개의 파라미터를 받음
        # 로그인 메소드
        if (some_user.email == my_email and some_user.password == my_password):
        # 파라미터로 받은 이메일 주소와 비밀번호가 user 인스턴스의 이메일 주소, 비밀번호와 같은지 확인
            print("로그인 성공, 환영합니다")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")


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

User.say_hello(user1)
# 클래스 이름.메소드 이름(인스턴스) 대신
user1.say_hello()
# 인스턴스 이름.메소드 이름()으로도 메소드를 사용할 수 있음
# say_hello 메소드는 some_user라는 파라미터를 넘겨줘야 하는데, 파라미터를 넘겨주지 않았는데 에러가 안 남
# 왜 에러가 안 날까?
# 인스턴스 메소드의 특별한 규칙 때문
# 윗줄은 클래스에서 메소드를 호출했고, 아랫줄은 인스턴스에 메소드를 호출함
# 밑에처럼 인스턴스에 메소드를 호출하면 user1 인스턴스가 say_hello의 첫 번째 파라미터로 자동으로 전달됨
# 파라미터를 따로 써줄 필요가 없음
# 윗줄과 아랫줄은 다르게 생겼지만 완전히 똑같다고 생각하면 됨
# 여기에 파라미터 넣으면 어떻게 될까?

# user1.say_hello(user1)
# TypeError: User.say_hello() takes 1 positional argument but 2 were given
# say_hello는 파라미터를 1개만 받는데, 2개가 넘어왔다
# user1 인스턴스로 메소드를 호출했으니 자동으로 user1이 파라미터로 들어감
# 거기에 추가로 user1 또 넘겨준 것
# user1을 2번 넘겨주니 에러가 난 것
# User.say_hello(user1, user1) 과 똑같은 것

# login 메소드 추가 예시
# user1.login(user1, "captain@codeit.kr", "12345")
# user1.login("captain@codeit.kr", "12345")
# 두번째 줄이 맞는 코드
# user1 인스턴스로 메소드를 호출하기 때문에, user1 인스턴스가 자동으로 첫 번째 파라미터로 전달됨
# 그래서 첫 번째 파라미터를 빼고 나머지 파라미터들만 적어야 함