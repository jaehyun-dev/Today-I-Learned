class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))


user1 = User("Young", "young@codeit.kr", "123456")


print(type(user1))
# <class '__main__.User'>
# user1 인스턴스는 '__main__.User' 클래스의 인스턴스이다.
# __main__ 표시는 지금 실행되고 있는 파일을 나타냄
# 지금 실행되고 있는 main03_02.py 파일에 정의돼있는 User 클래스라는 뜻

print(type(2))          # <class 'int'>
print(type("string"))   # <class 'str'>
print(type([]))         # <class 'list'>
print(type({}))         # <class 'dict'>
print(type(()))         # <class 'tuple'>

def print_hello():
    print("안녕하세요!")

print(type(print_hello))    # <class 'function'>

# 모두 다 어떤 클래스의 인스턴스
# 파이썬을 만든 개발자들이 미리 클래스로 만들어놓음
# 자주 사용할 것 같으니 가져다 쓰라고 만들어둠

# 1     # int 클래스로 만든 1을 나타내는 인스턴스가 생성됨
# ""    # 문자열 클래스로 만든 빈 문자열을 나타내는 인스턴스가 생성됨
# def function_1():     # function 클래스의 인스턴스가 생성됨

int_list = []

int_list.append(1)
int_list.append(3)
int_list.append(7)

print(int_list)
# [1, 3, 7]
# 파이썬을 만든 개발자들이 list 클래스에 append 메소드를 미리 정해놨기 때문에 우리가 가져다가 사용할 수 있다.
# 방금 본 기본 도구들 말고도 파이썬에 있는 모든 것들은 특정 클래스의 인스턴스로 생성된다.
# 파이썬 코드를 조금이라도 쓰게 되면 우리도 모르는 사이에 객체를 생성하고 객체 지향 프로그래밍을 하고 있는 것.
# 이것이 바로 파이썬을 순수 객체 지향 언어라고 부르는 이유.