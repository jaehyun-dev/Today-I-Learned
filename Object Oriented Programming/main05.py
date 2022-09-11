class User:
    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def login(self, my_email, my_password):    # 세 개의 파라미터를 받음
        # 로그인 메소드
        if (self.email == my_email and self.password == my_password):
        # 파라미터로 받은 이메일 주소와 비밀번호가 user 인스턴스의 이메일 주소, 비밀번호와 같은지 확인
            print("로그인 성공, 환영합니다")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")


user1 = User()

user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

# user1.login(user1, "captain@codeit.kr", "12345")
user1.login("captain@codeit.kr", "12345")

# 인스턴스 메소드의 특별한 규칙
# 인스턴스 메소드를 호출하면, 이 인스턴스가 메소드의 첫 번째 파라미터로 자동 전달됨
# 인스턴스 메소드를 정의할 때는 항상 첫 번째 파라미터로 인스턴스를 받기 위한 파라미터를 써줘야 함
# 기존에는 some_user라고 썼지만, 앞으로는 self라고 쓸 것
# 파이썬에서는 인스턴스 메소드의 첫 번째 파라미터 이름을 self로 쓸 것을 권장
# 인스턴스 메소드로 호출하는 인스턴스 자신이 첫 번째 파라미터로 들어가기 때문에 self라는 단어가 어울림
# 인스턴스 메소드의 주인공은 첫 번째 파라미터로 들어오는 인스턴스
# 첫 번째 파라미터를 self로 써주면 주인공이 항상 self라는 것을 알기 떄문에 훨씬 읽기 편한 코드가 됨
# 사실 self 말고 다른 단어를 써도 실행에는 아무런 문제가 없음
# 하지만 이건 파이썬 세계의 약속
# 인스턴스 메소드의 특별한 규칙
# 첫 번째 파라미터의 이름은 꼭! self로 쓰기