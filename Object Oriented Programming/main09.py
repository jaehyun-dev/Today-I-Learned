# 실습과제
# 코드잇에서 강의를 듣고 인스타그램에 취직한 Jane은 User 클래스에 "팔로우" 기능을 추가하라는 지시를 받았습니다.
# 팔로우 기능은 크게 2개의 동작을 해야 합니다.
#
# 1. "내가 팔로우하는 사람" 목록에 그 사람을 추가하는 동작과
# 2. 상대방의 "나를 팔로우하는 사람" 목록에 나를 추가하는 동작
#
# 팔로우 기능은 follow 메소드로 구현하려고 하는데요.
# 팔로우 기능을 만드는 김에
#
# 1. follow 메소드 말고도
# 2. 유저가 팔로우하는 사람 수를 알려주는 num_following 메소드와
# 3. 유저를 팔로우하는 사람 수를 알려주는 num_followers 메소드도
#
# 추가해봅시다.
# User 클래스에 이 메소드들을 모두 추가하고 나서 코드를 실행하면 아래와 같은 실행 결과가 나와야 합니다.
#
# 실행 결과
# Young 2 2
# Yoonsoo 1 3
# Taeho 2 0
# Lisa 1 1

class User:
    # 인스턴스 변수 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
        self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트

    # 팔로우
    def follow(self, another_user):
        # 코드를 입력하세요
        self.following_list.append(another_user)
        another_user.followers_list.append(self)

    # 내가 몇 명을 팔로우하는지 리턴
    def num_following(self):
        # 코드를 입력하세요
        return len(self.following_list)

    # 나를 몇 명이 팔로우하는지 리턴
    def num_followers(self):
        # 코드를 입력하세요
        return len(self.followers_list)

# 유저들 생성
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 유저마다 서로 관심 있는 유저를 팔로우
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

# 유저 이름, 자신의 팔로워 수, 자신이 팔로우하는 사람 수를 출력합니다
print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())


# 과제 해설
# 주어진 코드는 다음과 같습니다.
#
#
# class User:
#     # 초깃값 설정
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password
#
#         self.following_list = []  # 이 유저가 팔로우하는 유저 리스트
#         self.followers_list = []  # 이 유저를 팔로우하는 유저 리스트
#
# follow 메소드
# # 팔로우
# def follow(self, another_user):
#     pass
#
# follow 메소드에서
#
# 1. self의 following_list에 another_user를 추가하고,
# 2. another_user의 followers_list에 self를 추가하면 됩니다.
#
# # 팔로우
# def follow(self, another_user):
#     self.following_list.append(another_user)
#     another_user.followers_list.append(self)
#
# follow 하는 수, follow 받는 수
# 이제 내가 팔로우하는 사람 수, 나를 팔로우하는 사람 수를 알려주는 메소드 2개를 완성해야 합니다. 각각
#
# 1. self.following_list의 길이와
# 2. self.followers_list의 길이를
#
# 리턴하면 됩니다.
# 먼저 num_following리스트는
#
# # 몇 명이 나를 팔로우하는지 리턴
# def num_following(self):
#     return len(self.following_list)
#
# 이렇게 following 리스트의 길이를 리턴해주면 됩니다.
# num_followers 메소드는 다음과 같겠죠.
#
# # 몇 명이 나를 팔로우하는지 리턴
# def num_followers(self):
#     return len(self.followers_list)
#
# 테스트를 해보면:
#
# # 유저들 생성
# user1 = User("Young", "young@codeit.kr", "123456")
# user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
# user3 = User("Taeho", "taeho@codeit.kr", "123abc")
# user4 = User("Lisa", "lisa@codeit.kr", "abc123")
#
# # 유저마다 서로 관심 있는 유저를 팔로우
# user1.follow(user2)
# user1.follow(user3)
# user2.follow(user1)
# user2.follow(user3)
# user2.follow(user4)
# user4.follow(user1)
#
# # 유저 이름, 자신의 팔로워 수, 자신이 팔로우하는 사람 수를 출력합니다
# print(user1.name, user1.num_followers(), user1.num_following())
# print(user2.name, user2.num_followers(), user2.num_following())
# print(user3.name, user3.num_followers(), user3.num_following())
# print(user4.name, user4.num_followers(), user4.num_following())
#
# 실행 결과
# Young 2 2
# Yoonsoo 1 3
# Taeho 2 0
# Lisa 1 1
#
# 잘 출력됩니다.