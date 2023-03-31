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
