# 추상화

2023.03.17

## 01. 객체 지향 프로그래밍의 4가지 기둥이란?

### 객체 지향 프로그래밍의 4가지 기둥
- 추상화(Abstraction)
- 캡슐화(Encapsulation)
- 상속(Inheritance)
- 다형성(Polymorphism)

<img src="https://i.imgur.com/oQeEd4g.png">

<br/><br/>

2023.03.18

## 02. 추상화란?
- 프로그래머들이 특정 코드를 사용할 때 필수적인 정보를 제외한 세부사항을 가리는 것
- 예) 커피를 만들기 위해 커피 머신을 사용할 줄 알면 되지 커피 머신의 구조와 부품의 작동 원리까지 알 필요는 없는 것

<br/><br/>

2023.03.19

## 03. 추상화는 이때까지 쓰고 있었다
- 변수나 함수, 클래스를 쓰는 것도 추상화
- 구체적인 값이나 동작하는 원리를 알지 못해도, 이름, 파라미터, 역할, 사용하는 방법 등만 알면 잘 활용할 수 있음
- 추상화를 잘 이해하면 예전에 썼던 코드를 보거나 개발자들 상호 간에 코드를 이해하고 활용하는 데 도움이 됨

<br/><br/>

2023.03.20

## 04. 추상화 잘하기: 이름 잘 짓기
- 변수, 메소드, 클래스의 이름을 잘 지어야 뭐를 나타내는지 잘 파악할 수 있다
- 코드만 보고도 어디에 쓰고 어떻게 쓰는지 감이 오면 좋은 이름

<br/><br/>

2023.03.21

## 05. 추상화 더 잘하기: 문서화하기
문서화(documentation string, docstring, 문서화 문자)
- 이 클래스는 무엇을 위해 만들어졌고 어떻게 사용하는지
- 이 변수는 어떤 변수이고 자료형은 무엇인지
- 이 메소드는 어떤 기능을 하는 메소드인지

```python
"""
설명하고 싶은 클래스나 메소드 이름 바로 아래 필요한 정보를 쓰면 됨.
"""
```

![image](https://user-images.githubusercontent.com/71001479/226637831-0b1d7774-b977-4fac-8b79-8972b9bb8171.png)

<br/><br/>

2023.03.22

## 06. 추상화 잘 쓰기: 문서화 결과
class 중간중간에 있는 docstring 읽는 것보다 더 편한 방법  
```python
help(class_name)
```
클래스에 있는 docstring 한 번에 보여줌

![image](https://user-images.githubusercontent.com/71001479/226938046-b7243037-314a-4cd2-87fc-b903e9c1ae71.png)  

list 클래스의 docstring:  
![image](https://user-images.githubusercontent.com/71001479/226938260-45c5712c-87f7-48f3-81b2-f989036e529b.png)

<br/><br/>

2023.03.23

## 07. 문서화 스타일

흔히 사용하는 3가지 포맷:

```python
def find_suggestion_videos(self, number_of_suggestions=5):
```

### Google docstring:
```python
"""유저에게 추천할 영상을 찾아준다
Parameters:
  number_of_suggestions (int): 추천하고 싶은 영상 수
    (기본값은 5)
    
Returns:
  list: 추천할 영상 주소가 담긴 리스트
"""
```

### reStructuredText (파이썬 공식 문서화 기준):
```
"""유저에게 추천할 영상을 찾아준다
    
:param number_of_suggestions: 추천하고 싶은 영상 수
  (기본값은 5)
:type number_of_suggestions: int
:returns: 추천할 영상 주소가 담긴 리스트
:rtype: list
"""
```

### NumPy/SciPy (통계, 과학 분야에서 쓰이는 Python 라이브러리):
```python
"""유저에게 추천할 영상을 찾아준다
    
Parameters
----------
number_of_suggestions: int
  추천하고 싶은 영상 수 (기본값은 5)
    
Returns
-------
list 
  추천할 영상 주소가 담긴 리스트
"""
```

프로그램을 함께 만드는 팀원들과 문서화 포맷에 관해 미리 약속하고 잘 지킬 것  
일관성 있게 사용한다면 나중에 프로그램 수정할 때 도움 됨

<br/><br/>

2023.03.24

## 08. User 클래스 문서화하기
```python
class User:
    """SNS의 유저를 나타내는 클래스"""
    count = 0

    def __init__(self, name, email, pw):
        """이름, 이메일, 비밀번호를 인스턴스 변수로 갖고, 인스턴스가 생성될 때마다 클래스 변수 count를 1씩 증가시킨다."""
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        """유저의 이름을 포함한 인사 메시지를 출력한다."""
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        """유저 정보를 정의된 문자열 형태로 리턴한다."""
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    @classmethod
    def number_of_users(cls):
        """총 유저 수를 출력하는 클래스 메소드"""
        print("총 유저 수는: {}입니다".format(cls.count))

help(User)
```
```
Help on class User in module __main__:

class User(builtins.object)
 |  User(name, email, pw)
 |  
 |  SNS의 유저를 나타내는 클래스
 |  
 |  Methods defined here:
 |  
 |  __init__(self, name, email, pw)
 |      이름, 이메일, 비밀번호를 인스턴스 변수로 갖고, 인스턴스가 생성될 때마다 클래스 변수 count를 1씩 증가시킨다.
 |  
 |  __str__(self)
 |      유저 정보를 정의된 문자열 형태로 리턴한다.
 |  
 |  say_hello(self)
 |      유저의 이름을 포함한 인사 메시지를 출력한다.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  number_of_users() from builtins.type
 |      총 유저 수를 출력하는 클래스 메소드
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  count = 0
```

신경써서 이름을 잘 짓고 문서화하는 것이 객체 지향 프로그래밍 추상화를 잘하는 첫 걸음  
좋은 개발자가 되고 다른 개발자들과 협업을 잘하기 위해 필수적

<br/><br/>

2023.03.25

## 09. 여기서 잠깐! 파이썬의 type hinting

파이썬은 동적 타입 언어 -> 변수의 타입을 따로 정하지 않아도 됨  
정적 타입 언어에서는 변수의 타입을 표시해야 함  

동적 타입 언어는 타입을 안 적어서 코드를 더 적게 적어도 된다는 장점이 있음  
그러나 어떤 타입의 값을 넣어야 하는지 표시가 없어 개발자들이 혼란을 느낄 수 있다는 단점이 있음  

파이썬은 이를 보완하기 위해 버전 3.5부터 type hinting 기능 추가함  
변수나 파라미터 이름 뒤에 콜론(:) 쓰고 타입 쓰면 됨  
메소드의 리턴값은 정의 뒤에 화살표(->) 쓰고 타입 쓰면  
```python
interest: float 0.02
```

type hinting 지키지 않아도 실행은 되지만, 엉뚱한 결과 나올 수 있음  
개발자들에게 변수나 파라미터에 어떤 타입의 값을 넣어야 하는지 빠르게 파악할 수 있게 도와주는 역할
