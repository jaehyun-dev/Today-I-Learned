# 캡슐화

2023.03.27

## 01. 캡슐화의 필요성

### 캡슐화의 정의
1. 객체의 일부 구현 내용에 대한 외부로부터의 직접적인 액세스를 차단하는 것
2. 객체의 속성과 그것을 사용하는 행동을 하나로 묶는 것

<br/><br/>

2023.03.28

## 02. 객체 내부를 숨기는 법

캡슐화의 첫 번째 정의  
- 객체의 일부 구현 내용에 대한 외부로부터의 직접적인 액세스를 차단하는 것

사람들이 마음대로 보면 안 되는 민감한 개인정보 등, 수정하면 안 되는 정보 등  

변수나 메소드 이름 앞에 언더바(\_) 두 개를 붙이면, 클래스 밖에서 접근이 불가능해짐  
변수나 메소드를 클래스 밖에서 호출해도 실행되지 않고 오류가 뜸  
실제로는 있지만 없는 것처럼

```python
class Citizen:

  def __init__(self, name, age, resident_id):
    self.name = name
    self.__age = age
    self.__resident_id = resident_id

kyusik = Citizen("최규식", 25, "12345678")
print(kyusik.__resident_id)
```
```
AttributeError: 'Citizen' object has no attribute '__resident_id'
```

<br/><br/>

2023.03.29

## 03. 밑줄 두 개(__)와 특수 메소드들

\_\_init\_\_, \_\_str\_\_ 메소드 등 이름 앞뒤에 모두 밑줄 2개(__)가 있으면 일반 메소드와 동일하게 사용할 수 있음  
__resident_id 처럼 이름 앞에만 밑줄 2개가 있으면 외부에서 접근할 수 없음


<br/><br/>

2023.03.30

## 04. 객체의 메소드를 통해 변수 접근하기 I

숨겨진 변수는 클래스 밖에서 접근 불가. 접근할 수 있는 메소드를 따로 만들어 해결할 수 있음.  
외부에서 접근 불가능한 변수나 메소드에 접근할 수 있는 메소드를 만드는 것  
= 캡슐화의 2번째 정의: 객체의 속성과 그것을 사용하는 행동을 하나로 묶는 것  

```python
class Citizen:
  drinking_age = 19  # 음주 가능 나이

  def __init__(self, name, age, resident_id):
    self.name = name
    self.__age = age
    self.__resident_id = resident_id
```
\_\_age, \_\_resident_id에는 접근할 수 없음  
이때 클래스 안에  
```python
  def can_drink(self):
    return self.__age > Citizen drinking_age
```  
이렇게 메소드를 만들어주면 클래스 밖에서도 \_\_age에 관하여 알 수 있음

<br/><br/>

2023.03.31

## 05. 객체의 메소드를 통해 변수 접근하기 II

변수의 값을 읽는 메소드: getter 메소드  
변수의 값을 설정하는 메소드: setter 메소드  

숨긴 변수에 대해서 getter / setter 메소드 꼭 만들 필요는 없다  
민감한 정보, 바뀌면 안 되는 정보 등은 만들면 안 됨  

### 캡슐화 정리
1. 클래스 밖에서 접근 못하게 할 변수, 메소드 정하기
2. 변수나 메소드 이름 앞에 언더바(\_) 2개 붙이기
3. 변수에 간접 접근할 수 있게 메소드 추가하기
    - getter/setter 또는 다른 용도의 메소드

<br/><br/>

2023.04.01

## 06. 객체의 메소드를 통해 변수 접근하기 III

setter 메소드는 파라미터로 전달된 값이 적절한지 점검하는 코드를 넣는 게 좋음  
그렇지 않으면 객체의 속성이 엉뚱한 값을 갖게 될 수도 있기 때문


<br/><br/>

2023.04.02

## 07. 여기서 잠깐! 파이썬의 캡슐화
파이썬에서 캡슐화 하기 위해 변수나 메소드 이름 앞에 밑줄 2개를 붙이면, 파이썬은 그 앞에 추가적으로 "\_클래스 이름"을 덧붙여 이름을 바꿔버림  
이를 네임 맹글링(name mangling)이라고 함  
바뀐 이름으로 클래스 밖에서도 변수에 접근할 수 있음  
파이썬은 언어 차원에서 캡슐화를 지원하지 않음  
Java는 private 키워드를 통해 완벽히 캡슐화할 수 있음  

<br/><br/>

## 08. 캡슐화와 파이썬 문화
파이썬 개발자들은 변수나 메소드 이름 앞에 밑줄(\_) 한 개를 붙여서 다른 개발자에게 외부에서 접근하지 말라고 알려줌  
이 코드를 보는 다른 개발자들은 암묵적으로 접근하지 않는다는 규칙을 지킴  
강제적인 규칙은 아니고 믿음에 기반한 코드 문화  
만약 규칙 어기고 접근해도 코드는 잘 실행 됨  
그러나 만약 무시하고 코드를 계속 발전해서 작성하다 보면, 어느 순간 문제가 생길 수 있음  

<br/><br/>

## 09. 데코레이터를 사용한 캡슐화
@property, @method.setter 데코레이터를 이용해 getter, setter 메소드를 만들 수 있음  

<br/><br/>

## 10. 객체를 사용할 땐 최대한 메소드로
변수 이름을 직접 가져다 쓰는 대신 메소드를 사용하면, 상황이 변했을 때 수정하고 코드를 유지 보수하기가 쉬워짐  
변수 직접 사용 최소화 => 유지보수 쉬운 코드  

<br/><br/>

## 11. 신용 카드 정보 조회하기 I

### 모범 답안
완성된 CreditCard 클래스의 전체 코드를 보여드릴게요.
```python
class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    # 모든 인스턴스 변수 이름 앞에 __를 붙여서 외부 접근을 막는다
    def __init__(self, name, password, payment_limit):
        self.__name = name
        self.__password = password
        self.__payment_limit = payment_limit

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_password(self):
        return "비밀 번호는 볼 수 없습니다"

    def set_password(self, new_password):
        self.__password = new_password

    def get_payment_limit(self):
        return self.__payment_limit

    def set_payment_limit(self, new_payment_limit):
        if new_payment_limit >= 0 and new_payment_limit <= CreditCard.MAX_PAYMENT_LIMIT:
            self.__payment_limit = new_payment_limit
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해 주세요!")
```

<br/><br/>

## 12. 신용 카드 정보 보호하기 II

### 모범 답안
```python
class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    # 모든 인스턴스 변수를 _를 통해서 외부 접근을 막는다
    def __init__(self, name, password, payment_limit):
        self.name = name
        self._password = password
        self._payment_limit = payment_limit

    @property
    def password(self):
        return "비밀 번호는 볼 수 없습니다"

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def payment_limit(self):
        return self._payment_limit
    
    @payment_limit.setter
    def payment_limit(self, new_payment_limit):
        if new_payment_limit >= 0 and new_payment_limit <= CreditCard.MAX_PAYMENT_LIMIT:
            self._payment_limit = new_payment_limit
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해 주세요!")
```

<br/><br/>

## 13. 캡슐화 퀴즈

질문 1  
해설: 밑줄 두 개(\_\_)를 변수의 이름 앞에 붙이면 그 변수의 이름은 네임 맹글링(name mangling)됩니다. 그리고 네임 맹글링된 후의 새 이름을 사용하면 외부로부터 그 변수에 접근할 수 있기 때문에 완벽하게 접근을 막을 수 있는 건 아닙니다.

질문 2  
해설: 캡슐화를 적용하면 민감한 정보를 외부에 노출하지 않을 수 있고 객체 내부의 속성을 항상 안정적으로 유지할 수 있습니다. 캡슐화를 적용하지 않으면 반대의 상황들이 발생하겠죠?

질문 3  
해설: 정답은 보기 1입니다. 가장 파이썬 문화에 부합하는 캡슐화는 getter/setter 메소드를 직접 정의하는 것이 아니라 @property 데코레이터를 사용하는 것입니다. @property 데코레이터를 사용하면 마치 직접 변수에 접근하는 것 같은 방식으로(실제로는 그것이 아니라 getter/setter 메소드가 실행되는 것이지만) 변수의 값을 읽을 수 있습니다.
