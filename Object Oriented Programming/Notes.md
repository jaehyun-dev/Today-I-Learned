22.09.08 20:24  

# 객체 지향 프로그래밍이란?

## 1 객체 지향 프로그래밍 시작하기

### 01. 객체란?
객체 지향 프로그래밍을 이해하기 위해서는 우선 객체가 무엇인지 알아야 함  
객체: 속성, 행동으로 이루어진 존재  
우리가 살아가면서 보는 모든 존재를 객체라고 생각하면 됨  
예를 들어 자동차에는 색깔이라는 속성, 의자 갯수라는 속성, 차의 높이 등의 속성이 있다  
또한 자동차에는 시동이 걸리는 행동, 악셀을 밟으면 앞으로 나아가는 행동 등이 있다  
이런 식으로 자동차에는 속성과 행동이 있기 때문에 자동차를 객체로 볼 수 있다  
또 다른 예시로 instagram과 같은 SNS의 유저들이 있다  
SNS 유저는 속성으로 이메일주소, 비밀번호, 친구목록 등이 있다  
그리고 행동으로 게시물에 좋아요 누르기, 친구 추가하기 등의 행동이 있다  
SNS 유저는 실제 물리적으로는 존재하지 않지만 속성과 행동이 있기 때문에 객체라고 볼 수 있다  
따라서 거의 모든 게 객체가 될 수 있다  
현실에 존재하든, 가상에 존재하든, 추상적 개념이든 상관없이 속성과 행동을 떠올릴 수 있다면 모두 객체  
  
### 02. 객체 지향 프로그래밍이란?
객체 지향 프로그래밍이란  
프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 접근법이다.  
프로그램을 객체들과 객체들 간의 소통으로 바라보는 것!  
객체 지향 프로그래밍을 이용해서 총게임 만든다고 가정  
먼저 총게임에 어떤 객체들이 필요할지 생각해야 함  
일단 게임 캐릭터 객체, 총 객체, 총알 객체 등 있어야 함  
다른 객체도 많겠지만 일단 여기까지 생각한다면  
각 객체에 어떤 속성과 행동이 있어야 하는지 생각해야 함  
- 게임 캐릭터 객체
  - 속성: 접속할 때 사용하는 아이디, 현재 사용 중인 총, 체력, 목숨 등  
  - 행동: 현재 사용 중인 총을 발사한다, 달린다, 체력이 0 이하가 되면 죽는다 등  
- 총 객체
  - 속성: 모델명, 무게, 장전된 총알 갯수 등  
  - 행동: 총알을 발사한다  
- 총알 객체
  - 속성: 공격력  
  - 행동: 총알을 맞은 캐릭터의 체력을 공격력만큼 깎는다 등  

각 객체는 어떻게 소통할까?  
게임 캐릭터 객체가 총 객체에게 발사하라고 신호를 보냄  
총 객체는 장전된 총알 중 하나를 발사함  
대신 이 때 자신의 속성 중 장전된 총알 갯수에서 1을 빼야 함  
총알이 발사되어 다른 게임 캐릭터 객체에 닿으면 이 총알은 그 객체에게 체력을 깎으라는 신호를 보냄  
총알의 신호를 받은 게임 캐릭터 객체는 총알의 공격력만큼 자신의 체력을 깎음  
이때 깎고난 후의 체력이 0 이하라면 죽어야 함  
만약 죽으면 목숨 수에서 1을 빼야 함  
  
이러한 식으로 게임을 만들었으면, "프로그램을 객체지향적으로 설계했다, 모델링(modeling)했다"고 표현  
객체 지향 프로그래밍으로 프로그램을 만들려면  
1. 프로그램에 어떤 객체들이 필요할지 정한다  
2. 객체들의 속성과 행동을 정한다
3. 객체들이 서로 어떻게 소통할지 정한다  
  
22.09.09 23:36  
## 2 객체를 만드는 법

### 01. 클래스와 인스턴스
인스타그램과 같은 SNS를 만들려고 한다고 가정  
User를 나타내는 객체를 어떻게 만들 수 있을까?  
User 객체는 어떤 속성과 행동을 가질까?  
- 속성
  - 이름
  - 이메일 주소
  - 비밀번호
  - 팔로우 목록
  - 팔로워 목록
- 행동
  - 자기소개하기
  - 팔로우하기

모든 User 객체는 위의 속성과 행동을 가지고 있음  
User 객체의 틀을 정했다고 할 수 있음  
User 객체를 만들 떄 이 틀을 기반으로 만들면 됨  
  
또다른 예시  
붕어빵 모양의 틀에 반죽을 붓고 구우면 붕어빵이 만들어짐  
사람들이 더 주문하면 요리사는 같은 틀로 붕어빵을 또 만들면 됨  
붕어빵 틀 하나로 붕어빵을 계속 만들 수 있음  
마찬가지로, 객체의 틀이 있으면 틀을 이용해 객체를 계속 만들 수 있음  
  
파이썬에서는 객체의 틀을 클래스라고 하고, 틀로 만든 결과물을 객체라고 함  
클래스가 있으면 객체를 계속 만들 수 있음  
클래스로 객체(인스턴스)를 만든다  
객체와 인스턴스는 굳이 따지면 조금 다르기는 하지만 큰 차이 없어 같은 의미임  
클래스로 여러 객체, 혹은 여러 인스턴스를 만들 수 있음  
  
[main01.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main01.py) 참고
  
22.09.10 22:43  
### 02. 인스턴스 변수
main01.py에서는 User 클래스로 인스턴스를 3개 만듦  
그런데 User 클래스에는 아무 내용도 없음  
속성과 행동을 나타내는 부분 없다는 뜻  
인스턴스에 속성을 추가하는 방법은?  
변수와 굉장히 비슷하다  
  
#### 인스턴스 변수 정의하기  
인스턴스 이름.속성이름(인스턴스 변수) = "속성에 넣을 값"  
인스턴스가 개인적으로 갖고 있는 속성을 **인스턴스 변수**라고 함  
  
#### 인스턴스 변수 사용하기
인스턴스 이름.인스턴스 변수 이름  
인스턴스 변수를 사용하려면 꼭 그 전에 미리 정의해놔야 함

[main02.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main02.py) 참고 
  
### 03. 인스턴스 메소드  
객체는 속성과 행동으로 이루어져있음  
파이썬에서는 속성을 인스턴스 변수로 나타냄  
변수로 속성을 나타내는 것  
파이썬에서 행동은 어떻게 나타낼까?  
행동은 함수로 나타냄  
클래스 안에 함수를 정의하면 객체의 행동을 정의한 것  
이렇게 객체의 행동을 나타내는 함수를 **메소드**라고 부름  
클래스 안에 함수를 정의하면 메소드를 정의했다고 할 수 있음  
 
#### 메소드의 종류
1. 인스턴스 메소드
2. 클래스 메소드
3. 정적 메소드

#### 인스턴스 메소드
인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드  

#### 인스턴스 메소드 사용하기
클래스 이름.메소드 이름(인스턴스)
  
[main03.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main03.py) 참고
  
### 04. 인스턴스 메소드의 특별한 규칙
인스턴스 메소드를 사용하는 또다른 방법이 있음  
인스턴스 이름.메소드 이름()  
인스턴스로 메소드를 호출할 경우, 인스턴스가 첫 번째 파라미터로 전달됨  

[main04.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main04.py) 참고
  
22.09.11 20:03
### 05. self를 사용합시다
#### 인스턴스 메소드의 특별한 규칙
첫 번째 파라미터의 이름은 꼭! **self**로 쓰기  
  
[main05.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main05.py) 참고  
  
### 06. 인스턴스 변수와 같은 이름을 갖는 파라미터
인스턴스 변수와 파라미터의 이름이 같아도 상관없음  
심지어 이런 식으로 작성하는 게 꽤나 일반적이기도 함  
  
[main06.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main06py) 참고  
  
### 07. initialize 메소드
인스턴스 변수를 하나하나 작성하면 코드가 너무 길어짐  
클래스에 initialize 메소드를 만들어 간단하게 할 수 있음  
  
[main07.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main07.py) 참고  
  
### 08. __init__ 메소드
#### special method, magic method(특수 메소드)
앞뒤로 __(underbar 2개) 붙어있으면 특수 메소드  
특정 상황에서 자동으로 호출되는 메소드  
#### __init__ 메소드
인스턴스가 생성될 때 자동으로 호출  
  
__init__ 메소드를 쓰면 인스턴스 생성과 동시에 인스턴스 변수 초기값 설정을 한 줄에 할 수 있음  
이러한 장점으로 클래스에는 보통 이닛 메소드를 꼭 작성함  
  
[main08.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main08.py) 참고  
  
### 09. #맞팔해요
  
[main09.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main09.py) 참고  
  
### 10. __str__ 메소드
메소드 이름 양옆에 underbar 두 개가 있는 특수 메소드  
"double underscore", 줄여서 **dunder** 메소드라고 부르기도 함  
dunder str 메소드라고 부름  
특수 메소드는 특정 상황에 자동으로 호출되는 메소드  
dunder str 메소드는 print 함수를 호출할 때 자동으로 부름  
어떤 인스턴스를 출력하면 dunder str 메소드의 return 값이 출력됨  
인스턴스를 출력할 때 우리가 원하는 정보를 나오게 하려면 클래스에 __str__ 메소드를 정의하면 됨  
  
[main10.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main10.py) 참고  
  
### 11. 클래스 변수 I
인스턴스 자신만의 속성을 나타내는 인스턴스 변수  
여러 인스턴스들이 공유하는 속성은?
  
SNS User 클래스의 user 인스턴스의 총 갯수를 나타내는 속성을 만들고 싶음  
이 속성은 특정 인스턴스가 갖고 있는 값이 아니라 서로 공유하는 값  
어떤 user 인스턴스라도 똑같은 값을 가지고 있어야 함  
파이썬에서는 이러한 속성을 **클래스 변수**라는 것으로 나타냄  
클래스 변수는 같은 클래스의 인스턴스들이 공유하는 값  
  
[main11.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main11.py) 참고  
  
### 12. 클래스 변수 II
#### 클래스 변수의 값을 읽는 법
1. 클래스 이름.클래스 변수 이름
2. 인스턴스 이름.클래스 변수 이름

#### 클래스 변수의 값 설정하는 법
1. 클래스 이름.클래스 변수 이름
  
[main12.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main12.py) 참고  
  
### 13. 여기서 잠깐! 데코레이터 I
#### 데코레이터(decorator)
파이썬에서 어떤 함수를 꾸며서 새로운 함수를 만들 때 사용하는 방법  

[main13.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main13.py) 참고

22.09.13 23:21  
### 14. 여기서 잠깐! 데코레이터 II
@ 붙여서 데코레이터 함수 이용하여 새로운 기능을 줄 수 있음  

[main14.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main14.py) 참고

22.09.14 23:46
### 15. 클래스 메소드 I
인스턴스 메소드: 인스턴스 변수의 값을 읽거나 설정하는 메소드  
클래스 메소드: 클래스 변수의 값을 읽거나 설정하는 메소드

#### 클래스 메소드의 특별한 규칙
클래스 메소드의 첫 번째 파라미터의 이름은 꼭! cls로 쓰기

#### 클래스 안의 함수를 클래스 메소드로 만드는 방법
classmethod 데코레이터로 함수를 데코레이팅 해주기

[main15.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main15.py) 참고

### 16. 클래스 메소드 II
인스턴스 변수를 사용하면 인스턴스 메소드를, 클래스 변수를 사용하면 클래스 메소드를 사용  
클래스 변수만 사용하는 메소드라면 클래스 메소드로 작성해야 함  
클래스 변수와 인스턴스 변수를 모두 사용하면 인스턴스 메소드 사용해야 함  
인스턴스 메소드는 인스턴스 변수와 클래스 변수를 모두 사용 가능한 반면, 클래스 메소드는 인스턴스 변수를 가져올 수 없기 때문  
인스턴스가 없을 때에도 필요하거나 사용할 가능성이 있으면 클래스 메소드로 만들어야 함  

[main16.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main16.py) 참고

### 17. 클래스 메소드 활용

[main17.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main17.py) 참고

### 18. 정적 메소드
이때까지
- 인스턴스 메소드
- 클래스 메소드

를 배웠습니다. 메소드의 종류는 총 3가지라고 했죠? 아직 하나가 더 남았습니다.

바로 **정적 메소드**(static method)입니다. 정적 메소드는 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드입니다.  
아래 코드를 볼까요?
```python
class User:
    count = 0
    
    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw
    
        User.count += 1
    
    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))
    
    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)
    
    @classmethod
    def number_of_users(cls):
        print("총 유저 수는: {}입니다".format(cls.count))
    
    @staticmethod
    def is_valid_email(email_address):
        return "@" in email_address
```
지금 User 클래스에서 is_valid_email 메소드가 정적 메소드입니다. 정적 메소드는 메소드 정의 위에  @staticmethod 데코레이터를 표시해야 합니다. is_valid_email 메소드는 파라미터 email_address로 받은 문자열에  @가 들어있는지 체크합니다.

정적 메소드는
- 인스턴스 메소드의 self
- 클래스 메소드의 cls

같은 자동 전달되는 파라미터가 없습니다.

그리고 정적 메소드는 아래 코드처럼 인스턴스, 클래스 두 가지 모두를 통해 사용 가능합니다.  
```python
print(User.is_valid_email("taehosung"))
print(User.is_valid_email("taehosung@codeit.kr"))
    
print(user1.is_valid_email("taehosung"))
print(user1.is_valid_email("taehosung@codeit.kr"))
```
```python
False
True
False
True
```

#### 정적 메소드는 언제 사용할까요?
```python
# 인스턴스 메소드
def __str__(self):
    return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

# 클래스 메소드    
@classmethod
def number_of_users(cls):
    print("총 유저 수는: {}입니다".format(cls.count))

# 정적 메소드    
@staticmethod
def is_valid_email(email_address):
    return "@" in email_address
```
User 클래스에는 인스턴스 메소드, 클래스 메소드, 정적 메소드가 있습니다.
1. 인스턴스 메소드 __str__는 인스턴스 변수인 self.name, self.email을 사용하고,
2. 클래스 메소드 number_of_user는 클래스 변수인 cls.count를 사용합니다.
3. 하지만 is_valid_email 메소드에선 아무 변수도 사용하고 있지 않네요.

인스턴스 변수나 클래스 변수 중 아무것도 사용하지 않을 메소드라면 정적 메소드로 만들면 됩니다. 그러니까 어떤 속성을 다루지 않고, 단지 기능(행동)적인 역할만 하는 메소드를 정의할 때 정적 메소드로 정의하면 됩니다. 이제 여러분은 메소드의 종류에는
- 인스턴스 메소드
- 클래스 메소드
- 정적 메소드

이 3가지가 있다는 것을 기억해주세요.  

Q. @staticmethod 안 쓰면?  
A. self인자가 파라미터 처음에 들어가게 되므로 인스턴스를 생성해주어야 사용이 가능함.  
반면 정적 메소드 데코레이터를 붙여주면 인스턴스를 생성하지 않아도 클래스 자체로 호출 및 사용 가능함.  

### 19. 객체를 만드는 법
질문 1  
다음 중 옳은 내용을 고르시오.  
(1) 인스턴스 변수는 __init__ 메소드에서 설정해주는 것이 좋다.  
(2) 클래스 변수는 인스턴스를 통해 접근해서 값을 바꾸면 된다.  
(3) 모든 인스턴스들이 같은 값을 공유해야하는 속성은 인스턴스 변수에 저장한다.  
(4) 모든 인스턴스 변수의 값이 같으면 둘은 같은 인스턴스이다.  
(5) 클래스 변수는 클래스를 통해서만 접근할 수 있다.  

질문 2  
다음 중 틀린 것을 고르시오.  
(1) 정적 메소드는 인스턴스 변수나 클래스 변수를 사용하지 않는다.  
(2) 인스턴스 메소드로 작성하는 모든 행동은 클래스 메소드로도 나타낼 수 있다.  
(3) \_\_init__ 메소드는 따로 호출하지 않아도 인스턴스를 생성할 때 자동으로 호출된다.  
(4) \_\_str__ 메소드는 인스턴스의 정보를 이해하기 쉬운 문자열로 나타내고 싶을 때 유용하게 사용된다.  
(5) 특수 메소드들은 파이썬에서 미리 지정한 특정 상황에 자동으로 호출되는 메소드이다.  

질문 3  
클래스 User에  
1. 인스턴스 메소드 say_hello(파라미터 : self)
2. 클래스 메소드 number_of_users(파라미터: cls)
3. 정적 메소드 is_valid_email(파라미터 : email_address)

가 있고, 그 인스턴스인 user1이 있을 때, 다음 중 에러를 일으키는 코드를 고르시오.  
(1) User.say_hello(user1)  
(2) user1.say_hello()  
(3) User.number_of_users()  
(4) user1.number_of_users(User)  
(5) user1.is_valid_email("t<span>aehosung@</span>codeit.kr")

<br/><br/>
<br/><br/>
<br/><br/>
#### 퀴즈 해설  
질문 1  
정답: (1)  
해설:  
(1) (O): 모든 인스턴스 변수를 __init__ 메소드에서 설정해주면 보기 쉬운 코드를 쓸 수 있습니다.  
(2) (X): 인스턴스를 통해 클래스 변수의 값을 바꾸려고 하면 클래스 변수의 값이 바뀌는 게 아니라 같은 이름의 새로운 인스턴스 변수가 만들어집니다. 따라서 클래스 변수의 값을 바꾸고 싶으면 인스턴스가 아닌 클래스로 접근해서 값을 바꿔야 합니다.  
(3) (X): 모든 인스턴스들이 같은 값을 공유해야하는 변수라면 클래스 변수로 정의해야 합니다.  
(4) (X): 모든 인스턴스 변수의 값이 같아도 인스턴스들은 서로 다른 존재일 수도 있습니다.  
(5) (X): 클래스 변수는 클래스나 인스턴스 2가지 방법을 통해서 접근할 수 있습니다.

질문 2  
정답: (2)  
해설: 인스턴스 메소드와 달리 클래스 메소드는 특정 인스턴스에 접근할 수 없습니다. 따라서 인스턴스 메소드에서 할 수 있는 것 중 클래스 메소드에서는 하지 못하는 것들도 있습니다.  

질문 3  
정답: (4)  
해설: 클래스 메소드는 어떤 방식으로 호출하든 첫번째 파라미터로 그 클래스가 넘어갑니다. number_of_users는 파라미터가 한 개만 필요한데, 보기 4에서는 자동 전달되는 User 클래스와 직접 전달한 User 클래스까지 총 두 개의 파라미터가 넘어가기 때문에 에러가 발생합니다.

22.09.29 21:46

## 3 미리 알고 가야 할 것들

### 01. 미리 알고 갑시다
'객체 지향 프로그래밍' 관련 여러 토픽들을 수강하기 전에는 파이썬 문법 등에 관한 사전 지식이 필요합니다. 이런 것들을 알아야 다음 단계로 넘어갈 수 있으니까 이 챕터의 내용을 꼼꼼히 읽고 기억해주세요!

### 02. 파이썬은 순수 객체 지향 언어?
파이썬으로 객체 지향 프로그래밍을 배우는 이유?  
파이썬이 순수 객체 지향 언어라서  
-> 파이썬의 모든 것이 객체라는 뜻  
숫자, 문자열 등 모두 어떤 클래스의 인스턴스  

[main3_02.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main3_02.py) 참고


22.12.26 22:02

### 03. 가변 vs. 불변 타입  
파이썬에서 객체는 크게 가변 타입과 불변 타입으로 나뉨  

**가변 타입 객체**  
- 한번 생성한 인스튼서의 속성 변경 가능
- ex) 리스트 클래스

**불변 타입 객체**  
- 한번 생성한 인스턴스의 속성 변경 불가
- ex) 튜플 클래스

어떤 타입이냐에 따라 같은 상황에서도 다른 결과 나타남  

[main3_03.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main3_03.py) 참고


### 04. 파이썬 퀴즈  
질문 1  
다음 중 틀린 정보를 고르세요  
1 파이썬은 순수 객체 지향 언어이다.  
2 클래스는 인스턴스를 만드는 틀의 역할을 한다.  
3 파이썬으로 코드를 쓰면 의도하지 않았어도 기본적으로 객체 지향 프로그래밍을 하게 된다.  
4 type 함수를 사용하면 인스턴스의 클래스를 확인할 수 있다.  
5 인스턴스를 먼저 만들고 이후에 클래스를 정의해도 된다.  

질문 2  
다음 중 파이썬에서 가변 타입인 것을 고르세요.  
1 딕셔너리(dict)  
2 문자열(str)  
3 불린(bool)  
4 정수(int)  
5 튜플(tuple)  

질문 3  
다음 파이썬 코드 마지막 줄에서 출력되는 값을 입력하세요.  
```python
def change_list(list_parameter):
    list_parameter[2] = 5

list_x = [1, 2, 3, 4]

change_list(list_x)
print(list_x[2])
```

<br/><br/>
<br/><br/>
<br/><br/>
#### 퀴즈 해설  
질문 1  
정답: (5)  
해설: 클래스를 미리 정의해놓지 않으면 해당 클래스의 인스턴스를 만들 수 없습니다.  

질문 2  
정답: (1)  
해설: 파이썬에서 리스트, 딕셔너리는 가변 타입이고 문자열, 불린, 정수, 튜플은 불변 타입입니다.

질문 3  
정답: 5  
해설:  
리스트는 가변 타입입니다. 가변 타입 인스턴스를 다른 변수 이름에 aliasing하고 그 변수를 통해 값을 수정한 상황입니다. list_x를 change_list에 list_parameter로 넘겨준 후, list_parameter의 2번째 인덱스의 요소를 바꿨네요. list_parameter와 list_x는 같은 인스턴스를 가리키므로 list_x를 통해서도 바뀐 결과를 볼 수 있습니다.

<br/><br/>
<br/><br/>
<br/><br/>

### 05. 절차 지향 프로그래밍 vs. 객체 지향 프로그래밍  
우리는 지금 **객체 지향 프로그래밍**을 배우고 있습니다. 그런데 객체 지향 프로그래밍이 있다면 객체 지향이 아닌 프로그래밍도 있지 않을까요? 맞습니다. 다른 프로그래밍도 있습니다.  

### 절차 지향 프로그래밍이란?
객체 지향 프로그래밍이 등장하기 이전에 **절차 지향 프로그래밍**이 있었습니다. 절차 지향 프로그래밍은 객체 지향 프로그래밍과 달리 ‘객체’라는 개념이 없습니다. 대신 절차 지향 프로그래밍에도 ‘함수’라는 개념은 있습니다. ‘함수’는 순서대로 특정 명령어들을 실행하는 부분을 하나로 묶은 것입니다. 절차 지향 프로그래밍으로 작성된 프로그램을 한번 봅시다.

#### 절차 지향 프로그래밍 예시
```python
# 절차 지향 프로그래밍
# 반복적으로 사용하는 코드를 함수로 정의한다
def print_person_info(person_name, person_age, person_gender):
    # 사람의 이름, 나이, 성별을 파라미터로 받으면 받은 정보를 이해할 수 있는 문자열로 출력해주는 함수
    print("사람 한 명을 소개합니다")
    print("{}님은 {}살이고 {}입니다".format(person_name, person_age, person_gender))
    
def is_underage(person_age):
    # 사람의 나이를 파라미터로 받아서 미성년자인지를 리턴해주는 함수
    return person_age < 20
    
# 영훈이의 정보
young_name = "영훈"
young_age = 10
young_gender = "남자"
    
# 윤수의 정보
yoonsoo_name = "윤수"
yoonsoo_age = 20
yoonsoo_gender = "남자"
    
# 영훈/윤수 정보 출력
print_person_info(young_name, young_age, young_gender)
print_person_info(yoonsoo_name, yoonsoo_age, yoonsoo_gender)
    
# 영훈/윤수가 미성년자인지 출력
print(is_underage(young_age))
print(is_underage(yoonsoo_age))
```
```python
사람 한 명을 소개합니다
영훈님은 10살이고 남자입니다
사람 한 명을 소개합니다
윤수님은 20살이고 남자입니다
True
False
```

print_person_info 함수와 is_underage 함수가 있네요. 이렇게 프로그램에 필요한 동작을 함수라는 단위로 묶어서 사용하는 것이 절차 지향 프로그래밍입니다. 같은 프로그램을 객체 지향 프로그래밍으로 작성하면 다음과 같습니다.

#### 객체 지향 프로그래밍 예시

```python
# 객체 지향 프로그래밍
# 속성과 행동을 갖는 객체들이 행동을 하는 방식으로 작성한다
class Person:
    # 사람을 나타내는 클래스
    def __init__(self, name, age, gender):
        # 사람은 이름, 나이, 성별을 속성으로 갖는다
        self.name = name
        self.age = age
        self.gender = gender
    
    def print_info(self):
        # 자신의 정보를 출력하는 메소드
        print("사람 한 명을 소개합니다")
        print("{}님은 {}살이고 {}입니다".format(self.name, self.age, self.gender))
    
    def is_underage(self):
        # 사람의 나이를 파라미터로 받아서 미성년자인지를 리턴해주는 메소드
        return self.age < 20
    
# 영훈/윤수을 나타내는 객체 생성
young = Person("영훈", 10, "남자")
yoonsoo = Person("윤수", 20, "남자")
    
# 영훈/윤수 정보 출력
young.print_info()
yoonsoo.print_info()
    
# 영훈/윤수가 미성년자인지 출력
print(young.is_underage())
print(yoonsoo.is_underage())
```
```python
사람 한 명을 소개합니다
영훈님은 10살이고 남자입니다
사람 한 명을 소개합니다
윤수님은 20살이고 남자입니다
True
False
```

객체 지향 프로그래밍은 필요한 동작 뿐만 아니라 아예 연관된 데이터도 객체로 묶어서 하나의 클래스로 나타냅니다. 즉,  
- 절차 지향 프로그래밍에서는 프로그램 안에서 서로 관련된 동작들만을 묶어서 관리하는데
- 객체 지향 프로그래밍에서는 관련된 동작들을 관련된 데이터와도 함께 묶어서 관리하는 거죠.

### 절차 지향 프로그래밍과 객체 지향 프로그래밍의 차이
절차 지향 프로그래밍이 객체 지향 프로그래밍과 다른 점은 크게 2가지입니다.
1. 절차 지향 프로그램은 프로그램에 필요한 데이터를 관련있는 함수와 묶어서 관리하기 힘듭니다. 그렇다면 객체 지향 프로그래밍은? 서로 관련있는 데이터와 함수를 객체로 묶어서 사용할 수 있습니다. 클래스라는 것이 있으니까요!
2. 절차 지향 프로그래밍은 프로그램을 단지 명령어들을 순서대로 실행하는 것으로 봅니다. 그렇다면 객체 지향 프로그래밍은? 프로그램을 객체 간의 소통으로 봅니다. 즉, 객체가 프로그램의 기본 단위가 되고 이 객체 속을 들여다보면 서로 관련된 데이터(객체의 속성)와 동작(객체의 행동)이 모여있습니다. 그리고 프로그램을 이 객체들이 순서대로 소통하는 과정으로 간주합니다.  

이 두 가지의 차이를 표로 나타내볼까요?  

|                 절차 지향 프로그래밍                 |                 객체 지향 프로그래밍                 |
|:----------------------------------------------------:|:----------------------------------------------------:|
|   프로그램을 만들 때 데이터와 함수를 합칠 수 없다.   |   프로그램을 만들 때 데이터와 함수를 합칠 수 있다.   |
| 프로그램을 명령어들을 순서대로 실행하는 것으로 본다. | 프로그램을 객체들이 순서대로 소통하는 과정으로 본다. |  

두 방식 중 어느 한 가지가 더 좋다고 할 수는 없습니다. 프로그램의 용도에 따라 적합한 방식이 다르기 때문입니다. 만약 데이터와 동작의 연관성이 높고 이걸 객체라는 단위로 묶는 것이 낫겠다는 생각이 들면 객체 지향 프로그래밍을 하는 것이 좋습니다. 보통 복잡한 프로그램일수록 객체 지향 프로그래밍으로 하는 것이 더 나은 경우가 많습니다.

<br/><br/>
<br/><br/>
<br/><br/>

### 06. 유용한 함수들  
앞으로 자주 마주치게 될 함수들을 미리 살펴봅시다.  

### max, min 함수  
```python
print(max(2, 5))             # => 5
print(max(2, 7, 5))          # => 7
print(min(2, 5))             # => 2
print(min(2, 7, 5, 11, 6))   # => 2
```
max 함수는 파라미터 중 가장 큰 값을, min 함수는 파라미터 중 가장 작은 값을 리턴합니다.  
두 함수 모두 원하는 개수만큼의 파라미터들을 넘겨줄 수 있습니다.  

### sum 함수  
```python
int_list = [1, 2, 3, 4, 5]
int_tuple = (4, 3, 6, 1, 2)
int_dict = {1: "one", 2: "two", 3: "three"}
    
print(sum(int_list))         # => 15
print(sum(int_tuple))        # => 16
print(sum(int_dict))         # => 6
```
sum 함수는 리스트, 튜플, 딕셔너리에 있는 숫자형 요소들의 합을 리턴합니다.  
sum 함수에 딕셔너리를 파라미터로 넘기면 key들의 합을 리턴합니다.  

### ternary expression  
```python
condition = True
    
if condition:
    condition_string = "nice"
else:
    condition_string = "not nice"
    
print(condition_string)      # => nice
```
```python
condition = True
    
condition_string = "nice" if condition else "not nice"
    
print(condition_string)      # => nice
```
위의 코드와 아래의 코드는 같은 내용입니다. "nice" if condition else "not_nice" 이 구문은
1. condition이 True 일 때는 "nice"가 되고
2. False 일 때는 "not_nice"가 된다는 뜻입니다.  

이렇게 불린(Boolean) 값에 따라 다른 값을 리턴하는 구문을 **ternary expression**이라고 합니다.  
ternary expression을 사용하면 if, else로 복잡하게 표현해야 하는 구문을 간단하게 나타낼 수 있습니다.

### list comprehension  
```python
int_list = [1, 2, 3, 4, 5, 6]
squares = []
    
for x in int_list:
    squares.append(x**2)
    
print(squares)               # [1, 4, 9, 16, 25, 36]
```
```python
int_list = [1, 2, 3, 4, 5, 6]
squares = [x**2 for x in int_list]
    
print(squares)               # [1, 4, 9, 16, 25, 36]
```
위 코드와 아래 코드는 같은 뜻입니다. **list comprehension**은 새로운 리스트를 만드는 간편한 방법입니다. 특정 리스트나 튜플을 바탕으로 리스트를 생성할 때
1. [] 안에 원하는 값을 리턴하는 식(x**2) 뒤에
2. for문을 써줍니다(for x in int_list).  

이렇게 쓰면 int_list 의 각 요소들을 제곱해준 값들로 이루어진 새로운 리스트가 생성됩니다.  
x**2 부분에 여러분이 원하는 식을 쓰면 되겠죠?

### zfill 메소드  
이 메소드는 문자열을 최소 몇 자리 이상을 가진 문자열로 변환시켜줍니다.  
이때 만약 모자란 부분은 왼쪽에 “0”을 채워주는데요.  
예를 들어 만약 "1".zfill(2)을 하면 "01"을 리턴합니다.  
그리고 설정된 자릿수보다 이미 더 긴 문자열이라면 그 문자열을 그대로 출력합니다.  
그러니까 "333".zfill(2) 와 같이 하면 문자열 그대로 “333”을 리턴합니다.  
아래 코드를 보면 더 쉽게 이해할 수 있습니다.  
이 메소드는 문자열을 예쁘고 통일감있게 출력하고자 할 때 자주 사용되니까 꼭 기억해주세요.  
```python
print("1".zfill(6))
print("333".zfill(2))
print("a".zfill(8))
print("ab".zfill(8))
print("abc".zfill(8))
```
실행결과
```
000001
333
0000000a
000000ab
00000abc
```


<br/><br/>
<br/><br/>
<br/><br/>

### 07. 모듈
**모듈**(module)이란 변수, 함수, 클래스 등을 모아놓은 파일입니다. 이런 모듈은 다른 곳에서 가져다 쓸 수 있습니다.  
calculator.py라는 모듈을 만들고, 다른 파일에서 이 모듈을 가져다 써봅시다.  

```python
# calculator.py
# calculator 모듈
    

# 합
def sum(x, y):
    return x + y
    
# 차이
def difference(x, y):
    return x - y
      
# 곱
def product(x, y):
    return x * y
    
# 제곱
def square(x):
    return x * x
```
test.py라는 파일을 만들어 calculator.py 모듈을 사용해봅시다.  
모듈 안에 있는 변수, 함수, 클래스를 사용하려면 test.py 파일 위에 다음과 같이 적어야 합니다.  
```python
from 모듈의 이름 import 불러올 변수/함수/클래스 이름
```
이때 모듈의 이름에는 파일명에서 확장자명(.py)을 뺀 이름을 적으면 됩니다.  
calculator.py에 정의된 sum이라는 함수를 호출해봅시다.
```python
# test.py

# calculator.py에서 sum 함수 불러오기
from calculator import sum
    
print(sum(3, 5))
```
```python
8
```
만약 calculator.py모듈에 정의된 모든 것들을 사용하려면 어떻게 선언해야 할까요?
```python
from calculator import sum, difference, product, square
```
위와 같이 하면 되겠죠? 하지만 모듈에서 가져오려는 하는 것이 100개 이상이라면? 100개의 이름을 모두 쓰기는 힘들겠죠?  
이럴 땐 *를 쓰면, 모듈 안에 정의된 모든 변수/함수/클래스를 사용할 수 있습니다.  
```python
from calculator import *
    
print(sum(3, 5))
print(difference(3, 5))
print(product(3, 5))
print(square(3))
```
```python
8
-2
15
9
```

### randint 함수와 uniform 함수  
파이썬에 기본으로 내장된 모듈에서 함수를 가져다 써봅시다.  
파이썬에 기본 내장된 random이라는 모듈에는 randint라는 함수가 있습니다.  
이 함수는 두 정수 사이에서 랜덤한 정수(난수)를 리턴하는 함수입니다.  
한번 사용해볼까요? 아래 코드처럼 하면 됩니다.

다음을 실행하면 1부터 20 사이의 정수 중 랜덤으로 한 가지 수가 출력됩니다.  
```python
from random import randint
# 1 <= N <= 20를 만족하는 랜덤한 정수(난수) N을 리턴한다.
x = randint(1, 20)
print(x)
```

uniform도 random 모듈에 있는 함수인데요, 두 수 사이의 랜덤한 소수(난수)를 리턴하는 함수입니다.  
다음을 실행하면 0과 1사이의 소수 중 랜덤으로 한 가지 수가 출력됩니다.  
```python
from random import uniform
# 0 <= N <= 1을 만족하는 랜덤한 소수(난수) N을 리턴한다.
x = uniform(0, 1)
print(x)
```

<br/><br/>
<br/><br/>
<br/><br/>

22.12.27  

## 4 객체 만들기 연습

### 01. 메뉴 만들기

#### 실습 설명
올해 코드잇 대학교를 졸업한 영훈이는 배달 어플 회사 “여기오”에 취직했습니다. “여기오”는 고객들이 배달 음식을 주문할 수 있는 어플을 만들려고 합니다. 영훈이가 맡게 된 업무는 어플에서 각 배달 음식 메뉴를 나타낼 클래스를 작성하는 건데요.

MenuItem 클래스가 가져야할 다음 조건들을 보고 배달 음식 메뉴를 나타내는 MenuItem 클래스를 정의해 보세요.  

- 인스턴스 변수(타입):
    - name(문자열): 메뉴 이름
    - price(숫자): 메뉴 가격
- 인스턴스 메소드:
    - __init__: MenuItem 클래스의 모든 인스턴스 변수를 초기화한다.
    - __str__: MenuItem 인스턴스의 정보를 문자열로 리턴한다. 단, 리턴 형식은 아래의 출력 예시와 같은 형식이어야 한다.

#### 출력예시
```
햄버거 가격: 4000
콜라 가격: 1500
후렌치 후라이 가격: 1500
```

[main4_01.py](https://github.com/jaehyun-dev/Today-I-Learned) 참고

<br/><br/>

### 02. 속성이 없는 계산기

#### 실습 설명  
이번 과제에서는 **계산기 클래스**를 만들어 볼게요. 이때까지 객체는 속성과 행동을 갖는 존재라고 했습니다.  
하지만 속성없이 행동만 있는 객체도 있습니다. 이 말은 변수는 없고 메소드만 있는 클래스도 만들 수 있다는 뜻입니다.  
우리가 배웠던 메소드의 종류는 아래 3가지입니다.  
1. 인스턴스 메소드  
2. 클래스 메소드  
3. 정적 메소드  

변수가 없는 클래스에서는 무슨 메소드를 써야 할까요? 이전에 우리는 인스턴스 변수나 클래스 변수를 쓰지 않을 거라면 **정적 메소드**(static method)를 사용해야 한다고 배웠죠? 변수가 없는 클래스에서는 정적 메소드를 정의하면 됩니다.

다음 조건들을 보고 계산기 클래스인 SimpleCalculator 클래스의 정적 메소드들을 완성해 보세요.  
- 정적 메소드
    - add: 파라미터로 받은 두 숫자의 합을 리턴한다
    - subtract: 첫 번째 파라미터에서 두 번째 파라미터를 뺀 값을 리턴한다
    - multiply: 파라미터로 받은 두 숫자의 곱을 리턴한다
    - divide: 첫 번째 파라미터를 두 번째 파라미터로 나눈 값을 리턴한다

[main4_02.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main4_02.py) 참고
