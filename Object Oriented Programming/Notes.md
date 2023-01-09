22.09.08 20:24  

# 객체 지향 프로그래밍이란?

## 1 객체 지향 프로그래밍 시작하기

### 01. 객체란?
객체 지향 프로그래밍을 이해하기 위해서는 우선 객체가 무엇인지 알아야 함  
객체: 속성, 행동으로 이루어진 존재  
우리가 살아가면서 보는 모든 존재를 객체라고 생각하면 됨  
예를 들어 자동차에는 색깔이라는 속성, 의자 개수라는 속성, 차의 높이 등의 속성이 있다  
또한 자동차에는 시동이 걸리는 행동, 악셀을 밟으면 앞으로 나아가는 행동 등이 있다  
이런 식으로 자동차에는 속성과 행동이 있기 때문에 자동차를 객체로 볼 수 있다  
또 다른 예시로 instagram과 같은 SNS의 유저들이 있다  
SNS 유저는 속성으로 이메일주소, 비밀번호, 친구목록 등이 있다  
그리고 행동으로 게시물에 좋아요 누르기, 친구 추가하기 등의 행동이 있다  
SNS 유저는 실제 물리적으로는 존재하지 않지만 속성과 행동이 있기 때문에 객체라고 볼 수 있다  
따라서 거의 모든 게 객체가 될 수 있다  
현실에 존재하든, 가상에 존재하든, 추상적 개념이든 상관없이 속성과 행동을 떠올릴 수 있다면 모두 객체  

<br/><br/>
  
### 02. 객체 지향 프로그래밍이란?
#### 객체 지향 프로그래밍이란  
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

<br/><br/>
<br/><br/>
<br/><br/>

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
  
<br/><br/>

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
  
<br/><br/>  
  
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

<br/><br/>

### 04. 인스턴스 메소드의 특별한 규칙
인스턴스 메소드를 사용하는 또다른 방법이 있음  
인스턴스 이름.메소드 이름()  
인스턴스로 메소드를 호출할 경우, 인스턴스가 첫 번째 파라미터로 전달됨  

[main04.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main04.py) 참고

<br/><br/>

22.09.11 20:03
### 05. self를 사용합시다
#### 인스턴스 메소드의 특별한 규칙
첫 번째 파라미터의 이름은 꼭! **self**로 쓰기  
  
[main05.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main05.py) 참고  

<br/><br/>

### 06. 인스턴스 변수와 같은 이름을 갖는 파라미터
인스턴스 변수와 파라미터의 이름이 같아도 상관없음  
심지어 이런 식으로 작성하는 게 꽤나 일반적이기도 함  
  
[main06.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main06py) 참고  

<br/><br/>
  
### 07. initialize 메소드
인스턴스 변수를 하나하나 작성하면 코드가 너무 길어짐  
클래스에 initialize 메소드를 만들어 간단하게 할 수 있음  
  
[main07.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main07.py) 참고  

<br/><br/>
  
### 08. \_\_init\_\_ 메소드
#### special method, magic method(특수 메소드)
앞뒤로 \_\_(underbar 2개) 붙어있으면 특수 메소드  
특정 상황에서 자동으로 호출되는 메소드  
#### \_\_init\_\_ 메소드
인스턴스가 생성될 때 자동으로 호출  
  
\_\_init\_\_ 메소드를 쓰면 인스턴스 생성과 동시에 인스턴스 변수 초기값 설정을 한 줄에 할 수 있음  
이러한 장점으로 클래스에는 보통 이닛 메소드를 꼭 작성함  
  
[main08.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main08.py) 참고  

<br/><br/>

### 09. #맞팔해요
  
[main09.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main09.py) 참고  

<br/><br/>

### 10. \_\_str\_\_ 메소드
메소드 이름 양옆에 underbar 두 개가 있는 특수 메소드  
"double underscore", 줄여서 **dunder** 메소드라고 부르기도 함  
dunder str 메소드라고 부름  
특수 메소드는 특정 상황에 자동으로 호출되는 메소드  
dunder str 메소드는 print 함수를 호출할 때 자동으로 부름  
어떤 인스턴스를 출력하면 dunder str 메소드의 return 값이 출력됨  
인스턴스를 출력할 때 우리가 원하는 정보를 나오게 하려면 클래스에 \_\_str\_\_ 메소드를 정의하면 됨  
  
[main10.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main10.py) 참고  

<br/><br/>

### 11. 클래스 변수 I
인스턴스 자신만의 속성을 나타내는 인스턴스 변수  
여러 인스턴스들이 공유하는 속성은?
  
SNS User 클래스의 user 인스턴스의 총 갯수를 나타내는 속성을 만들고 싶음  
이 속성은 특정 인스턴스가 갖고 있는 값이 아니라 서로 공유하는 값  
어떤 user 인스턴스라도 똑같은 값을 가지고 있어야 함  
파이썬에서는 이러한 속성을 **클래스 변수**라는 것으로 나타냄  
클래스 변수는 같은 클래스의 인스턴스들이 공유하는 값  
  
[main11.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main11.py) 참고  

<br/><br/>

### 12. 클래스 변수 II
#### 클래스 변수의 값을 읽는 법
1. 클래스 이름.클래스 변수 이름
2. 인스턴스 이름.클래스 변수 이름

#### 클래스 변수의 값 설정하는 법
1. 클래스 이름.클래스 변수 이름
  
[main12.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main12.py) 참고  

<br/><br/>

### 13. 여기서 잠깐! 데코레이터 I
#### 데코레이터(decorator)
파이썬에서 어떤 함수를 꾸며서 새로운 함수를 만들 때 사용하는 방법  

[main13.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main13.py) 참고

<br/><br/>

22.09.13 23:21  
### 14. 여기서 잠깐! 데코레이터 II
@ 붙여서 데코레이터 함수 이용하여 새로운 기능을 줄 수 있음  

[main14.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main14.py) 참고

<br/><br/>

22.09.14 23:46
### 15. 클래스 메소드 I
인스턴스 메소드: 인스턴스 변수의 값을 읽거나 설정하는 메소드  
클래스 메소드: 클래스 변수의 값을 읽거나 설정하는 메소드

#### 클래스 메소드의 특별한 규칙
클래스 메소드의 첫 번째 파라미터의 이름은 꼭! cls로 쓰기

#### 클래스 안의 함수를 클래스 메소드로 만드는 방법
classmethod 데코레이터로 함수를 데코레이팅 해주기

[main15.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main15.py) 참고

<br/><br/>

### 16. 클래스 메소드 II
인스턴스 변수를 사용하면 인스턴스 메소드를, 클래스 변수를 사용하면 클래스 메소드를 사용  
클래스 변수만 사용하는 메소드라면 클래스 메소드로 작성해야 함  
클래스 변수와 인스턴스 변수를 모두 사용하면 인스턴스 메소드 사용해야 함  
인스턴스 메소드는 인스턴스 변수와 클래스 변수를 모두 사용 가능한 반면, 클래스 메소드는 인스턴스 변수를 가져올 수 없기 때문  
인스턴스가 없을 때에도 필요하거나 사용할 가능성이 있으면 클래스 메소드로 만들어야 함  

[main16.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main16.py) 참고

<br/><br/>

### 17. 클래스 메소드 활용

[main17.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main17.py) 참고

<br/><br/>

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

<br/><br/>

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

<br/><br/>
<br/><br/>
<br/><br/>

22.09.29 21:46
## 3 미리 알고 가야 할 것들

### 01. 미리 알고 갑시다
'객체 지향 프로그래밍' 관련 여러 토픽들을 수강하기 전에는 파이썬 문법 등에 관한 사전 지식이 필요합니다. 이런 것들을 알아야 다음 단계로 넘어갈 수 있으니까 이 챕터의 내용을 꼼꼼히 읽고 기억해주세요!

<br/><br/>

### 02. 파이썬은 순수 객체 지향 언어?
파이썬으로 객체 지향 프로그래밍을 배우는 이유?  
파이썬이 순수 객체 지향 언어라서  
-> 파이썬의 모든 것이 객체라는 뜻  
숫자, 문자열 등 모두 어떤 클래스의 인스턴스  

[main3_02.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main3_02.py) 참고

<br/><br/>

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

<br/><br/>

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
```
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
```
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
    - \_\_init\_\_: MenuItem 클래스의 모든 인스턴스 변수를 초기화한다.
    - \_\_str\_\_: MenuItem 인스턴스의 정보를 문자열로 리턴한다. 단, 리턴 형식은 아래의 출력 예시와 같은 형식이어야 한다.

#### 출력예시
```
햄버거 가격: 4000
콜라 가격: 1500
후렌치 후라이 가격: 1500
```

[main4_01.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main4_01.py) 참고

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


<br/><br/>

### 03. 게임 캐릭터 만들기

#### 실습 설명
한국의 최대 온라인 게임업체 넥손에서 일하는 대위는 최근 새 프로젝트인 ‘은행스토리’에 개발자로 참여하게 되었는데요. 대위가 맡은 부분은 게임 캐릭터를 ‘클래스’로 작성하는 것입니다. 이미 객체의 속성과 행동을 어떻게 할지에 대해서는 생각을 마친 상태입니다.  

다음 조건들과 출력 예시에 맞게 GameCharacter클래스를 작성하세요.  
- 인스턴스 변수(타입)
    - name(문자열): 캐릭터의 이름
    - hp(숫자형): 캐릭터의 체력
    - power(숫자형): 캐릭터의 공격력
- 인스턴스 메소드
    - \_\_init\_\_: 사용할 모든 인스턴스 변수를 설정한다.
    - is_alive: 게임 캐릭터의 체력이 0보다 큰지(살았는지 죽었는지) 확인한다.
        - 0 초과이면 True를, 0 이하라면 False를 리턴한다.
    - get_attacked: 게임 캐릭터의 체력이 0보다 큰 상태라면 파라미터로 받은 공격력만큼 체력을 깎는다.
        - 조건:
            - is_alive 메소드를 사용해서 인스턴스가 살아있을 때만 체력을 깎는다. 이미 캐릭터가 죽었으면 죽었다는 메시지를 출력한다.
            - 남은 체력보다 공격력이 더 크면 체력(hp)을 0으로 설정한다.
    - attack: 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다.
        - 조건:
            - is_alive 메소드를 이용해서 살아있는 인스턴스만 공격을 할 수 있도록 한다.
            - get_attacked 메소드를 사용한다.
    - \_\_str\_\_: 게임 캐릭터의 의미있는 정보를 포함한 문자열을 리턴한다.

#### 실습 결과
```
Ww영훈전사wW님은 이미 죽었습니다.
Ww영훈전사wW님의 hp는 0만큼 남았습니다.
Xx지웅최고xX님의 hp는 70만큼 남았습니다.
```

[main4_03.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main4_03.py) 참고

<br/><br/>

22.12.28  

### 04. 블로그 유저 만들기

#### 실습 설명
프로그래밍에 관심이 많은 영준이는 여러 사람들이 자신의 글을 올릴 수 있는 블로그를 만들려고 합니다. 영준이는 일단 아래와 같이 게시글을 나타내는 Post 클래스를 정의했습니다.

#### Post 클래스
```python
class Post:
    # 게시글 클래스
    def __init__(self, date, content):
        # 게시글은 속성으로 작성 날짜와 내용을 갖는다
        self.date = date
        self.content = content
    
    def __str__(self):
        # 게시글의 정보를 문자열로 리턴하는 메소드
        return "게시일: {}\n내용: {}".format(self.date, self.content)
```
이제 블로그 유저를 나타내는 클래스를 정의해 볼까요? 다음 조건들과 출력 예시를 보고 BlogUser 클래스를 정의해 보세요.

- 인스턴스 변수(타입)
    - name(문자열): 블로그 사용자의 이름
    - posts(리스트): 블로그 게시글들을 담을 리스트
- 메소드
    - \_\_init\_\_: 인스턴스 변수가 설정되는 메소드
    - add_post: 블로그 사용자의 블로그 게시글 리스트에 새로운 게시글 인스턴스를 추가하는 메소드
    - show_all_posts: 블로그 사용자가 올린 모든 게시글을 출력하는 메소드
    - \_\_str\_\_: 블로그 사용자의 간단한 인사와 이름을 문자열로 리턴하는 메소드

#### 실습 결과
```
안녕하세요 성태호입니다.

작성 날짜: 2019년 8월 30일
내용: 
오늘은 내 생일이었다.
많은 사람들이 축하해줬다.
행복했다.

작성 날짜: 2019년 8월 31일
내용: 
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
```

[main4_04.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main4_04.py) 참고

<br/><br/>
<br/><br/>
<br/><br/>

22.12.29
## 5 객체 지향 프로그래밍 직접 해보기

### 01. 혹시... 시간이 어떻게 되나요?

이번 토픽에서는 객체 지향 프로그래밍이 무엇인지, 그리고 파이썬에서 클래스와 인스턴스를 어떻게 만드는지 배웠는데요. 배운 것을 다시 제대로 점검합시다.

우리가 컴퓨터나 스마트폰에서 자주 확인하는 시계 프로그램을 객체 지향 프로그래밍으로 만들어봅시다.

일단 정의하려는 시계가 어떤 기능을 가져야할지 먼저 정합시다. 특별한 기능을 갖기보다는 기본 기능에 충실한 시계를 만들려고 합니다. 다음과 같은 기능들이 필요하겠죠?

1. 현재 시간을 설정할 수 있다.
2. 현재 시간을 변경할 수 있다.
3. 현재 시간에 1초씩 더할 수 있다.

아래의 코드처럼 Clock 클래스를 사용할 수 있도록, 이 3가지 기능들을 Clock 클래스 안에 정의해야합니다.
```python
# 1시 30분 48초인 시계 인스턴스 생성
clock = Clock(1, 30, 48)
    
# 13초를 늘린다
for i in range(13):
    clock.tick()
    
# 시계의 현재 시간 출력
print(clock)
    
# 2시 3분 58초로 시계 세팅
clock.set(2, 3, 58)
    
# 5초를 늘린다
for i in range(5):
    clock.tick()
    
# 시계의 현재 시간 출력
print(clock)
    
# 23시 59분 57초로 세팅
clock.set(23, 59, 57)
    
# 5초를 늘린다
for i in range(5):
    clock.tick()
    
# 시계의 현재 시간 출력
print(clock)
```
#### 실행 결과
```
01:31:01
02:04:03
00:00:02
```
위 코드처럼 작동하는 Clock 클래스를 작성한다고 할 때, 어떤 속성과 기능(행동)을, 어떻게 넣어야 할까요?
다음 레슨의 설명을 듣기 전에 꼭 스스로 이 부분에 대해 고민해보세요!

[main5_01.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main5_01.py) 참고

<br/><br/>

### 02. 시간 나누기

#### 실습 설명
비슷한 객체를 표현하더라도 그 내부를 어떻게 구성하느냐는 프로그램의 목적이나 개발자의 생각에 따라 다를 수 있습니다. 일단 이 과제에서는 어떻게 문제를 풀지에 대한 간단한 **가이드**를 드릴게요, 본인만의 다른 사고방식이 있다면 답을 보기 전에 먼저 본인의 방식대로 과제를 풀어봐도 좋습니다.

자, 이제 가이드를 드리겠습니다. 시계는 결국 시간을 나타내는 기능이 핵심이고 시간은 **시, 분, 초**로 구성되어 있습니다. 시, 분, 초 이 3가지는 모두 하나의 클래스로 표현 가능합니다. 이 하나의 클래스는 다음과 같은 속성과 행동을 가져야 합니다.

##### 속성
- 시, 분, 초는 각각 자기의 “값”을 속성으로 갖습니다. 예를 들면 4시 54분 12초에서는 4, 54, 12가 각각 시, 분, 초의 값이 되죠.
- 시, 분, 초 모두 “최댓값”이 있습니다. 분과 초는 각각 59, 그리고 시는 23이라는 최댓값을 가집니다.

##### 행동
- 값 1 증가시키기:
    - 시간이 흐르는 동작 즉 1초, 1분, 1시가 증가하는 동작을 할 수 있어야 합니다.
    - 이렇게 시간이 흐를 때 시, 분, 초는 각자의 최댓값에 도달하면 그 값을 0으로 바꾸고 그 위의 단위를 1 증가시켜야 합니다. 예를 들어 59초에서 60초가 되면 초를 다시 0으로 바꿔주고 분을 1분 늘리는 것처럼요.
- 값 설정하기: 가끔씩 잘 되던 시계에 오차가 생기거나 시간대가 다른 나라로 여행을 가면 현재 시간을 변경해야 합니다. 이렇게 하려면 시, 분, 초를 바로 세팅할 수 있어야겠죠? 이 기능도 추가하겠습니다.  

이처럼 같은 속성과 행동을 갖는 시, 분, 초를 하나의 클래스로 나타내 봅시다. 시, 분, 초의 주된 동작은 "0 또는 시작값"에서 "최댓값"까지 숫자를 증가시키는 것이니까 클래스 이름을 Counter로 작성해 봅시다.

#### 실습 결과
```
1부터 5까지 카운트하기 
01 
02
03
04
05
카운터 값 0으로 설정하기
00
카운터 값 27로 설정하기
27
카운터 값이 30이 되면 0으로 바뀝니다
28
29
00
01
02
```

<br/><br/>
<br/><br/>
<br/><br/>

#### 해설
```python
class Counter:
    """
    시계 클래스의 시,분,초를 각각 나타내는데 사용될 카운터 클래스    
    """
    
    def __init__(self, limit):
        """
        인스턴스 변수 limit(최댓값), value(현재까지 카운트한 값)을 설정한다.
        인스턴스를 생성할 때 인스턴스 변수 limit만 파라미터로 받고, value는 초깃값 0으로 설정한다.
        """
        # 여기에 코드를 작성하세요
    
    def set(self, new_value):
        """
        파라미터가 0 이상, 최댓값 미만이면 value에 설정한다.
        아닐 경우 value에 0을 설정한다.
        """
        # 여기에 코드를 작성하세요
    
    def tick(self):
        """
        value를 1 증가시킨다.
        카운터의 값 value가 limit에 도달하면 value를 0으로 바꾼 뒤 True를 리턴한다.
        value가 limit보다 작은 경우 False를 리턴한다.
        """
        # 여기에 코드를 작성하세요
    
    def __str__(self):
        """
        value를 최소 두 자릿수 이상의 문자열로 리턴한다. 
        일단 str 함수로 숫자형 변수인 value를 문자열로 변환하고 zfill 메소드를 호출한다. 
        """
        return str(self.value).zfill(2)
```

Counter 클래스의 메소드를 하나씩 살펴봅시다.

##### \_\_init\_\_ 메소드
파라미터로 받은 limit을 인스턴스 변수 limit에 설정하고, 인스턴스 변수 value에 0을 설정합니다. 코드로는 이렇게 해주면 됩니다.  
```python
def __init__(self, limit):
    """
    인스턴스 변수 limit(최댓값), value(현재까지 카운트한 값)을 설정한다.
    인스턴스를 생성할 때 인스턴스 변수 limit만 파라미터로 받고, value는 초깃값 0으로 설정한다.
    """
    self.limit = limit
    self.value = 0
```

##### set 메소드
인스턴스 변수 value를 파라미터 new_value의 값에 따라 new_value 의 값으로 설정하거나 0으로 설정해야 합니다. **ternary expression**을 사용하면 불린 조건에 따라 다른 값을 지정할 수 있습니다.  
```python
def set(self, new_value):
    """
    파라미터가 0 이상, 최댓값 미만이면 value에 설정한다.
    아닐 경우 value에 0을 설정한다.
    """
    self.value = new_value if 0 <= new_value < self.limit else 0
```
위 코드는 아래의 코드랑 똑같은 뜻을 가집니다. 하지만 위 코드처럼 좀 더 짧게 쓰는 게 보기 좋죠?
```python
def set(self, new_value):
    """
    파라미터가 0 이상, 최댓값 미만이면 value에 설정한다.
    아닐 경우 value에 0을 설정한다.
    """
    if 0 <= new_value < self.limit:
        self.value = new_value
    else:
        self.value = 0
```

##### tick 메소드
tick 메소드는 다음 설명에 따라 동작하면 됩니다.
1. 인스턴스 변수 value의 값을 1만큼 증가시키고
2. value의 값이 limit 값과 같으면
    1. value 변수에 0을 지정하고
    2. True를 리턴한다
3. 같지 않다면 False를 리턴한다

코드로 바꾸면 이렇게 되겠죠?
```python
def tick(self):
    """
    value를 1 증가시킨다.
    카운터의 값 value가 limit에 도달하면 value를 0으로 바꾼 뒤 True를 리턴한다.
    value가 limit보다 작은 경우 False를 리턴한다.
    """
    self.value += 1
    
    if self.value == self.limit:
        self.value = 0
        return True
    return False
```
아래는 완성된 Counter 클래스의 전체 코드입니다.

#### 모범 답안
```python
class Counter:
    """
    시계 클래스의 시,분,초를 각각 나타내는데 사용될 카운터 클래스
    """
    
    def __init__(self, limit):
        """
        인스턴스 변수 limit(최댓값), value(현재까지 카운트한 값)을 설정한다.
        인스턴스를 생성할 때 인스턴스 변수 limit만 파라미터로 받고, value는 초깃값 0으로 설정한다.
        """
        self.limit = limit
        self.value = 0
    
    def set(self, new_value):
        """
        파라미터가 0 이상, 최댓값 미만이면 value에 설정한다.
        아닐 경우 value에 0을 설정한다.
        """
        self.value = new_value if 0 <= new_value < self.limit else 0
    
    def tick(self):
        """
        value를 1 증가시킨다.
       카운터의 값 value가 limit에 도달하면 value를 0으로 바꾼 뒤 True를 리턴한다.
        value가 limit보다 작은 경우 False를 리턴한다.
        """
        self.value += 1
    
        if self.value == self.limit:
            self.value = 0
            return True
        return False
    
    def __str__(self):
        """
        value를 최소 두 자릿수 이상의 문자열로 리턴한다. 
        일단 str 함수로 숫자형 변수인 value를 문자열로 변환하고 zfill을 호출한다. 
        """
        return str(self.value).zfill(2)
```
Counter 클래스가 제대로 작동하는지 확인합시다.
```python
# 최대 30까지 셀 수 있는 카운터 인스턴스 생성
counter = Counter(30)

# 0부터 5까지 센다
print("1부터 5까지 카운트하기")
for i in range(5):
    counter.tick()
    print(counter)

# 타이머 값을 0으로 바꾼다
print("카운터 값 0으로 설정하기")
counter.set(0)
print(counter)

# 카운터 값 27로 설정
print("카운터 값 27로 설정하기")
counter.set(27)
print(counter)

# 카운터 값이 30이 되면 0으로 바뀌는지 확인
print("카운터 값이 30이 되면 0으로 바뀝니다")
for i in range(5):
    counter.tick()
    print(counter)    
```
#### 실습 결과
```
1부터 5까지 count
01
02
03
04
05
카운터 값 0으로 설정하기
00
카운터 값 27로 설정하기
27
카운터 값이 30이 되면 0으로 바뀝니다
28
29
00
01
02
```
잘 동작하네요! 이제 Counter 클래스로 인스턴스 3개를 만들면 각각 시, 분, 초를 나타내도록 할 수 있겠네요. 이걸 잘 진행하면 결국 시계를 완성할 수 있을 것 같은데, 다음 실습에서 계속 진행해 봅시다.

[main5_02.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main5_02.py) 참고

<br/><br/>

### 03. 시계 프로그램

#### 실습 설명
"0 또는 시작값"에서부터 특정 "최댓값"까지 숫자를 증가시키는 Counter 클래스를 정의했습니다. 그렇다면 Counter 클래스로 어떻게 시계의 시, 분, 초를 나타낼 수 있을까요? 그 전에 일단 ‘시계’라는 객체도 클래스로 정의해야겠죠? 이전의 레슨에서 보았듯이, 만들려는 시계 프로그램은 다음 조건들을 만족해야 합니다.
1. 현재 시간을 설정할 수 있다.
2. 현재 시간을 변경할 수 있다.
3. 현재 시간에 1초씩 더할 수 있다.
Counter 클래스를 조합하면 시계의 기능을 완성할 수 있는데요. 시계를 나타내는 클래스의 이름은 Clock으로 하겠습니다. Clock 클래스가 가질 속성과 행동을 먼저 봅시다.

##### 속성
시계는 현재 시간을 속성으로 가집니다. Counter 클래스를 사용해서 시, 분, 초를 나타낼 수 있습니다.
- 초: 1부터 59까지 셀 줄 아는 Counter 클래스의 인스턴스
- 분: 1부터 59까지 셀 줄 아는 Counter 클래스의 인스턴스
- 시: 1부터 23까지 셀 줄 아는 Counter 클래스의 인스턴스

##### 행동
- 1초 증가시키기
    - 시간을 1초씩 증가시킵니다.
    - 이때 주의할 점은 시간을 증가시킬 때 59초가 60초가 되면 초를 다시 00초로 바꾼 후에 분을 1분 증가시키고, 59분이 60분이 되면 분을 다시 00분으로 바꾼 후에 시를 1시간 증가시키는 것입니다. 이것은 당연한 시간의 원리이니 따로 설명하지 않겠습니다. 이 부분을 구현할 때 Counter 클래스의 tick 메소드의 리턴값(True 또는 False)이 어떻게 활용될지 생각해 보세요.
- 값 변경하기: 이미 Counter 클래스에는 값을 설정하는 메소드가 있습니다. 시계 클래스에서 시간을 설정할 때 시, 분, 초를 각각 따로 설정하는 건 귀찮겠죠? 시, 분, 초의 값을 한번에 설정하는 메소드를 만듭시다.  

이러한 속성과 행동을 가지는 Clock 클래스를 정의해 보세요!

#### 실습 결과
```
시간을 1시 30분 48초로 설정합니다
01:30:48
13초가 흘렀습니다
01:31:01
시간을 2시 59분 58초로 설정합니다
02:59:58
5초가 흘렀습니다
03:00:03
시간을 23시 59분 57초로 설정합니다
23:59:57
5초가 흘렀습니다
00:00:02
```

<br/><br/>
<br/><br/>
<br/><br/>

#### 해설
```python
    def set(self, hour, minute, second):
        """현재 시간을 파라미터 hour시, minute분, second초로 설정한다."""     

    def tick(self):
        """
        초 카운터의 값을 1만큼 증가시킨다.
        초 카운터를 증가시킬 때, 분 또는 시가 바뀌어야하는 경우도 처리한다.
        """

    def __str__(self):
        """
        현재 시간을 시:분:초 형식으로 리턴한다. 시, 분, 초는 두 자리 형식이다.
        예시: "03:11:02"
        """
```
Clock 클래스의 메소드를 하나씩 살펴보겠습니다.

##### \_\_init\_\_ 메소드, set 메소드  
먼저 시, 분, 초를 나타내는 인스턴스 변수 3개가 필요합니다. 이를 위해 hour, minute, second 라는 Counter 클래스의 인스턴스 3개를 정의합니다. hour의 최댓값은 24, minute과 second의 최댓값은 60입니다. Clock  클래스의 클래스 변수들 HOURS, MINUTES, SECONDS를 사용해서 최댓값을 지정하겠습니다. 그리고 Counter 클래스의 set 메소드로 현재의 시, 분, 초를 설정하면 되겠네요.
```python
def __init__(self, hour, minute, second):
    """
    각각 시, 분, 초를 나타내는 카운터 인스턴스 3개(hour, minute, second)를 정의한다.
    현재 시간을 파라미터 hour시, minute분, second초로 지정한다.
    """
    self.hour = Counter(Clock.HOURS)
    self.minute = Counter(Clock.MINUTES)
    self.second = Counter(Clock.SECONDS)

    self.hour.set(hour)
    self.minute.set(minute)
    self.second.set(second)
```
다음은 Clock 클래스의 set 메소드를 작성합시다. 이미 __init__ 메소드에서 각 Counter 인스턴스를 초기화했으므로 여기서는 Counter 인스턴스의 값만 지정하면 됩니다. Counter 클래스의 set 메소드를 사용하면 됩니다.
```python
def set(self, hour, minute, second):
    """현재 시간을 파라미터 hour시, minute분, second초로 설정한다."""
    self.hour.set(hour)
    self.minute.set(minute)
    self.second.set(second)
```
Clock 클래스의 set 메소드의 바디를 작성하고 나니 그 내용이 \_\_init\_\_ 메소드의 뒷부분과 똑같죠? \_\_init\_\_ 메소드의 뒷부분을 방금 완성한 set 메소드를 사용해서 더 간결하게 나타냅시다.
```python
def __init__(self, hour, minute, second):
    """
    각각 시, 분, 초를 나타내는 카운터 인스턴스 3개(hour, minute, second)를 정의한다.
    현재 시간을 파라미터 hour시, minute분, second초로 지정한다.
    """
    self.hour = Counter(Clock.HOURS)
    self.minute = Counter(Clock.MINUTES)
    self.second = Counter(Clock.SECONDS)

    self.set(hour, minute, second)
```
\_\_init\_\_ 메소드가 훨씬 더 간결해졌네요.

##### tick 메소드
Counter 클래스의 tick 메소드는 해당 인스턴스의 value를 1만큼 증가시키고 최댓값에 도달하면 value의 값을 0으로 바꾼 후 True를 리턴합니다.

시간은 1초씩 증가하니까 초를 나타내는 second의 tick 메소드를 호출해야 합니다. 이렇게 1초씩 증가시키다가 second의 value가 limit 이상이 될 경우 True를 리턴해야 합니다. 이 True의 의미는 무엇일까요? 초의 값을 0으로 초기화하고 더 윗 단위인 minute을 1만큼 증가시키라는 겁니다. 이 부분을 이해했다면 아래 코드를 보세요.
```python
def tick(self):
    """
    초 카운터의 값을 1만큼 증가시킨다.
    초 카운터를 증가시킴으로써, 분 또는 시가 바뀌어야하는 경우를 처리한다.
    """
    if self.second.tick():
        if self.minute.tick():
            self.hour.tick()
```
Clock 클래스의 tick 메소드에서 시, 분, 초를 나타내는 Counter 인스턴스 3가지의 tick 메소드를 사용하고 있죠? 이렇게 계단식으로 표현하면 초가 60초가 되면 1분이 늘어나고, 분이 60분이 되면 시가 1시 늘어납니다. 뭔가 참신한 방법 아닌가요? 여러분은 어떤 식으로 구현했을지 궁금하네요.

##### \_\_str\_\_ 메소드
아래와 같이 문자열의 {}와 format 메소드로 hour, minute, second 변수들의 값을 {}이 있는 부분에 순서대로 추가할 수 있는데요. 이렇게 하면 시계 인스턴스를 출력할 때 "시:분:초" 형식의 현재 시간이 출력되겠죠?
```
def __str__(self):
    """
    현재 시간을 시:분:초 형식으로 리턴한다. 시, 분, 초는 두 자리 형식이다.
    예시: "03:11:02"
    """
    return "{}:{}:{}".format(self.hour, self.minute, self.second)
```
완성된 Clock 클래스의 전체 코드는 다음과 같습니다.

#### 모범 답안
```python
class Clock:
    """
    시계 클래스
    """
    HOURS = 24 # 시 최댓값
    MINUTES = 60 # 분 최댓값
    SECONDS = 60 # 초 최댓값

    def __init__(self, hour, minute, second):
        """
        각각 시, 분, 초를 나타내는 카운터 인스턴스 3개(hour, minute, second)를 정의한다.
        현재 시간을 파라미터 hour시, minute분, second초로 지정한다.
        """
        self.hour = Counter(Clock.HOURS)
        self.minute = Counter(Clock.MINUTES)
        self.second = Counter(Clock.SECONDS)

        self.set(hour, minute, second)

    def set(self, hour, minute, second):
        """현재 시간을 파라미터 hour시, minute분, second초로 설정한다."""
        self.hour.set(hour)
        self.minute.set(minute)
        self.second.set(second)

    def tick(self):
        """
        초 카운터의 값을 1만큼 증가시킨다.
        초 카운터를 증가시킴으로써, 분 또는 시가 바뀌어야하는 경우를 처리한다.
        """
        if self.second.tick():
            if self.minute.tick():
                self.hour.tick()

    def __str__(self):
        """
        현재 시간을 시:분:초 형식으로 리턴한다. 시, 분, 초는 두 자리 형식이다.
        예시: "03:11:02"
        """
        return "{}:{}:{}".format(self.hour, self.minute, self.second)
```
이제 Clock 클래스를 사용하는 코드를 실행해 봅시다.
```python
# 초가 60이 넘을 때 분이 늘어나는지 확인하기
print("시간을 1시 30분 48초로 설정합니다")
clock = Clock(1, 30, 48)
print(clock)

# 13초를 늘린다
print("13초가 흘렀습니다")
for i in range(13):
    clock.tick()
print(clock)

# 분이 60이 넘을 때 시간이 늘어나는지 확인
print("시간을 2시 59분 58초로 설정합니다")
clock.set(2, 59, 58)
print(clock)

# 5초를 늘린다
print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)

# 시간이 24가 넘을 때 00:00:00으로 넘어가는 지 확인
print("시간을 23시 59분 57초로 설정합니다")
clock.set(23, 59, 57)
print(clock)

# 5초를 늘린다
print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)
```

#### 실습 결과
```
시간을 1시 30분 48초로 설정합니다
01:30:48
13초가 흘렀습니다
01:31:01
시간을 2시 59분 58초로 설정합니다
02:59:58
5초가 흘렀습니다
03:00:03
시간을 23시 59분 57초로 설정합니다
23:59:57
5초가 흘렀습니다
00:00:02
```

잘 출력되는군요! 이렇게 우리는 Clock 클래스에서 Counter라는 다른 클래스의 인스턴스를 사용해서 그 기능을 완성해 보았습니다. 이제 객체를 설계하고 실제 클래스로 만들어보는 게 좀 익숙해지셨나요? 일단 여러분은 객체 지향 프로그래밍의 기초를 모두 배우신 겁니다. 보람찬 마음을 갖고 객체 지향 프로그래밍을 더 공부해 봅시다!

[main5_03.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Object%20Oriented%20Programming/main5_03.py) 참고
