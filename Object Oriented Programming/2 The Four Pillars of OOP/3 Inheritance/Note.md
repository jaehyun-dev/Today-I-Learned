# 상속

2023.04.03

## 01. 중복되는 코드
서로 다른 클래스에서 같은 변수나 메소드를 쓰는 경우가 있음  
상속을 이용하면 반복되는 내용을 한 번만 써도 됨  
효율적으로 코드를 작성할 수 있음  

<br/><br/>

2023.04.04

## 02. 상속이란?
- 두 클래스 사이에 부모-자식 관계를 설정하는 것  
- A클래스가 B클래스에 포함되면 B는 부모 클래스, A는 자식 클래스로 상속관계를 설정할 수 있음  
- 자식 클래스는 부모 클래스의 모든 변수와 메소드를 물려받음  

<br/><br/>

## 03. 부모 클래스 정의하기
- 서로 다른 클래스에서 공통되는 부분을 부모 클래스로 정의할 수 있음  
- 공통되는 부분이 부모 클래스, 공통되는 부분을 상속받는 클래스가 자식 클래스

<br/><br/>

## 04. 상속 I(부모로부터 물려받기)
```python
class Employee:
  """직원 클래스"""
  

class Cashier(Employee):
  """캐셔 클래스"""

class DeliveryMan(Employee):
  """배달원 클래스"""
```  
자식 클래스 이름 뒤에 괄호를 쓰고, 괄호 안에 상속할 부모 클래스 이름을 적으면 됨  
help() 함수로 클래스의 상속 관계와 세부 내용을 파악할 수 있음  
파이썬에서 모든 클래스는 builtins.object 클래스를 자동으로 상속받는 자식 클래스  

<br/><br/>

## 05. 상속과 관련된 메소드와 함수들

### mro 메소드
```python
class Employee:
    """직원 클래스"""
    raise_percentage = 1.03
    company_name = "코드잇 버거"

    
    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name
        self.wage = wage


    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self.wage *= Employee.raise_percentage


    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class Cashier(Employee):
    pass


class Manager(Employee):
    pass

print(Cashier.mro())
```
mro 메소드를 호출하면 클래스가 상속하는 부모 클래스를 볼 수 있음
```python
[<class '__main__.Cashier'>, <class '__main__.Employee'>, <class 'object'>]
```

### isinstance 함수
- 어떤 인스턴스가 주어진 클래스의 인스턴스인지를 알려줌
1. 첫 번째 파라미터에는 검사할 인스턴스의 이름
2. 두 번째 파라미터에는 기준 클래스의 이름  

을 넣고 실행하면 그 인스턴스가 해당 클래스의 인스턴스인지를 불린 값(True 또는 False)으로 리턴함

```python
# 인스턴스를 생성한다
young = Cashier("강영훈", 8900)

print(isinstance(young, Cashier)) # 출력: True
print(isinstance(young, DeliveryMan)) # 출력: False
print(isinstance(young, Employee)) # 출력: True
```
상속 관계에 있는 두 클래스가 있을 때, 자식 클래스로 만든 인스턴스는 부모 클래스의 인스턴스이기도 함(다형성 핵심 원리)

### issubclass 함수
- 한 클래스가 다른 클래스의 자식 클래스인지를 알려줌
1. 첫 번째 파라미터로 검사할 클래스의 이름
2. 두 번째 파라미터에는 기준이 되는 부모 클래스의 이름

을 넣고 실행하면 클래스 상속 관계 불린 값으로 리턴함

```python
print(issubclass(Cashier, Employee)) # 출력: True
print(issubclass(Cashier, object)) # 출력: True
print(issubclass(Manager, Employee)) # 출력: True
print(issubclass(Employee, list)) # 출력: False
```

<br/><br/>

2023.04.06

## 06. 상속 II(오버라이딩)  

### 오버라이딩
- 부모 클래스를 상속한 후, 각 클래스에 맞게 수정하는 것  
- 자식 클래스에서, 물려받은 같은 이름의 메소드(또는 변수)를 내용을 바꿔 정의하면 됨

### super 함수
- 자식 클래스에서 부모 클래스의 메소드를 사용하고 싶을 때 쓰는 함수
- super 함수로 부모 클래스의 메소드를 사용할 때는 self 파라미터를 넘겨줄 필요 없음

```python
class Employee:
    def __init__(self, name, wage):
        self.name = name
        self.wage = wage

class Cashier(Employee):
    def __init__(self, name, wage, number_sold):
        super().__init__(name, wage)
        self.number_sold = number_sold
```

<br/><br/>

2023.04.07

## 07. 상속 III(mro)

### mro(Method Resolution Order, 메소드 검색 순서) 메소드
- 클래스가 상속받는 부모 클래스들이 순서대로 담긴 리스트를 리턴

자식 클래스는 물려받은 메소드와 오버라이딩한 메소드 둘 다 있는데 어떻게 오버라이딩한 메소드가 호출될까?

메소드를 호출하면 파이썬이 mro에 나와있는 순서대로 메소드를 탐색함  
따라서 mro에서 앞에 나오는 자식 클래스의 메소드가 뒤에 나오는 부모 클래스의 같은 이름의 메소드보다 먼저 찾아져서 호출됨  

mro에 나와있는 순서대로, 메소드 검색 방향은 자식 클래스부터 부모 클래스 방향으로 검색  
따라서 자식 클래스와 부모 클래스에 같은 이름의 메소드가 있어도, 자식 클래스의 오버라이딩한 메소드를 사용할 수 있는 것

<br/><br/>

2023.04.08

## 08. 상속 IV(기능 추가하기)
클래스에서 중복되지 않았던 그 자체만의 원래 내용은 상속받기 전과 똑같이 정의해주면 됨

<br/><br/>

2023.04.09

## 09. 상속 정리
- 여러 개의 클래스에서 공통되는 부분이 있으면 부모 클래스를 만들고 그 클래스를 상속하면 됨  
- 상속 후 클래스에 맞게 오버라이딩 해줄 수 있음
- 중복되지 않았던 자신만의 메소드와 변수는 똑같이 추가하면 됨
- 상속을 적용하면 더 적은 코드로 비슷한 특징을 가진 새로운 클래스를 편하게 만들 수 있음

<br/><br/>

## 10. 배달도 해 주세요
```python
class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03
    
    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name
        self.wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self.wage *= self.raise_percentage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name
```
```python
class DeliveryMan:
    """배달원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage, on_standby):
        self.name = name
        self.wage = wage
        self.on_standby = on_standby

    def raise_pay(self):
        """시급을 인상한다"""
        self.wage *= self.raise_percentage

    def deliver(self, address):
        """배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 설명 메시지를 출력한다"""
        if self.on_standby:
            print(address + "로 배달 나갑니다!")
            self.on_standby = False
        else:
            print("이미 배달하러 나갔습니다!")

    def back(self):
        """배달원을 복귀 처리한다"""
        self.on_standby = True

    def __str__(self):
        return DeliveryMan.company_name + " 배달원: " + self.name
```
```python
class DeliveryMan(Employee):
    def __init__(self, name, wage, on_standby):
    super().__init__(name, wage)
    self.on_standby = on_standby
    
    def __str__(self):
    return DeliveryMan.company_name + " 배달원: " + self.name
    
    def deliver(self, address):
    """배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 메시지를 출력한다"""
    if self.on_standby:
        print(address + "로 배달 나갑니다!")
        self.on_standby = False
    else:
        print("이미 배달하러 나갔습니다!")

    def back(self):
        """배달원을 복귀 처리한다"""
        self.on_standby = True
```

<br/><br/>

## 11. 계좌는 다 계좌
```python
class BankAccount:
    # 여기에 코드를 작성하세요
    def __init__(self, name, balance):
        """모든 인스턴스 변수의 초기값을 설정한다"""
        self.name = name
        self.balance = balance
    
    def withdraw(self, amount):
        """돈을 출금한다"""
        self.balance -= amount
        
    def deposit(self, amount):
        """돈을 입금한다"""
        self.balance += amount
    
    def __str__(self):
        """계좌의 정보를 문자열로 리턴한다."""
        return "{}님의 계좌 예치금은 {}원입니다".format(self.name, self.balance)
        
class CheckingAccount(BankAccount):
    # 여기에 코드를 작성하세요
    """자유 입출금 계좌 클래스"""
    def __init__(self, name, balance, max_spending):
        """모든 인스턴스 변수의 초기값을 설정한다"""
        super().__init__(name, balance)
        self.max_spending = max_spending
        
    def use_check_card(self, amount):
        """한 회 사용 한도 초과 이하인 금액을 체크 카드 결제 시 예치금을 줄인다"""
        if amount <= self.max_spending:
            self.balance -= amount
        else:
            print("{}님의 체크 카드는 한 회 {} 초과 사용 불가능합니다".format(self.name, self.max_spending))

class SavingsAccount(BankAccount):
    # 여기에 코드를 작성하세요
    def __init__(self, name, balance, interest_rate):
        """모든 인스턴스 변수의 초기값을 설정한다"""
        super().__init__(name, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        """이자를 더한다"""
        self.balance *= (1+self.interest_rate)
```

<br/><br/>

## 12. 다중 상속
- 하나의 자식 클래스가 여러 부모 클래스를 상속받는 것  
- 클래스 이름 뒤에 괄호를 열고 상속받고 싶은 부모 클래스를 콤마(,)로 구분하여 넣어주면 됨  
- 상속받는 모든 클래스로부터 변수와 메소드를 물려받음
- super()을 썼을 때 어느 부모 클래스를 말하는지 알 수 없다는 게 다중 상속의 단점

<br/><br/>

2023.04.11

## 13. 다중 상속의 위험성
- 다중 상속을 받았을 때, 여러 부모 클래스에서 같은 이름의 메소드나 변수가 있다면 어느 클래스의 메소드가 실행될지 애매함
- mro 함수를 써서 메소드를 찾는 순서를 확인하면, 앞의 순서대로 클래스와 메소드를 검색하여 사용함
- 그러나 mro는 클래스 간의 상속 관계에 따라 변할 수 있음
- Java는 이런 문제 피하기 위해 다중 상속 지원하지 않고, 하나의 부모 클래스만 상속 가능
- Python에서 다중 상속을 할 때 해결 방법
    - 부모 클래스끼리 같은 이름의 메소드를 갖지 않도록 하기
    - 같은 이름의 메소드는 자식 클래스에서 오버라이딩

<br/><br/>

## 14. 상속 퀴즈
질문 1  
해설: 상속 관계는 연속적으로 있을 수 있습니다. 한 클래스가 다른 클래스의 자식 클래스이면서 또다른 클래스의 부모 클래스일 수 있습니다.

질문 2  
해설: 자식 클래스가 부모 클래스가 갖는 모든 인스턴스 변수를 갖고 싶으면(갖고 있는 것이 좋은 상속입니다) 중복되는 코드를 줄이기 위해서 부모 클래스의 \_\_init\_\_ 메소드를 그대로 갖고와서 사용하는 것이 좋지만, 굳이 그렇게 하지 않아도 에러는 나지 않습니다.

질문 3  
해설: 부모 클래스를 참조할 때의 애매모호함 때문에 되도록 다중 상속을 하지 않는 것이 바람직합니다.
