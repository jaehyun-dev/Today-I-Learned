def print_hello():
    print('안녕하세요!')


def add_print_to(original):
    def wrapper():
        print('함수 시작')
        original()
        print('함수 끝')
    return wrapper

# add_print_to 함수는 파라미터로 또다른 함수를 받음
# add_print_to 함수 안에서 wrapper라는 또 다른 함수를 정의하고 있음
# 그리고 wrapper 함수를 return함
# 즉 파라미터로 어떤 함수를 받아서 또 다른 함수를 return

add_print_to(print_hello)
# line39 이후 괄호 추가
# add_print_to(print_hello)()

# add_print_to 함수를 호출하는데, 파라미터로 print_hello라는 다른 함수를 넘겨줌
# 그러면 파라미터 original로 print_hello가 들어가서 print_hello가 original이라는 새로운 이름을 갖게 됨
# add_print_to 함수 내에서는 original과 print_hello가 똑같은 함수
# wrapper 함수 정의하는데, "함수 시작"이라고 출력
# original 함수를 호출하는데, print_hello 함수를 호출하는 것과 같음
# 그리고 "함수 끝"이라고 출력
# original 함수를 호출함으로써 print_hello 함수를 호출했음
# 그리고 앞뒤로 다른 부가기능 추가
# 부가기능이 기존의 original(print_hello) 함수를 꾸며줌
# 즉 print_hello 함수를 데코레이팅 했다고 할 수 있음

# 실행하면 아무것도 출력되지 않음
# add_print_to 함수 호출
# 함수가 하는 일은 정의했던 wrapper 함수 return
# wrapper 함수 실행시키는 게 아니라, return 해주기만
# 따라서 아무것도 출력되지 않음
# return된 wrapper 함수는 호출한 부분에 그대로 들어감
# 즉, add_print_to(print_hello) == wrapper
# return된 함수를 호출하려면 괄호를 열고 닫아야 함

# 더 깔끔하게 쓰는 방법
print_hello = add_print_to(print_hello)
# add_print_to 함수가 새로운 함수 wrapper를 호출함
# return된 함수를 다시 print_hello에 넣고
print_hello()
# print_hello 호출

# 정리
# add_print_to 함수를 정의
# 이 함수가 하는 일은, 파라미터로 어떤 함수를 받아서 데코레이팅, 꾸며주는 것
# 앞뒤로 문자열을 출력하는 코드를 추가함
# 꾸며진 함수를 return 시켜줌
# add_print_to는 어떤 함수를 받고, 꾸며서, 새로운 함수를 return함
# 이 함수는 다른 함수를 꾸며주는 역할이기 때문에 add_print_to 함수를 데코레이터 함수라고 부름