# 실습과제
# 인스턴스를 생성할 때 필요한 정보들이 항상 우리가 원하는 형태로 존재할까요?
# 우리는 다양한 형태의 정보에서 필요한 부분을 뽑아내서 인스턴스를 생성할 수 있어야 합니다.
# 예를 들어 유저 인스턴스 생성에 필요한 정보가 문자열일 수도 있고 리스트일 수도 있습니다.
# 어떻게 각각의 형태에 대응할 수 있을까요?
# 아래와 같은 User 클래스가 있다고 해보죠.
#
# User 클래스
# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password
#
# 그리고 아래와 같이 서로 다른 형태의 정보를 갖고 유저 인스턴스를 만들어야 한다면?
# info_string = "강영훈,younghoon@codeit.kr,123456"
# info_list = ["이윤수", "yoonsoo@codeit.kr", "abcdef"]
#
# 1. 문자열은 쉼표(,)를 기준으로 분리하면 되겠고
# 2. 리스트는 각 인덱스의 요소를 가져오면 되겠죠?
# 아래 코드를 볼까요?
#
# 다양한 형태의 정보로 유저 인스턴스 만들기
# # 유저 인스턴스 만들기 (1): 문자열로 인스턴스 만들기
# parameter_list = info_string.split(",") # split 메소드를 사용해서 쉼표(,)를 기준으로 문자열을 리스트로 분리한다
#
# # 각 변수에 분리된 문자열 각각 저장
# younghoon_name = parameter_list[0]
# younghoon_email = parameter_list[1]
# younghoon_password = parameter_list[2]
#
# younghoon = User(younghoon_name, younghoon_email, younghoon_password)
#
# # 유저 인스턴스 만들기 (2): 리스트로 인스턴스 만들기
# yoonsoo_name = info_list[0]
# yoonsoo_email = info_list[1]
# yoonsoo_password = info_list[2]
#
# yoonsoo = User(yoonsoo_name, yoonsoo_email, yoonsoo_password)
#
# # 인스턴스가 제대로 생성되었는지 확인
# print(younghoon.name, younghoon.email, younghoon.password)
# print(yoonsoo.name, yoonsoo.email, yoonsoo.password)
#
# 실행 결과
# 강영훈 younghoon@codeit.kr 123456
# 이윤수 yoonsoo@codeit.kr abcdef
#
# 서로 다른 형태의 정보를 갖고도 User 인스턴스를 만들 수 있죠?
# 하지만 코드가 너무 깁니다.
# 이럴 때 User 클래스에 클래스 메소드를 두고 사용하면 훨씬 깔끔한 코드로 인스턴스를 생성할 수 있는데요.
# User 클래스의 클래스 메소드 from_string 과 from_list의 내용을 채워봅시다.




class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        # 코드를 쓰세요
        name, email, password = string_params.split(",")
        return cls(name, email, password)

    @classmethod
    def from_list(cls, list_params):
        # 코드를 쓰세요
        name, email, password = list_params[0], list_params[1], list_params[2]
        return cls(name, email, password)

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)



# 과제해설

# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password
#
#     @classmethod
#     def from_string(cls, string_params):
#         # 코드를 쓰세요
#
#     @classmethod
#     def from_list(cls, list_params):
#         # 코드를 쓰세요
#
# User 인스턴스를 생성할 수 있는 클래스 메소드
# 1. from_string 메소드와
# 2. from_list 메소드를 완성해봅시다.
#
#
# from_string 메소드
# 먼저 from_string 메소드를 완성합시다.
# 인스턴스 생성을 위해 필요한 정보가 쉼표(,)로 구분된 문자열 형태로 들어오는 경우에 어떻게 하면 될까요? 그럼
# 1. split 메소드로 문자열을 쉼표(,)를 기준으로 분리해서 리스트로 만들면 됩니다.
# 2. 그리고 이 리스트의 각 요소를 사용하면 됩니다.
# 아래 코드처럼요.
#
# @classmethod
# def from_string(cls, string_params):
#     # 각 변수에 분리된 문자열 저장
#     params_list = string_params.split(",")
#
#     name = params_list[0]
#     email = params_list[1]
#     password = params_list[2]
#
# 문자열을 분리해서 탄생한 리스트는 params_list라는 변수에 설정했습니다.
# 그리고 params_list 의 각 인덱스에 있는 요소들을 사용해서 인스턴스를 생성하면 되는데요. 어떻게 하면 될까요?
# 우리는 클래스 메소드의 첫번째 파라미터 cls로 User 클래스가 자동 전달된다고 배웠습니다. 그래서 다음 두 코드는 같은 코드입니다.
#
# User("강영훈", "younghoon@codeit.kr", "123456")
# cls("강영훈", "younghoon@codeit.kr", "123456")
#
# 그렇기 때문에 우리는 from_string 메소드에 파라미터로 넘어오는 cls를 사용해서 인스턴스를 생성하면 됩니다. 아래 코드의 맨 아랫줄처럼요.
#
#
# @classmethod
# def from_string(cls, string_params):
#     # 각 변수에 분리된 문자열 저장
#     params_list = string_params.split(",")
#
#     name = params_list[0]
#     email = params_list[1]
#     password = params_list[2]
#
#     # 인스턴스 생성 후 리턴
#     return cls(name, email, password)
#
# from_list 메소드
# User 인스턴스 생성에 필요한 정보가 리스트 형태로 존재하면 어떻게 할까요?
# 그럼 그냥 리스트의 각 인덱스에 있는 요소를 가져오면 됩니다.
# 인스턴스를 생성하는 부분은 from_string 메소드 때와 동일하게 적어주면 되구요.
#
# @classmethod
# def from_list(cls, list_params):
#     name = list_params[0]
#     email = list_params[1]
#     password = list_params[2]
#
#     # 인스턴스 생성 후 리턴
#     return cls(name, email, password)
#
#
# 테스트
# 클래스 메소드를 테스트 해보면,
#
# # 유저 생성 및 초기값 설정
# younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
# yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])
#
# print(younghoon.name, younghoon.email, younghoon.password)
# print(yoonsoo.name, yoonsoo.email, yoonsoo.password)
#
# 실행 결과
# 강영훈 younghoon@codeit.kr 123456
# 이윤수 yoonsoo@codeit.kr abcdef
#
# 잘 출력되네요, 이번 과제처럼 인스턴스를 생성하는 클래스 메소드를 클래스 속에 작성하는 것은 실제로 개발자들이 자주 사용하는 방식입니다.
# 깔끔한 코드로 인스턴스를 생성할 수 있는 방식이니까 기억해두세요.