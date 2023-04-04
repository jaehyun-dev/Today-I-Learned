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
