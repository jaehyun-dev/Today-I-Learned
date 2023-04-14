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
