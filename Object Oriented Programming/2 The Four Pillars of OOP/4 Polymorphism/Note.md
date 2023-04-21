# 다형성

2023.04.11

## 01. 클래스 다형성 I

예시)  
- 그림판 프로그램 만든다고 가정  
```python
class Rectangle:

class Circle:

class Paint:
```

<br/><br/>

## 02. 클래스 다형성 II
- Rectangle 클래스와 Circle 클래스에 동일한 메소드가 있어서 같은 값을 리턴한다면, Paint 클래스에서 이를 이용하여 메소드를 실행할 때 어느 클래스인지 신경쓰지 않고 오류 없이 실행할 수 있음
- 클래스의 메소드가 파라미터로 받는 값이 여러 클래스의 인스턴스를 가리키는 것을 다형성이 있다고 표현
- 다형성(Polymorphism): 하나의 변수가 서로 다른 클래스의 인스턴스를 가리킬 수 있는 성질

<br/><br/>

## 03. 상속없는 다형성의 한계
- 동일한 메소드를 포함하지 않는 다른 클래스의 인스턴스도 받아와서 실행하면 오류가 남
- 이를 방지하기 위해 isinstance 함수를 사용하여 필요한 메소드가 있는 클래스의 인스턴스만 실행하도록 조건문 짤 수는 있지만, 클래스가 많아지면 비효율적
- 효율적이고 안전하게 다형성을 적용할 방법은?

<br/><br/>

2023.04.12

## 04. 상속을 활용한 다형성 I(일반 상속)
어떤 변수가 여러 종류의 인스턴스를 가리키게 해서 다형성을 가지게 할 수 있음  
하지만 그 인스턴스에 어떤 메소드를 호출했을 때 인스턴스가 그 메소드를 갖고 있어야만 다형성이 성립됨  
그 메소드를 갖고 있지 않으면 에러가 발생함  
이걸 방지하려면 메소드 호출 전 isinstance 함수로 어떤 클래스의 인스턴스가 맞는지 미리 확인해야 함  
이때 클래스 종류가 많으면 isinstance 함수로 확인해야 하는 클래스 개수가 많아진다는 단점이 있음  
그걸 해결하기 위해, 같은 메소드를 갖는 여러 클래스가 상속받는 부모 클래스를 하나 만들면 됨  
부모 클래스는 메소드 이름만 정의하고, 내용은 pass로 한 뒤, 각 자식 클래스에서 오버라이딩 하면 됨  
자식 클래스의 인스턴스는 부모 클래스의 인스턴스이므로, isinstance 함수에서는 부모 클래스의 인스턴스가 맞는지만 확인하면 됨  


<br/><br/>

2023.04.13

## 05. 상속을 활용한 다형성 II(일반 상속의 문제점)

부모 클래스에서 메소드 정의만 하고 내용 없이 pass만 한 경우, 자식 클래스에서 오버라이딩을 해야 함  
만약에 어떤 자식 클래스에서 오버라이딩 없이 상속만 하면, 부모 클래스의 빈 내용의 메소드 상속받음  
그러면 나중에 isinstance 함수는 통과하는데 필요한 변수가 없어 실행했을 때 오류가 날 수 있음  
이를 방지하기 위해 무조건 오버라이딩 하도록 강제하는 방법은?

<br/><br/>

2023.04.14

## 06. 상속을 활용한 다형성 III(추상 클래스 개념)

### 추상 클래스
- 여러 클래스들의 공통점을 추상화해서 모아놓은 클래스  
- 추상 클래스로 정의하면 상속받는 자식 클래스들이 메소드를 오버라이딩 하도록 강제할 수 있음
- 추상 클래스로 정의하기 위해서는 abc 모듈로부터 ABC를 import 해서 상속받으면 됨
- ABC: Abstract Base Class, 추상화 기초 클래스
- 추상 클래스로는 인스턴스를 만들 수 없음

### 추상 메소드
- 자식 클래스 오버라이딩이 반드시 필요한 메소드
- 추상 메소드로 정의하기 위해서는 abc 모듈로부터 abstractmethod 데코레이터 함수를 import하여 사용하면 됨 

```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Shape 클래스를 상속받는 자식 클래스는 반드시 area 메소드를 오버라이딩 해야 함
```

<br/><br/>

## 07. 상속을 활용한 다형성 IV(추상 클래스 활용)
자식 클래스가 추상 클래스를 상속받고 추상 메소드를 오버라이딩 하지 않으면 실행 시 오류가 남  
ABC를 상속받고 추상 메소드를 1개 이상 가지고 있으면 정의에 의해 자식 클래스 또한 추상 클래스이기 때문
추상 메소드를 오버라이딩 하면 일반 클래스로 만들 수 있음  
오버라이딩의 방향을 제시하기 위해 추상 클래스는 type hinting을 해주는 게 좋음

<br/><br/>

## 08. 직각삼각형
```python
from math import sqrt
from abc import ABC, abstractmethod

class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass
    
    
class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """도형 인스턴스만 그림판에 추가한다"""
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("도형 클래스가 아닌 인스턴스는 추가할 수 없습니다!")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])

    
class RightTriangle(Shape):
    # 여기에 코드를 작성하세요
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height / 2
    
    def perimeter(self):
        return sqrt((self.base) ** 2 + (self.height) ** 2) + self.base + self.height
    
    
    

# 여기에 코드를 작성하세요
right_triangle_1 = RightTriangle(3, 4)
right_triangle_2 = RightTriangle(5, 12)
right_triangle_3 = RightTriangle(6, 8)

paint_program = Paint()

paint_program.add_shape(right_triangle_1)
paint_program.add_shape(right_triangle_2)
paint_program.add_shape(right_triangle_3)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())
```

1. 추상 클래스로 원하는 클래스의 조건(여기서는 클래스가 area, perimeter 메소드를 가져야한다는 조건)을 정한다.
2. 해당 추상 클래스의 인스턴스만 그림판에 추가한다.(추상 클래스로는 인스턴스를 바로 생성할 수 없으므로 실제로는 해당 추상 클래스의 자식 클래스의 인스턴스입니다, isinstance 함수를 배울 때 자식 클래스의 인스턴스는 부모 클래스의 인스턴스이기도 하다는 걸 배웠죠?)

<br/><br/>

2023.04.15

## 09. 추상 클래스 더 알아보기

### 1. 추상 클래스와 추상화!
- 추상 클래스는 서로 관련있는 **클래스들의 공통 부분을 묶어서** 추상화함
- 어떤 메소드에 특정 타입을 가지는 인스턴스가 파라미터로 들어와야 한다는 것 알려주기 위해 type hinting 기능 사용할 수 있음

### 2. 추상 클래스에도 일반 메소드를 추가할 수 있어요!
추상 클래스에 꼭 추상 메소드만 있어야하는 것은 아닙니다. @abstractmethod 데코레이터가 없는 일반적인 메소드가 있어도 상관없습니다. 이 메소드들 또한 자식 클래스가 물려받아 그대로 사용하거나 오버라이딩하여 사용할 수 있습니다. 하지만 차이점이 있다면
1. 반드시 오버라이딩해야하는 추상 메소드와 달리
2. 일반 메소드는 물려받은 그대로 사용할지, 오버라이딩할지를 자식 클래스에서 결정하는 것이구요.

### 3. 추상 메소드에도 내용을 채울 수 있습니다!
- 추상 메소드에 내용을 채워둔 뒤, 자식 클래스에서 super() 함수를 이용하여 상속받고 추가로 내용을 작성하여 사용할 수 있음
- 보통 추상 메소드에 내용을 쓸 때는 모든 자식 클래스에 해당하는 공통 내용을 써줍니다. 그리고 자식 클래스에서 추상 메소드를 오버라이딩하더라도 이렇게 미리 채워진 내용을 가져와서 재활용할 수 있습니다. 이는 super 함수를 사용하면 가능합니다.

### 4. 자식 클래스가 특정 변수를 갖도록 유도할 수 있어요!
- 부모 클래스에서 추상 메소드인 getter 메소드를 만들어서 자식 클래스가 그 getter 메소드의 대상이 되는 인스턴스 변수를 갖도록 유도할 수 있음

<br/><br/>

2023.04.16

## 10. 추상 클래스 다중 상속받기
- 일반 클래스와 다르게, 추상 클래스 여러 개를 다중 상속받는 것은 일반적으로 많이 쓰임
- 자식 클래스는 어차피 상속받는 추상 클래스들의 모든 추상 메소드를 오버라이딩해야 함
- 따라서 만약 부모 추상 클래스들 사이에 겹치는 메소드가 추상 메소드라면 문제없이 다중 상속을 할 수 있음

### 기억할 것
정리하자면 이 세 가지를 기억하셔야 합니다:
1. 추상 클래스 다중 상속은 일반적으로 많이 사용한다.
2. 다중 상속받는 부모 추상 클래스들이 추상 메소드로만 이뤄져 있으면 아무 문제 없이 다중 상속받을 수 있다.
3. 다중 상속받는 부모 추상 클래스들 간에 이름이 겹치는 일반 메소드가 있으면 일반 클래스를 다중 상속받을 때와 동일한 문제가 생길 수 있다.

<br/><br/>

2023.04.17

## 11. 함수/메소드 다형성

변수 하나가 다양한 클래스의 인스턴스를 가리킬 수 있는 것: 클래스 다형성  
함수와 메소드 다형성도 있음  
print 함수에 들어가는 파라미터 개수가 다양한 것처럼, 여러 가지 형태로 함수나 메소드를 호출하는 것  

### 1. 옵셔널(optional) 파라미터
- 기본값을 미리 지정해준 파라미터  
- 값을 전달받지 않은 경우 지정해둔 으로 처리  
- 파라미터 중 가장 뒤에 정의해야 함  

### 2. 파라미터 이름 명시  
- 함수를 호출할 때 파라미터 이름 표시
- 파라미터 이름과 함께 쓰면 함수 정의 시 파라미터 순서와 상관없이 쓸 수 있음

### 3. 개수가 확정되지 않은 파라미터  
- 개수가 정해지지 않은 파라미터들을 받아야 할 때 마지막 파라미터 이름 앞에 별표(\*)를 써줌
- 마지막 파라미터 변수에 튜플 담겨서 전달됨

<br/><br/>

2023.04.18

## 12. 간단한 주행 시뮬레이터 설명
예시) 여러 교통 수단(일반 자동차, 스포츠카, 자전거 등) 주행, 정지, 현재 속도 문자열 출력 등

<br/><br/>

## 13. 교통 수단

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        """추상 메소드 start: 교통 수단의 주행을 시작한다"""
        pass

    @property
    @abstractmethod
    def speed(self):
        """변수 _speed(교통 수단의 속도)에 대한 추상 getter 메소드"""
        pass

    def stop(self):
        """일반 메소드 stop: 교통 수단의 속도를 0으로 바꾼다"""
        self.speed = 0
```

<br/><br/>

## 14. 다양한 교통 수단
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        """추상 메소드 start: 교통 수단의 주행을 시작한다"""
        pass

    @property
    @abstractmethod
    def speed(self):
        """변수 _speed(교통 수단의 속도)에 대한 추상 getter 메소드"""
        pass

    def stop(self):
        """일반 메소드 stop: 교통 수단의 속도를 0으로 바꾼다"""
        self.speed = 0
        

class Bicycle(Vehicle):
    max_speed = 15 # 자전거의 최대 속도
    
    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= Bicycle.max_speed else 0

    def start(self):
        # 여기에 코드를 작성하세요
        print("자전거 페달 돌리기 시작합니다.")
        self._speed = Bicycle.max_speed / 3
        
    def __str__(self):
        # 여기에 코드를 작성하세요
        return f"이 자전거는 현재 {self.speed}km/h로 주행 중입니다."
        
class NormalCar(Vehicle):
    
    def __init__(self, speed, max_speed):
        self._speed = 0
        self.max_speed = max_speed
        
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0
    
    def start(self):
        # 여기에 코드를 작성하세요
        print("일반 자동차 시동겁니다.")
        self._speed = self.max_speed / 2

    def __str__(self):
        # 여기에 코드를 작성하세요
        return f"이 일반 자동차는 현재 {self._speed}km/h로 주행 중입니다."
    
    
class SportsCar(Vehicle):
    
    def __init__(self, speed, max_speed):
        self._speed = speed
        self.max_speed = max_speed
        
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0
               
    def start(self):
        # 여기에 코드를 작성하세요
        print("스포츠카 시동겁니다.")
        self._speed = self.max_speed
             
    def __str__(self):
        # 여기에 코드를 작성하세요
        return f"이 스포츠카는 현재 {self._speed}km/h로 주행 중입니다."
        

# 자전거 인스턴스
bicycle = Bicycle(0)        
    
# 일반 자동차 인스턴스
car = NormalCar(0, 100)

# 스포츠카 인스턴스
sports_car = SportsCar(0, 200)

# 정의한 인스턴스들을 모두 주행 시작시킨다
bicycle.start()
car.start()
sports_car.start()

# 자전거의 속도를 출력한다
print(bicycle)

# 자전거만 주행을 멈춰준다
bicycle.stop()

# 결괏값을 출력한다
print(bicycle)
print(car)
print(sports_car)
```

<br/><br/>

2023.04.19

## 15. 주행 시뮬레이터 만들기
```python
    def __str__(self):
        """갖고 있는 교통 수단들의 현재 속도를 문자열로 리턴한다"""
        res = ''
        
        for vehicle in self.vehicles:
            res += str(vehicle) + "\n"
        
        return res
```

\_\_str\_\_은 문자열 반환해야 함  
for문 안에 바로 return 넣으면 첫 번째 vehicle return 하고 끝나니까, res 만들어서 이어줘야 함

<br/><br/>

2023.04.20

## 16. 파이썬 EAFP 코딩 스타일과 다형성
```python
def add_shape(self, shape):
    if isinstance(shate, Shape):
        self.shapes.append(shape)
```
어떤 작업 전에 확인을 거치는 코딩 스타일: LBYL(Look Before You Leap, 뛰기 전에 살펴보라)
그와 상반되는 코딩 스타일: EAFP(Easier to Ask for Forgiveness than Permission, 허락보다 용서가 쉽다)  
try, except문  
일단 하고 문제가 발생하면 처리

<br/><br/>

2023.04.21

## 17. 다형성 퀴즈

질문 1  
해설: 단순히 여러 클래스에 같은 메소드 이름을 정의하는 방식으로 다형성을 적용하면 실수를 하기가 쉽고 코드의 유지 보수가 어려워집니다. 따라서 되도록 상속과 함께 다형성을 적용하는 것이 좋습니다.

질문 2  
해설: 추상 메소드를 정의할 때 그 안에 구현 내용을 쓸 수도 있습니다. 자식 클래스들이 공통적으로 사용해야할 내용을 추상 메소드에 미리 정의해두면, 추상 클래스를 상속받는 자식 클래스가 추상 메소드를 오버라이딩할 때, super 함수를 사용해 그 내용을 가져와서 쓸 수 있습니다.

질문 3  
해설: 옵셔널 파라미터를 사용하거나 파라미터 이름 앞에 \*를 붙이는 경우, 메소드 호출 시 전달하는 파라미터의 수가 다를 수 있습니다.
