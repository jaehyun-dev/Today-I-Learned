# @add_print_to # line21 후 추가
def print_hello():
    print('안녕하세요!')


def add_print_to(original):
    def wrapper():
        print('함수 시작')
        original()
        print('함수 끝')
    return wrapper


print_hello = add_print_to(print_hello) # line24후 삭제
print_hello()

# add_print_to 함수는 데코레이터 함수
# print_hello 함수를 꾸미기 위해서 add_print_to 함수가 print_hello 함수를 꾸며주고, print_hello가 꾸며진 함수를 다시 가리키도록
# line14 쓰지 않고도 print_hello 함수를 꾸밀 수 있음

# line1 ~ line3과 line6 ~ line11 위치 바꾼 뒤 line1 추가
# @add_print_to: print_hello 함수를 add_print_to로 꾸며주라는 뜻
# 이걸 쓰고 나서 앞으로 print_hello 함수를 호출하면 꾸며진 print_hello 함수가 호출됨
# 그러면 line14가 필요 없어짐

# 데코레이터는 어떤 쓸모가 있을까?

def function1():
    기존 함수 1 내용

def function2():
    기존 함수 2 내용

def function3():
    기존 함수 3 내용


# 아까처럼 함수가 실행되기 전과 후에 문자열을 출력하고 싶다고 가정
# 그럼 모든 함수의 기존 함수 내용 위 아래에 똑같은 기능을 추가해야 함

def function1():
    print('함수 시작')
    기존 함수 1 내용
    print('함수 끝')

def function2():
    print('함수 시작')
    기존 함수 2 내용
    print('함수 끝')

def function3():
    print('함수 시작')
    기존 함수 3 내용
    print('함수 끝')

# 일일이 하니 중복도 많고 귀찮음
# 이럴 때 데코레이터를 쓰면 훨씬 깔끔하게 할 수 있음

def add_print_to(original):
    def wrapepr():
        print('함수 시작')
        original()
        print('함수 끝')
    return wrapper

@add_print_to
def function1():
    기존 함수 1 내용

@add_print_to
def function2():
    기존 함수 2 내용

@add_print_to
def function3():
    기존 함수 3 내용

# 중복되는 부분을 모두 데코레이터 함수에 넣고, @ 붙여서 데코레이터 써줘서 코드 예쁘게 바꿀 수 있음

# 이후에도 꾸미고 싶은 함수가 있으면 그대로 @add_print_to 쓰면 됨

@add_print_to
def function4():
    기존 함수 4 내용

@add_print_to
def fucntion5():
    기존 함수 5 내용

# 객체지향 프로그래밍 배우면서 데코레이터 자주 사용
# 함수 위에 @ 보이면 데코레이터라고 생각하면 됨
# 함수를 어떤 함수로 꾸며서 새로운 기능을 준다, 기존의 함수에 새로운 기능 추가한다고 생각하면 됨