# 6 추상 자료형

23.01.11

## 01. 기능 vs 구현

삽입 연산(insert operation)의 기능과 구현?  

### 기능
연산이 "무엇"을 하는지
- 삽입 연산 기능: "순서 데이터에서 원하는 위치에 데이터를 저장"

### 구현
기능을 "어떻게" 하는지
- 동적 배열 삽입: 데이터 삽입할 때 인덱스와 인덱스 뒤에 있는 모든 인덱스를 뒤로 한 칸씩 뒤로 미룬 뒤 빈 인덱스에 데이터 삽입
- 링크드 리스트 삽입: 저장하려는 위치 바로 전 노드에 접근한 후, 앞 뒤 노드들의 레퍼런스들을 수정해서 원하는 위치에 데이터 삽입

<br/><br/>

## 02. 추상화

### 추상화
구현을 몰라도 기능만 알면 프로그래밍을 할 수 있게 해주는 개념

```python
def insert(data_type, index, element):
    """자료형 data_type의 위치 index에 데이터 element를 삽입해주는 함수"""
```

개발자들이 이 함수를 사용하고 싶으면 이 함수가 뭘 하는지만 알면, 어떻게 구현돼있는지 몰라도 충분히 사용할 수 있음  
이 함수의 기능만 알아도 사용할 수 있는 것  
이를 "추상화를 했다"고 표현함  
추상화를 하면 이미 쓴 코드를 재활용하고 개발자들끼리 협력하기 쉬워짐  
자료구조 사용할 때에도 추상화 많이 사용함

### 추상 자료형
- 자료 구조를 추상화 한 것
- 데이터를 저장/사용할 때 기능만 생각
- 구현은 신경쓰지 않아도 됨

<br/><br/>

## 03. 추상 자료형 vs 자료 구조

### 추상 자료형(Abstract Data Type, ADT)  
자료구조를 추상화한 개념  

#### 리스트
- 데이터간 순서 관계를 유지할 수 있다
- 접근 연산: 특정 위치에 있는 데이터를 가지고 오거나 수정한다
- 탐색 연산: 특정 조건을 만족하는 데이터를 찾는다
- 삽입 연산: 특정 위치에 새로운 데이터를 저장한다
- 삭제 연산: 특정 위치에 있는 데이터를 지운다

리스트는 대표적인 추상 자료형  
리스트는 데이터에 접근, 탐색, 삽입, 삭제를 할 수 있음  
데이터에 무엇을 하고 싶은지(기능) 포함됨, 어떻게(구현)은 포함되지 않음

### 자료 구조

#### 동적 배열
- 데이터를 메모리에 순서대로 그리고 연속적으로 저장한다
- 접근 연산: 인덱스 주소를 한 번에 계산해서 메모리에 접근한다
- 탐색 연산: 가장 앞 인덱스부터 선형적으로 모든 데이터를 확인한다
- 삽입 연산: 인덱스 뒤 데이터를 한 칸씩 뒤로 밀고, 데이터를 저장한다
- 삭제 연산: 데이터를 지우고 뒤 인덱스들을 하나씩 앞으로 옮겨서 저장한다

자료구조는 정확히 어떻게 기능을 할 것인지에 대해 구현을 묶어놓은 개념  
동적 배열은 리스트의 모든 연산들을 갖고 있는 자료 구조  
이때 리스트는 동적 배열로 구현할 수 있다고 표현함  
리스트를 구현하는 자료 구조가 동적 배열만 있는 것은 아님  
링크드 리스트도 접근, 탐색, 삽입, 삭제 연산이 다 있으므로 리스트를 구현하는 자료 구조  

따라서 리스트라는 추상 자료형을 동적 배열이라는 자료 구조 또는 링크드 리스트라는 자료 구조로 구현할 수 있음  
둘 중 어느 것을 사용해야 할지는 상황에 따라 다름  

### 추상 자료형을 알아야 하는 이유
프로그래밍을 할 때 바로 자료 구조를 떠올리는 것보다 추상 자료형을 떠올리는 게 편함  
큰틀에서 생각할 때 도움이 됨  
추상 자료형을 생각하면 코드의 흐름에 집중할 수 있다!

<br/><br/>

## 04. 추상 자료형 vs 자료 구조 현실 비유

### 추상 자료형 vs 자료 구조 현실 비유
추상 자료형과 자료 구조의 차이를 좀 더 현실에 가까운 예시를 들어서 설명해 볼게요.

사실 우리는 프로그래밍할 때 말고 실생활에서도 많은 물건들이나 개념들을 추상화해서 사용합니다. 남녀노소 누구나 가지고 있는 “핸드폰”도 추상화의 한 예시인데요.

“핸드폰”이라는 개념을 어떻게 정의할 수 있을까요? 주변을 보면 핸드폰인 많은 물건들은 있지만 딱 “핸드폰은 X다”라고 하기 쉽지가 않습니다. 한 번 핸드폰의 가장 기본적인 기능들을 정리해서 핸드폰이 뭔지 간단하게 정의해볼게요.

핸드폰은:

특징
- 전기선 없이 이곳저곳 들고 다닐 수 있다

행동
- 전화를 걸 수 있다
- 전화를 받을 수 있다
- 문자 메시지를 보낼 수 있다
- 문자 메시지를 받을 수 있다

이런 기능들을 갖는 것입니다. 핸드폰이 뭔지 물어봤을 때 딱 정확히 손가락으로 가리켜서 “이거다”라고 하기는 힘들지만 “저 기능들을 갖는 어떤 것이다”라고는 얘기할 수 있는 거죠.

조금 다르게 생각해보면 저 기능들을 갖는 존재들을 다 핸드폰이라고도 할 수도 있습니다. 기술적으로 어떻게 구현했는지는 기계가 핸드폰인지 아닌지와 전혀 상관이 없습니다. 그러니까 핸드폰은 구현은 없고 기능으로만 정의한 개념인 추상 자료형과 비슷한 거죠.

추상 자료형을 핸드폰에 비유할 수 있으면, 자료 구조는 뭐에 비유할 수 있을까요? 자료 구조는 핸드폰의 기능들을 가지고 있는 기계 모델들에 비유할 수 있습니다.

아이폰 6s, 삼성 갤럭시 S10, LG v50 이렇게 특정 방식에 의해서 전화와 문자를 보내거나 받을 수 있는 것들이 자료 구조에 해당하는 거죠.

실제로 어떤 모델 또는 회사인지에 따라 부수적으로 갖는 기능들도 다를 수도 있고 전화를 거는 구체적인 방식이 모두 다를 수는 있긴 합니다. 하지만 핸드폰의 모든 기능들을 모두 갖고 있습니다. 실질적으로 “핸드폰”의 기능을 모두 할 수 있으면, 그러니까 핸드폰을 “구현”하고 있으면 핸드폰이라고 부르고 사용할 수 있는 거죠.

여러분들은 평소에 여러분의 핸드폰에 대해 어떤 식으로 얘기를 하시나요? “내 핸드폰 어딨지?”, “너 핸드폰 번호 뭐야?” 이런 식으로 실제 사용하는 핸드폰의 모델명 대신, 추상화해서 핸드폰이라고 표현하면서 사용하는 경우가 많을 텐데요. 물론 “내 갤럭시 S10” 어딨지 이런 식으로 구체적인 모델 이름을 사용해도 틀린 건 아니지만 일반적으로 그렇게 얘기하지는 않죠?

### 컴퓨터 과학에서 추상 자료형
추상 자료형의 개념도 똑같습니다. 추상 자료형 리스트에 대해서 생각해봅시다.

특징
- 데이터 사이 순서 관계를 유지할 수 있다

연산
- 접근 연산: 특정 위치에 있는 데이터를 가지고 오거나 수정할 수 있다
- 탐색 연산: 특정 조건을 만족하는 데이터를 찾을 수 있다
- 삽입 연산: 특정 위치에 새로운 데이터를 저장해줄 수 있다
- 삭제 연산: 특정 위치에 데이터를 지울 수 있다

핸드폰이라는 추상적인 개념과 똑같이 이런 특징과 연산들을 가지는 존재를 “리스트”라고 부르는 겁니다. 여러분들이 핸드폰을 찾을 때 “내 핸드폰 어딨지“ 이런 식으로 얘기하는 것처럼, 데이터를 저장하고 사용할 때도 “리스트를 사용해야겠다!”이런 식으로 추상적으로 얘기할 수 있는 거죠.

### 추상 자료형 vs 자료 구조 뭐가 더 중요할까?
추상 자료형과 자료 구조는 뭐가 더 중요한 건 없습니다. 그냥 서로 다른 개념이죠. 기능을 중점적으로 얘기하고 싶을 때나, 흐름을 생각할 때와 같이 구현에 집중할 필요가 없을 때 추상 자료형을, 그리고 코드의 성능을 분석하거나 최적화 시켜야 될 때나(성능을 최대로 끌어올리고 싶을 때) 자료 구조를 중심적으로 생각하면 됩니다.

핸드폰이라는 개념과 단어가 우리한테 굉장히 중요하고 널리 쓰이는 거 만큼, 정확히 어떤 핸드폰을 쓰는지, 그러니까 아이폰 6s, 삼성 갤럭시 S10, LG v50 중에 어떤 모델을 쓰는지도 많은 사람들한테 굉장히 중요합니다.

그러니까 아이폰 6s보다는 아이폰 11 pro가 훨씬 빠르고, LG v50는 화면이 두 개고, 삼성 갤럭시 노트는 화면이 크고… 이런 구체적인 핸드폰의 세부 구현들도 핸드폰이라는 개념만큼 중요하다는 말이죠.

컴퓨터 과학을 공부하는 우리에게 추상 자료형들과 자료 구조들의 개념이 모두 중요한 거랑 비슷하죠.

<br/><br/>

## 05. 리스트 개념  

파이썬  
- 추상화가 많이 된 고수준 언어
- 개발자들이 구현보다 기능에 집중할 수 있게 해줌
- 많은 자료형 이름이 추상 자료형!
- 파이썬 자료형 list는 구현을 몰라도 기능만 알고 사용할 수 있음!

```python
# 파이썬 리스트 생성
trending = []

# 특정 위치에 데이터 삽입
trending.insert(0, "연예인 A씨")
trending.insert(1, "잠실 콘서트")
trending.insert(2, "한국 휴일 수")
trending.insert(3, "추석 음식")

print(trending)  # 리스트 출력
# ['연예인 A씨', '잠실 콘서트', '한국 휴일 수', '추석 음식']


# 괄호를 이용한 인덱스 접근
print(trending[0])  # 연예인 A씨
print(trending[1])  # 잠실 콘서트

trending[2] = 4

print(trending)
# ['연예인 A씨', '잠실 콘서트', 4, '추석 음식']


# in 을 이용한 탐색
print("연예인 A씨" in trending)  # True
print("연예인 B씨" in trending)  # False


# del 을 이용한 삭제
del trending[0]

print(trending)
# ['잠실 콘서트', 4, '추석 음식']
```

추상 자료형으로서 리스트의 핵심은, 개발자들이 리스트를 떠올릴 때 이걸 정확히 어떻게 구현하고 내부적으로 어떤 자료 구조를 어떻게 사용했는지 전혀 몰라도 됨. 리스트라는 게 무엇을 할 수 있는지, 기능들만 알고 사용할 수 있음

<br/><br/>

## 06. 리스트 구현

리스트 구현은 동적 배열 또는 링크드 리스트로 할 수 있음  
둘 중 어느 걸 사용해야 할까?

|             |     동적 배열    | 더블리 링크드 리스트 |
|:-----------:|:----------------:|:--------------------:|
|     접근    |      $O(1)$      |        $O(n)$        |
|     탐색    |      $O(n)$      |        $O(n)$        |
| 접근 + 삽입 |      $O(n)$      |        $O(n)$        |
| 접근 + 삭제 |      $O(n)$      |        $O(n)$        |
|             |                  |                      |
|  맨 앞 삽입 |      $O(n)$      |        $O(1)$        |
|  맨 앞 삭제 |      $O(n)$      |        $O(1)$        |
|  맨 뒤 삽입 | 분할 상환 $O(1)$ |        $O(1)$        |
|  맨 뒤 삭제 | 분할 상환 $O(1)$ |        $O(1)$        |

어떤 기능을 많이 사용할지를 생각해야 함  
접근을 많이 하고 싶은지, 맨 앞에 삽입을 많이 사용할 것인지  
각 자료구조에서 많이 사용할 연산의 시간 복잡도 비교해서 고르면 됨

접근을 많이 하고 싶을 때, 동적 배열은 $O(1)$, 더블리 링크드 리스트는 $O(n)$이기 때문에 이 경우에는 동적 배열을 사용하면 됨  
가장 앞에 데이터를 계속 삽입하고 싶다면, 동적 배열 사용하면 $O(n)$, 링크드 리스트 사용하면 $O(1)$이기 때문에 링크드 리스트를 사용하면 됨

파이썬 리스트는 내부적으로 동적 배열로 구현되어 있음  

<br/><br/>

23.01.12

## 07. 큐 개념

### 큐(Queue)  
- 리스트와 마찬가지로 데이터 간 순서를 약속하는 추상자료형
- 한국어로 대기열이라고도 함
- 영국에서는 사람들이 줄을 서 있을 때 이 줄을 큐라고도 함
- 마트에서 물건을 살 때: 맨 앞 사람부터 계산하고 나가고, 맨 뒤부터 줄을 섬
- 이처럼 큐는 데이터를 삭제할 떄는 맨 앞에서 삭제하고, 삽입할 때는 가장 뒤에서만 삽입해주는 추상자료형
- FIFO: First In First Out
- 즉, 가장 먼저 들어온 데이터가 가장 먼저 삭제됨

### 큐의 기능
- 데이터 간 순서 관계를 유지할 수 있다
- 맨 뒤 데이터 추가
- 맨 앞 데이터 삭제
- 맨 앞 데이터 접근

### deque
- 파이썬에서는 deque라는 자료형을 사용해서 큐를 쓸 수 있다  
- Doubly-ended-queue의 약자
- 양면큐라는 뜻
- 맨 앞과 뒤에 데이터를 삽입하고 삭제할 수 있게 해주는 자료형

```python
# deque는 파이썬 collections 모듈에서 가지고 온다
from collections import deque

queue = deque()

# 큐의 맨 끝에 데이터 삽입
queue.append("태호")
queue.append("현승")
queue.append("지웅")
queue.append("동욱")
queue.append("신의")

print(queue)  # 큐 출력
# deque(['태호', '현승', '지웅', '동욱', '신의'])


# 큐의 가장 앞 데이터에 접근
print(queue[0])  # 태호


# 큐 맨 앞 데이터 삭제
print(queue.popleft())  # 태호
print(queue.popleft())  # 현승
print(queue.popleft())  # 지웅

print(queue)  # 큐 출력
# deque(['동욱', '신의'])
```

리스트와 마찬가지로 append를 사용해서 맨 뒤에 데이터를 삽입할 수 있음  
파이썬 자료형들은 같은 행동을 하는 연산들은 메소드 이름도 똑같으니 편하게 쓸 수 있음  

[0] 인덱스 접근으로 큐의 가장 앞 데이터에 접근할 수 있음

popleft() 메소드로 맨 앞 데이터를 삭제함과 동시에 삭제하는 데이터를 return할 수 있음

삽입, 접근, 삭제 이 세 가지 연산을 할 수 있으면 queue  
이 기능을 사용하고 싶으면 복잡한 내부 구현을 떠올릴 필요 없이 queue를 떠올리면 되고,  
파이썬에서 queue를 사용하고 싶으면 deque 자료형을 사용하면 됨

<br/><br/>

23.01.13

## 08. 큐 구현

### 큐(Queue)
- 데이터 간 순서 관계를 유지할 수 있다
- 맨 뒤 데이터 추가
- 맨 앞 데이터 삭제
- 맨 앞 데이터 접근

### 큐 구현
- 동적 배열, 링크드 리스트 두 자료구조로 구현할 수 있음
- 어떤 게 더 효율적일까?

|            |     동적 배열    | 더블리 링크드 리스트 |
|:----------:|:----------------:|:--------------------:|
| 맨 앞 삭제 |      $O(n)$      |        $O(1)$        |
| 맨 뒤 삽입 | 분할 상환 $O(1)$ |        $O(1)$        |
| 맨 앞 접근 |      $O(1)$      |        $O(1)$        |

큐를 구현할 때 링크드 리스트는 모든 연산을 $O(1)$으로 할 수 있지만, 동적 배열은 맨 앞 삭제 연산에 $O(n)$이 걸리므로 링크드 리스트가 더 효율적임  
파이썬에서 queue로 사용했던 자료형 deque도 내부적으로는 더블리 링크드 리스트로 구현되어 있음

<br/><br/>

## 09. 서비스 센터 문의 처리

### 실습 설명
고조선 호텔 서비스 센터에서 일하고 있는 영훈이는 하루에도 수 백개의 문의를 처리합니다.

고조선 호텔 서비스 센터에서는 모든 문의 사항을 접수 순서대로 처리를 하도록 되어 있는데요. 다행히도 컴퓨터 과학을 공부한 영훈이는 프로그래밍을 이용해서 접수되는 문의들을 자동으로 처리하려고 합니다. 마침 데이터를 저장하는 순서대로 기억하고 가장 먼저 저장된 데이터부터 삭제할 수 있는 추상 자료형 큐가 있는데요. 큐를 이용해서 접수된 문의를 처리하는 클래스를 작성해 봅시다.

다행이 영훈이는 이미 고객 문의를 나타낼 클래스 CustomerComplaint는 정의해 놨는데요. 이제는 자동으로 문의를 처리해 줄 서비스 센터를 나타내는 CustomerServiceCenter를 작성해 봅시다. CustomerServiceCenter에는 문의를 처리하는 메소드 process_complaint() 메소드와 문의를 처리 대기열에 추가시켜주는 메소드 add_complaint() 메소드가 있습니다.

- process_complaint() 메소드는 아래 내용들을 수행합니다.
    1. 현재 접수 대기 중인 문의가 있으면 "{}님의 {} 문의 내용 접수 되었습니다. 담당자가 배정되면 {}로 연락드리겠습니다!"의 내용을 출력한다.
    2. 접수 대기중인 문의가 없으면 "더 이상 대기 중인 문의가 없습니다!"를 출력한다.
- add_complaint() 메소드는 다음 내용을 수행해요.
    1. 받아오는 파라미터를 이용해서 고객 센터 문의 인스턴스를 만들고 서비스 센터 인스턴스의 문의 대기 큐에 해당 문의를 추가시켜줍니다.

### 실습 결과
```
강영훈님의 음식이 너무 맛이 없어요 문의 내용 접수 되었습니다. 담당자가 배정되면 younghoon@codeit.com로 연락드리겠습니다!
더 이상 대기 중인 문의가 없습니다!
이윤수님의 에어컨이 안 들어와요... 문의 내용 접수 되었습니다. 담당자가 배정되면 yoonsoo@codeit.kr로 연락드리겠습니다!
손동욱님의 결제가 제대로 안 되는 거 같군요 문의 내용 접수 되었습니다. 담당자가 배정되면 dongwook@codeit.us로 연락드리겠습니다!
```

### 해설
#### add_complaint() 메소드
먼저 구체적인 문의 내용을 받아서 문의를 생성하고 접수 대기 큐에 추가시켜주는 add_complaint() 메소드를 정의해 봅시다.

일단 파라미터로 넘겨 받은 데이터를 이용해서 문의 인스턴스를 생성합니다.
```python
def add_complaint(self, name, email, content):
    """새로운 문의를 큐에 추가 시켜주는 메소드"""
    new_complaint = CustomerComplaint(name, email, content) # 새 문의 인스턴스 생성
```
그 다음에는 새롭게 만든 이 문의 사항을 문의 대기 큐에 추가시켜주면 되겠죠? deque를 이용한 큐의 마지막 순서에 데이터를 추가시켜주는 메소드는 append() 였던 거 기억나시죠?
```python
def add_complaint(self, name, email, content):
    """새로운 문의를 큐에 추가 시켜주는 메소드"""
    new_complaint = CustomerComplaint(name, email, content) # 새 문의 인스턴스 생성
    self.queue.append(new_complaint) # 문의 대기 큐에 추가 시켜준다
```
이렇게 하면 add_complaint 메소드는 다음 두 가지 조건을 만족시키게 돼요.
1. 새로운 문의 인스턴스를 생성한다.
2. 문의 대기 큐에 해당 인스턴스를 추가한다.

#### process_complaint() 메소드
다음은 처리 대기 중인 문의를 먼저 저장된 순서대로 처리해주는 메소드 process_complaint()를 작성해 봅시다.

가장 먼저 대기 큐가 비어 있는지 확인을 해야겠죠?
```python
def process_complaint(self):
    """접수된 고객 센터 문의 내용 처리하는 메소드"""
    if self.queue: # 대기 중인 문의가 있는지 확인
    
    else:
        print("더 이상 대기 중인 문의가 없습니다!")
```
파이썬 deque(를 비롯한 다른 여러 데이터 항목을 담는 자료형과 마찬가지로)가 비었는지 확인하는 방법은 if 뒤에 deque 인스턴스를 넣으면 됩니다.

만약 대기 큐가 비었으면 처리할 문의가 없기 때문에 해당 메시지를 출력하겠습니다.

다음은 대기 큐에 문의가 남아 있는 경우에 대해서 생각해 볼게요.

일단 가장 먼저 접수된 문의부터 삭제하는 동시에 처리해야 하는데요. deque에 popleft() 메소드를 사용하면 큐의 가장 앞에 저장되어 있는 데이터를 삭제하는 동시에 큐에서 삭제하는 데이터를 리턴받을 수 있습니다.

큐에서 삭제하면서 리턴받은 데이터의 속성을 이용하면 문의 처리 메시지를 출력할 수 있겠죠? 코드로 봅시다.
```python
def process_complaint(self):
    """접수된 고객 센터 문의 내용 처리하는 메소드"""
    if self.queue: # 대기 중인 문의가 있는지 확인

        # 가장 오래된 문의 먼저 처리
        complaint = self.queue.popleft()
        print(f"{complaint.name}님의 {complaint.content} 문의 내용 접수 되었습니다. 담당자가 배정되면 {complaint.email}로 연락드리겠습니다!")
    else:
        print("더 이상 대기 중인 문의가 없습니다!")
```
complaint 변수에 대기 큐에서 삭제한 문의 인스턴스를 저장하고 complaint의 속성들을 이용해서 이런식으로 처리 내용을 출력해 주는 거죠.

### 모범 답안
위 내용들을 하나로 뭉치면 이렇게 되겠죠?
```python
from collections import deque

class CustomerComplaint:
    """고객 센터 문의를 나타내는 클래스"""
    def __init__(self, name, email, content):
        self.name = name
        self.email = email
        self.content = content

class CustomerServiceCenter:
    """고조선 호텔 서비스 센터 클래스"""
    def __init__(self):
        self.queue = deque()   # 대기 중인 문의를 저장할 큐 생성

    def process_complaint(self):
        """접수된 고객 센터 문의 내용 처리하는 메소드"""
        if self.queue:  # 대기 중인 문의가 있는지 확인

            # 가장 오래된 문의 먼저 처리
            complaint = self.queue.popleft()
            print(f"{complaint.name}님의 {complaint.content} 문의 내용 접수 되었습니다. 담당자가 배정되면 {complaint.email}로 연락드리겠습니다!")
        else:
            print("더 이상 대기 중인 문의가 없습니다!")


    def add_complaint(self, name, email, content):
        """새로운 문의를 큐에 추가 시켜주는 메소드"""
        new_complaint = CustomerComplaint(name, email, content)   # 새 문의 인스턴스 생성
        self.queue.append(new_complaint)   # 문의 대기 큐에 추가 시켜준다
```

### 테스트 코드
```python
# 고객 문의 센터 인스턴스 생성
center = CustomerServiceCenter()


# 문의 접수한다
center.add_complaint("강영훈", "younghoon@codeit.com", "음식이 너무 맛이 없어요")

# 문의를 처리한다
center.process_complaint()
center.process_complaint()

# 문의 세 개를 더 접수한다
center.add_complaint("이윤수", "yoonsoo@codeit.kr", "에어컨이 안 들어와요...")
center.add_complaint("손동욱", "dongwook@codeit.us", "결제가 제대로 안 되는 거 같군요")
center.add_complaint("김현승", "hyunseung@codeit.ca", "방을 교체해주세요")

# 문의를 처리한다
center.process_complaint()
center.process_complaint()
```

### 실습 결과
```
강영훈님의 음식이 너무 맛이 없어요 문의 내용 접수 되었습니다. 담당자가 배정되면 younghoon@codeit.com로 연락드리겠습니다!
더 이상 대기 중인 문의가 없습니다!
이윤수님의 에어컨이 안 들어와요... 문의 내용 접수 되었습니다. 담당자가 배정되면 yoonsoo@codeit.kr로 연락드리겠습니다!
손동욱님의 결제가 제대로 안 되는 거 같군요 문의 내용 접수 되었습니다. 담당자가 배정되면 dongwook@codeit.us로 연락드리겠습니다!
이렇게 대기 순서대로 문의가 잘 처리되는 것을 확인할 수 있습니다.
```

[main6_09.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Data%20Structure/1%20Basic%20Data%20Structures/6%20Abstract%20Data%20Type/main6_09.py) 참고

<br/><br/>

23.01.14

## 10. 스택 개념

### 스택(Stack)
리스트, 큐와 마찬가지로 데이터 간 순서를 약속하는 추상 자료형  
stack: 어떤 물건이 차곡차곡 쌓여있는 것(예: 쌓여 있는 접시 스택 등)  
쌓여 있는 접시는 제일 위에 있는 접시부터 씀  
새로운 접시를 쌓을 때도 가장 위에 쌓음  
스택에서는 접시를 뺼 때도 쌓을 때도 맨 위에서만  
접시가 아니라 데이터로 바꾸어 생각해도 마찬가지  
데이터를 추가하거나 삭제할 때 맨 끝에 추가, 삭제하는 연산을 약속하는 추상 자료형  
큐는 FIFO, 스택은 LIFO  
LIFO: Last-in-first-out  
가장 마지막에 들어온 데이터가 가장 먼저 삭제됨

- 데이터 간 순서 관계를 유지할 수 있다
- 맨 뒤 데이터 추가
- 맨 뒤 데이터 삭제
- 맨 뒤 데이터 접근



파이썬에서는 큐와 마찬가지로 deque를 이용해 구현할 수 있음  
한글이나 워드에서 Ctrl + Z 하면 실행취소를 할 수 있음  
스택을 통해 구현 가능
```python
from collections import deque

stack = deque()

# 스택 맨 끝에 데이터 추가
stack.append("T")
stack.append("a")
stack.append("e")
stack.append("h")
stack.append("o")

print(stack)  # 스택 출력
# deque(['T', 'a', 'e', 'h', 'o'])


# 맨 끝 데이터 접근
print(stack[-1])  # o

# 맨 끝 데이터 삭제
print(stack.pop())  # o
print(stack.pop())  # h
print(stack.pop())  # e

print(stack)  # 스택 출력
# deque(['T', 'a'])
```

<br/><br/>

## 11. 스택 구현
스택도 동적 배열 또는 링크드 리스트로 구현할 수 있음  
|            |     동적 배열    | 더블리 링크드 리스트 |
|:----------:|:----------------:|:--------------------:|
| 맨 뒤 삭제 | 분할 상환 $O(1)$ |        $O(1)$        |
| 맨 뒤 삽입 | 분할 상환 $O(1)$ |        $O(1)$        |
| 맨 뒤 접근 |      $O(1)$      |        $O(1)$        |

시간 효율성 측면에서 동적 배열과 더블리 링크드 리스트 차이 없음  
deque를 스택처럼 이용  
deque는 더블리 링크드 리스트로 구현되어 있음  
그런데 동적 배열로 나타내도 마찬가지로 모든 연산을 $O(1)$으로 할 수 있음  
파이썬 리스트는 동적 배열로 구현되어 있음  
스택 사용하고 싶을 떄는 파이썬 deque 사용하는 것과 파이썬 list 사용하는 것에 시간 복잡도 차이 없음  
10. 스택 개념에서 쓴 코드에서
```python
stack = deque()
```
대신
```python
stack = []
```
로 써도 똑같이 작동함  
메소드 이름도 똑같음  
서로 다른 자료형이라도 같은 연산은 같은 메소드 이름을 씀  
결국 스택을 쓸 때 deque를 쓰나 list를 쓰나 시간 복잡도와 메소드 똑같음  

<br/><br/>

## 12. 괄호 짝 확인하기

### 실습 설명
마이크로하드에서 일하는 영훈이는 워드 프로세서 팀의 개발자로 일하고 있습니다. 어느날 샘 게이츠 사장님은 영훈이에게 워드 프로세서에서 이용자가 작성한 글에 짝이 없는 모든 괄호를 찾아내서 이용자에게 출력할 수 있는 기능을 추가하라는 특명을 받았습니다. 이 기능은 함수로 만들어 주라고 하는데요.

함수 parentheses_checker()는 인풋으로 문자열 파라미터 string을 받습니다.

parentheses_checker()는 string 안에 있는 모든 짝이 없는 괄호를 찾아내서 이 괄호들이 문자열 어디 위치에 있는지를 출력합니다. 만약 문자열 안에 모든 괄호가 짝이 있으면 함수는 아무 내용도 출력하지 않습니다.

스택이란 가장 뒤에 데이터를 추가할 수 있고 가장 마지막 데이터를 삭제할 수 있는 추상 자료형이라고 배웠죠. 한 번 파이썬 deque를 추상 자료형 스택으로 이용해서 이 함수를 작성해 봅시다!

### 실습 결과
```
테스트하는 문자열: (1+2)*(3+5)
테스트하는 문자열: ((3*12)/(41-31))
테스트하는 문자열: ((1+4)-(3*12)/3
문자열 0 번째 위치에 있는 괄호가 닫히지 않았습니다
테스트하는 문자열: (12-3)*(56/3))
문자열 13 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다
테스트하는 문자열: )1+14)/3
문자열 0 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다
문자열 5 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다
테스트하는 문자열: (3+15(*3
문자열 5 번째 위치에 있는 괄호가 닫히지 않았습니다
문자열 0 번째 위치에 있는 괄호가 닫히지 않았습니다
```

### 해설
#### 여는 괄호를 찾았을 때
```python
# 문자열의 각 문자를 돌면서
for i in range(len(string)):
    # 여는 괄호가 있는 위치를 스택에 저장한다
    if string[i] == "(":
        stack.append(i)
```
특정 위치에 있는 여는 괄호가 짝이 없는지 알기 위해서는 일단 문자열에 있는 모든 문자를 돌면서 확인을 해야되는데요.

문자열에서 여는 괄호를 찾았다고 합시다. 이 데이터를 어떻게 이용할 수 있을까요?

일단 여는 괄호가 문자열의 어디 위치에 있었는지 저장해야 되겠죠? 그래야지 나중에 닫는 괄호가 나오면 어떤 위치에 있는 여는 괄호랑 짝인지 확인할 수 있으니까요.

#### 닫는 괄호를 찾았을 때
```python
# 닫는 괄호가 있으면
elif string[i] == ")":
    # 스택에 여는 괄호 위치 데이터가 있으면 삭제하고
    if stack:
        stack.pop()
    # 아니면 현재 위치에 있는 닫는 괄호에 맞는 여는 괄호가 없다고 출력한다
    else:
        print(f"문자열 {i} 번째 위치에 있는 닫는 괄호에 맞는 여는 괄호가 없습니다")
```
문자열을 돌면서 닫는 괄호를 찾은 경우에 대해서 생각해 봅시다.

이 닫는 괄호에 맞는 여는 괄호가 있는지, 그리고 지금까지 나온 여는 괄호 중 어떤 괄호의 짝인지 어떻게 확인할 수 있을까요? 닫는 괄호의 짝은 앞서 본 모든 여는 괄호 중 가장 마지막에 본 여는 괄호입니다.
```
"5 + (4 - 2) * ((3 * 1) + 2)"
```
위와 같은 이런 문자열이 있으면, 1 뒤에 있는 닫는 괄호의 짝은 왼쪽으로 가장 가까운 여는 괄호, 3 앞에 있는 여는 괄호인 거죠.

다행히 우리는 여는 괄호를 찾을 때마다 스택에 순서대로 위치를 저장하고 있었는데요. 닫는 괄호를 찾을 때마다 맞는 여는 괄호는 스택에 맨 뒤에 저장된 위치에 있는 여는 괄호입니다.

스택 안에 데이터가 저장돼 있으면 현재 보고 있는 닫는 괄호는 여는 괄호 짝이 있으니까 스택에서 지워주면 됩니다.

닫는 괄호를 찾았는데 만약에 스택에 여는 괄호 위치가 저장이 안 돼 있으면, 그러니까 스택이 비어 있으면 무슨 뜻일까요? 이 때는 지금 인덱스 위치에 있는 닫는 괄호에 맞는 여는 괄호 짝이 없다는 뜻이 되겠죠.

이 때는 메시지를 출력하면 됩니다.

#### 여는 괄호 데이터가 끝까지 남을 때
마지막으로 문자열에 있는 모든 문자를 다 돌았는데 스택 안에 아직 여는 괄호 정보가 남아 있으면 무슨 의미인지 생각해 봅시다. 여는 괄호를 찾을 때마다 위치를 저장해주고 닫는 괄호를 찾을 때마다 여는 괄호를 하나씩 지워줬는데 모든 문자열을 다 돌고도 삭제되지 않은 여는 괄호 정보가 있다는 말은, 해당 인덱스에 있는 여는 괄호들은 짝 닫는 괄호가 없다는 뜻이겠죠? 이 정보도 출력해야 하니, 스택에 남아 있는 여는 괄호 정보를 하나씩 삭제해주면서 해당 괄호 위치에 여는 괄호는 짝 닫는 괄호가 없다는 것을 출력합니다.
```python
# 스택에 열린 괄호 위치 데이터가 남아 있으면 해당 열린 괄호는 짝이 맞는 닫힌 괄호가 없다는 뜻이다
while stack:
    print(f"문자열 {stack.pop()} 번째 위치에 있는 괄호가 닫히지 않았습니다")
```

### 모범 답안
해설 코드를 정리하면 이렇게 되겠죠?
```python
from collections import deque

def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""

    stack = deque()  # 사용할 스택 정의

    print(f"테스트하는 문자열: {string}") 

    # 문자열의 각 문자를 돌면서
    for i in range(len(string)):
        # 열리는 괄호가 있는 위치를 스택에 저장한다
        if string[i] == "(":
            stack.append(i)
        # 닫히는 괄호가 있으면
        elif string[i] == ")":
            # 스택에 열린 괄호 위치 데이터가 있으면 삭제하고
            if stack:
                stack.pop()
            # 아니면 현재 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없다고 출력한
            else:
                print(f"문자열 {i} 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다")

    # 스택에 열린 괄호 위치 데이터가 남아 있으면 해당 열린 괄호는 짝이 맞는 닫힌 괄호가 없다는 뜻이다
    while stack:
        print(f"문자열 {stack.pop()} 번째 위치에 있는 괄호가 닫히지 않았습니다")
```

### 테스트 코드
실행 코드를 돌려보면 출력 결과가 원하는대로 나오는 것을 확인할 수 있습니다.
```python
case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

parentheses_checker(case1)
parentheses_checker(case2)
parentheses_checker(case3)
parentheses_checker(case4)
parentheses_checker(case5)
parentheses_checker(case6)
```

### 실습 결과
```
테스트하는 문자열: (1+2)*(3+5)
테스트하는 문자열: ((3*12)/(41-31))
테스트하는 문자열: ((1+4)-(3*12)/3
문자열 0 번째 위치에 있는 괄호가 닫히지 않았습니다
테스트하는 문자열: (12-3)*(56/3))
문자열 13 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다
테스트하는 문자열: )1+14)/3
문자열 0 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다
문자열 5 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다
테스트하는 문자열: (3+15(*3
문자열 5 번째 위치에 있는 괄호가 닫히지 않았습니다
문자열 0 번째 위치에 있는 괄호가 닫히지 않았습니다
```

[main6_12.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Data%20Structure/1%20Basic%20Data%20Structures/6%20Abstract%20Data%20Type/main6_12.py) 참고

<br/><br/>

23.01.15

## 13. 딕셔너리

### 딕셔너리(Dictionary)
- 맵(Map)이라고도 부름
- key-value 쌍을 삽입, 탐색, 삭제할 수 있는 추상 자료형
- 데이터 간 순서 관계를 약속하지 않음

```python
grades = {}  # 딕셔너리는 중괄호로 선언함

# key - value 데이터 삽입
grades["현승"] = 80
grades["태호"] = 60
grades["영훈"] = 90
grades["지웅"] = 70
grades["동욱"] = 96

print(grades)  # 딕셔너리 출력
# {'현승': 80, '태호': 60, '영훈': 90, '지웅': 70, '동욱': 96}

# 한 key에 여러 value 저장 시도
grades["태호"] = 100

print(grades)  # 딕셔너리 출력
# {'현승': 80, '태호': 100, '영훈': 90, '지웅': 70, '동욱': 96}
# key에 여러 value가 들어가는 게 아니라 마지막 value로 바뀜

# key를 이용해서 value 탐색
print(grades["동욱"])  # 96
print(grades["현승"])  # 80

# key를 이용한 삭제
grades.pop("태호")  # print 사용하면 pop 하는 value return하여 보여줌
grades.pop("지웅")

print(grades)  # 딕셔너리 출력
# {'현승': 80, '영훈': 90, '동욱': 96}
```

key - value 쌍을 저장, key로 value 탐색, key로 데이터 삭제하고 싶으면 추상 자료형 딕셔너리(맵) 떠올리면 됨  
기능에 집중하고 구현은 신경 덜 쓸 수 있게 해줌  

딕셔너리를 어떤 자료구조로 구현할 수 있을까?  
해시 테이블  
|                     | 해시 테이블 |
|:-------------------:|:-----------:|
| key - value 쌍 삽입 |    $O(1)$   |
|  key를 이용한 탐색  |    $O(1)$   |
|  key를 이용한 삭제  |    $O(1)$   |

파이썬 딕셔너리도 해시 테이블 이용해 구현되어 있음  