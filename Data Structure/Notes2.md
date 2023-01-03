# 4 링크드 리스트
22.09.05 23:18  
  
## 01. 링크드 리스트 개념  
  
### 링크드 리스트(Linked List)
- 데이터를 순서대로 저장해준다
- 요소를 계속 추가할 수 있다

동적 배열과 비슷하지만 구현 방식이 조금 복잡함  
처음 배울 때는 굳이 이걸 왜 쓰나 싶을 수 있지만, 상황에 따라 링크드 리스트 사용하는 게 더 적합할 때가 있음  
   
링크드 리스트는 "노드"라는 단위의 데이터를 저장하고 데이터가 저장된 각 노드들을 순서대로 연결시켜서 만든 자료구조  
  
예시) 노드: 박스  
각 박스에는 이름이 있음  
규리, 태호, 동욱, 유나, 현승 등  
박스에는 칸막이 같은 게 있어서 왼쪽 오른쪽에 각각 뭔가를 넣을 수 있음  
왼쪽에는 저장하고 싶은 값을 넣으면 됨  
2, 3, 5, 7, 11을 저장하고 싶다고 가정  
각 박스의 왼쪽 칸에 값을 저장  
규리 박스 왼쪽 칸에 2, 태호 박스 왼쪽 칸에 3 등  
그 후에 2, 3, 5, 7, 11을 순서대로 나열하고 싶으면  
박스들의 이름을 이용하여, 박스의 오른쪽 칸에 다음 박스의 이름을 저장  
2가 담겨있는 규리 박스 오른쪽 칸에 3이 담겨있는 박스의 이름 태호를 넣으면 됨  
같은 식으로 하면 규리, 태호, 동욱, 유나, 현승 박스가 차례로 연결됨
오른쪽 칸이 비어있는 현승 박스는 마지막 박스  

<br/><br/>

22.09.06 23:47  
## 02. 링크드 리스트 프로그래밍적으로 생각하기
노드(Node)  
각 노드는 하나의 객체로 표현됨  
각 노드 객체에는 두 가지 속성이 있음  
데이터와 넥스트  
데이터에는 우리가 저장하고 싶은 정보를 넣음  
박스 비유에서 왼쪽 칸에 넣는 정보를 데이터 속성에 넣는 것  
넥스트 속성은 다음 노드에 대한 레퍼런스  
박스 비유에서 오른쪽 칸과 비슷함  
다음 박스의 이름 대신에 다음 노드에 대한 레퍼런스를 넣는 것  
예를 들어 n_1과 n_2 노드객체가 있다고 가정  
만약 n_1의 다음 노드를 n_2로 설정해주고 싶다면, n_1.next = n_2 지정하면 됨  
n_1.next는 n_2에 대한 레퍼런스  
노드 객체를 여러 개 만들었다고 가정  
이 노드 객체들은 서로 딱히 관계가 없음  
메모리에 연속적으로 저장된 게 아니라 각자 알아서 어딘가에 흩어져있음  
그런데 각 노드는 다음 노드에 대한 레퍼런스가 있음  
노드 객체의 next 속성을 보면 다음 노드가 어디에 저장돼있는지 알 수 있음  
가장 첫번째 노드 객체의 메모리 주소만 알고 있으면 next 타고 타고 가서 연결된 모든 노드 접근 가능  
링크드 리스트의 시작점 역할을 하는 첫 번째 노드 객체를 head라고 함  
head 노드만 있으면 흩어져있는 다른 노드들을 연결지어 순서를 저장할 수 있음  
배열이나 동적 배열처럼 정보를 원하는 순서로 저장할 수 있음  
주의사항  
앞으로 링크드 리스트 나타낼 때 마치 이 객체들이 순서대로 나열되어 있는 것처럼 보여주겠지만 이건 우리의 이해를 돕기 위한 것  
실제 메모리에서는 여기저기 흩어져있음  
  
<br/><br/>

22.09.07 23:04  
## 03. 노드 클래스 만들기
링크드 리스트는 노드 객체로 이루어져있음  
노드 객체를 만들려면 노드 클래스를 정의해야 함  
```python
class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data  # 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스


# 데이터 2, 3, 5, 7, 11을 담는 노드들 생성, 이름을 짓고 변수에 지정
head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)
```

<br/><br/>

## 04. 간단한 링크드 리스트 만들기  

```python
class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data  # 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스


# 데이터 2, 3, 5, 7, 11을 담는 노드들 생성, 이름을 짓고 변수에 지정
head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)

# 노드들을 연결
head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

# 노드 순서대로 출력
iterator = head_node

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next
```
```
2
3
5
7
11
```

<br/><br/>

22.12.30  
## 05. 링크드 리스트 추가 연산  
위에까지는 Node Class를 정의하고 인스턴스를 만들어 연결을 해주었다.  
링크드 리스트라고 할 수는 있는데, 더 체계적으로 관리하기 위해 LinkedList Class 만들 수 있다.  
append 메소드.

[main4_05.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Data%20Structure/main4_05.py) 참고

<br/><br/>

## 06. 링크드 리스트 \_\_str\_\_ 메소드
### \_\_str\_\_ 메소드
링크드 리스트를 클래스로 만들었으니까 링크드 리스트를 문자열로 표현해주는 \_\_str\_\_ 메소드를 정의해봅시다. \_\_str\_\_ 메소드가 기억 안 나시는 분들은 그냥 링크드 리스트를 출력할 때 자동으로 링크드 리스트의 내용을 사람들이 이해할 수 있는 문자열로 리턴해주는 메소드로 이해하시면 됩니다.

### 링크드 리스트 \_\_str\_\_ 메소드
```python
class LinkedList:
    """링크드  리스트 클래스"""
    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)
        
        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            self.tail = new_node  # 마지막 노드를 추가한 노드로 바꿔준다

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str
```
\_\_str\_\_ 메소드는 문자열을 리턴하니까 일단 리턴 시킬 res_str 변수를 빈 문자열로 정의합니다. iterator을 써서 링크드 리스트를 도는 방법은 이미 배웠죠?
1. iterator 변수를 링크드 리스트의 head를 가리키게 합니다
2. iterator 변수가 None이 아닐 때까지 (링크드 리스트의 처음부터 끝 노드까지) iterator 변수의 data를 res_str 변수에 추가해 줍니다. iterator 변수의 next 속성을 이용해서 while 문을 돌 때마다 다음 노드로 갑니다.
3. 링크드 리스트를 다 돈 후에 res_str 변수를 리턴합니다.

한 번 제대로 코드를 작성했는지 확인해봅시다.
```python
# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 링크드 리스트에 데이터 추가
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)
```
영상에서와 동일하게 링크드 리스트에 노드를 추가해줬습니다.
```python
print(linked_list)  # 링크드 리스트 출력
```
그다음에 이렇게 링크드 리스트 인스턴스를 출력할 건데요. 이때 노트 위에서 정의한 __str__ 메소드가 호출되는 거죠.
```
| 2 | 3 | 5 | 7 | 11 |
```
링크드 리스트의 내용이 원하는 대로 잘 출력되는군요! 앞으로 링크드 리스트에 저장되어 있는 데이터를 확인하기 위해서 \_\_str\_\_ 메소드를 자주 쓸 건데요. 이번 노트에서 정의해놨으니까 다음 레슨들에서 그냥 자연스럽게 사용할게요.

<br/><br/>

## 07. 링크드 리스트 접근

### 배열 접근 연산
```python
int_array[0]
int_array[1] = 11
```
- 특정 위치에 저장한 데이터를 가지고 오거나 바꿔주는 연산

### 링크드 리스트 접근 연산
- 특정 위치에 있는 **노드**를 리턴하는 연산
- 헤드 노드에서 시작해서 다음 노드들을 하나씩 돌면서 원하는 위치의 노드에 접근
- 인덕스 x에 있는 노드에 접근하려면 head에서 다음 노드로 x번 가면 됨

### 링크드 리스트 접근 시간 복잡도
- 인덱스 x에 있는 노드에 접근하려면 head에서 다음 노드로 x번 가면 됨
- 마지막 노드에 접근하려면 head에서 다음 노드로 n-1 번 가야 됨
- 접근 연산 시간 복잡도: $O(n)$

[main4_07.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Data%20Structure/main4_07.py) 참고

<br/><br/>

## 08. 링크드 리스트 탐색 연산

### 실습 설명
탐색 연산은 자료 구조에서 원하는 조건의 데이터를 찾아내는 연산입니다.

링크드 리스트 탐색 연산은 특정 데이터를 갖는 노드를 리턴합니다.

이렇게
```
| 2 | 3 | 5 | 7 | 11
```
링크드 리스트에 2, 3, 5, 7, 11이 저장돼 있다고 합시다. 여기서 5를 갖는 노드를 탐색하면, 링크드 리스트 안에서 5를 가지고 있는 노드를 찾아서 리턴하는 거죠.

배열에서 탐색 연산을 어떻게 하셨는지 기억 나시나요? 선형적으로 가장 앞부터 마지막 인덱스까지 돌면서 탐색을 했습니다. 링크드 리스트도 배열과 마찬가지로 선형 탐색을 사용합니다. 가장 앞 노드부터 끝 노드까지 돌면서 원하는 데이터를 갖는 노드를 리턴하죠.

이번 과제에서는 링크드 리스트의 탐색 연산을 직접 구현해 볼게요.

메소드 find_node_with_data는 찾으려는 데이터를 파라미터 data로 받아서 링크드 리스트 내에서 원하는 데이터를 갖고 있는 노드를 리턴합니다.

단, 원하는 데이터가 링크드 리스트 안에 없을 때는 None을 리턴합니다.

### 실습 결과
```
2
11
6을 갖는 노드는 없습니다
```

<br/><br/>

### 해설
해설 노트에서 링크드 리스트 클래스를 전부 다 보여주기에는 공간이 너무 많이 차지되기 때문에 과제마다 해당 메소드와 실행 코드만 보여드리겠습니다!

#### find_node_with_data 메소드
```python
def find_node_with_data(self, data):
    """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
    iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수
```
링크드 리스트를 처음부터 끝까지 돌 때는 \_\_str\_\_ 메소드나 find_node_at 메소드를 쓸 때랑 똑같이 iterator 변수를 사용합니다. 처음에 iterator 변수는 링크드 리스트의 헤드 노드를 가리키게 합니다.
```python
# 링크드 리스트 전체를 돈다
while iterator is not None:
    # iterator 노드의 데이터가 찾는 데이터면 iterator를 리턴한다
    if iterator.data == data:
        return iterator
    iterator = iterator.next  # 다음 노드로 넘어간다
```
그리고 링크드 리스트를 도는데요. while문을 이용해서 head에서 tail 노드까지 돕니다. iterator 변수가 반복문을 돌 때마다 다음 순서에 있는 노드를 가리키는데요. iterator가 None이면 더이상 다음 노드가 없다는 말, 그러니까 링크드 리스트 끝까지 도달했다는 뜻입니다.

반복문 안에서는 if문을 사용해서 현재 보고 있는 노드 iterator 변수의 속성이 파라미터로 받은 data인지 확인해 줍니다. 맞다면 iterator 변수, 즉 현재 돌면서 확인하고 있는 노드를 리턴하는 거죠.
```python
    # 링크드 리스트 안에 원하는 데이터가 없었기 때문에 None 리턴한다
    return None
```
링크드 리스트의 모든 노드를 다 돌았는데 원하는 조건의 노드를 못 찾은 경우는 뭘까요? 원하는 조건의 노드가 링크드 리스트 안에 없다는 거죠. 이 때는 None을 리턴합니다.



### 모범 답안
위 해설 코드를 다 합치면 이렇게 되겠죠?
```python
def find_node_with_data(self, data):
    """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
    iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

    # 링크드 리스트 전체를 돈다
    while iterator is not None:
        # iterator 노드의 데이터가 찾는 데이터면 iterator를 리턴한다
        if iterator.data == data:
            return iterator
        iterator = iterator.next  # 다음 노드로 넘어간다

    # 링크드 리스트 안에 원하는 데이터가 없었기 때문에 None 리턴한다
    return None 
```
#### 테스트 코드
제대로 동작하는지 실행 코드를 돌려 볼게요.
```python
# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 여러 데이터를 링크드 리스트 마지막에 추가
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)

# 데이터 2를 갖는 노드 탐색
node_with_2 = linked_list.find_node_with_data(2)

if not node_with_2 is None:
    print(node_with_2.data)
else:
    print("2를 갖는 노드는 없습니다")

# 데이터 11을 갖는 노드 탐색
node_with_11 = linked_list.find_node_with_data(11)

if not node_with_11 is None:
    print(node_with_11.data)
else:
    print("11를 갖는 노드는 없습니다")

# 데이터 6 갖는 노드 탐색
node_with_6 = linked_list.find_node_with_data(6)

if not node_with_6 is None:
    print(node_with_6.data)
else:
    print("6을 갖는 노드는 없습니다")
```
결과가 제대로 출력되는 걸 확인할 수 있습니다.
```
2
11
6을 갖는 노드는 없습니다
```

[main4_08.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Data%20Structure/main4_08.py) 참고

<br/><br/>

23.01.02  
## 09. 링크드 리스트 삽입 연산

append 메소드는 Linked List 끝에 새로운 데이터를 추가하는 방법  
Linked List의 Node가 주어졌을 때 그 노드 바로 뒤에 새로운 Node를 삽입하는 insert_after도 생각할 수 있다

[main4_09.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Data%20Structure/main4_09.py) 참고

<br/><br/>

## 10. prepend: 링크드 리스트 가장 앞 삽입

### 실습 설명
저번 레슨에서는 링크드 리스트에서 주어진 노드 뒤에 새로운 노드를 삽입하는 연산을 배웠는데요. 이 연산을 메소드로 구현했을 때는 insert_after 메소드로 구현했습니다.

사실 이 연산에는 한 가지 흠이 있는데요. 이 연산은 항상 주어진 노드 다음에 노드를 삽입하잖아요? 파라미터로 가장 앞 노드 head를 넘겨줘도 head 노드 앞에는 새로운 노드를 추가할 수 없습니다. 링크드 리스트 가장 앞에는 삽입할 수 없다는 거죠.

이 문제를 해결해주는 새로운 메소드를 정의해 줍시다. 이 메소드는 prepend라고 부르고요, 파라미터로 데이터 data를 받아서 링크드 리스트의 가장 앞에 데이터를 data로 갖는 새로운 노드를 추가시켜 줍니다.

주의 사항: prepend 메소드를 작성할 때 링크드 리스트가 비어 있는 경우도 생각해서 작성하셔야 됩니다!

### 실습 결과
```
| 2 | 3 | 5 | 7 | 11 |
2
11
```

[main4_10.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Data%20Structure/main4_10.py) 참고

<br/><br/>

## 11. 링크드 리스트 삭제  

삭제 연산 메소드 delete_after  
파라미터로 previous_node 받고 그 다음 순서 데이터를 지워줌  
삭제하려는 노드가 tail노드인지 아닌지 두 경우로 나뉨  
각 경우 나누어 삭제 및 남은 노드 연결해주고  
삭제하는 노드의 데이터를 보여주는 게 관습이기 때문에 삭제되는 데이터를 return

[main4_11.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Data%20Structure/main4_11.py) 참고

<br/><br/>

23.01.03  

## 12. popleft 링크드 리스트 가장 앞 삭제

### 실습 설명
바로 전 레슨에서 배운 삭제는 삽입과 마찬가지의 문제가 있는데요. 주어진 노드의 다음 노드를 삭제하기 때문에 head 노드를 삭제할 수 없습니다. 전과 마찬가지로 head 노드도 지울 수 있도록 메소드를 추가하겠습니다.

메소드 pop_left는 파라미터로 self 이외에 아무것도 받지 않으며, 링크드 리스트의 head 노드를 삭제해줍니다. pop_left 메소드는 링크드 리스트에서 삭제하는 노드의 데이터를 리턴합니다.

### 주의 사항
- pop_left 메소드를 호출함으로 인해서 링크드 리스트가 비어지는 경우를 생각해서 작성하셔야 됩니다! (지우려는 노드가 링크드 리스트의 마지막 남은 노드일 때)
- pop_left를 호출할 때 링크드 리스트가 비어 있는 경우는 없다고 가정해도 됩니다.
- pop_left 메소드는 삭제하는 노드의 데이터를 리턴합니다.

### 실습 결과
```
2
3
5
7
11
|
None
None
```

<br/><br/>

### 해설
#### 경우 1: 삭제하려는 노드가 마지막 남은 노드일 때
```python
def pop_left(self):
    """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정한다"""
    # 지우려는 데이터가 링크드 리스트의 마지막 남은 데이터일 때
    if self.head is self.tail:
        self.head = None
        self.tail = None
```
링크드 리스트에 하나의 노드만 남은 경우는 가장 앞 노드가 동시에 가장 마지막 노드인 경우입니다. 이 경우는 if self.head is self.tail의 if문으로 찾을 수 있습니다.

이 경우에는 링크드 리스트에 남은 노드가 하나도 없게 해야 됩니다. head와 tail 속성을 모두 None을 가리키게 하면 되죠.

#### 경우 2: 삭제하려는 노드가 마지막 남은 노드가 아닐 때
```python
else:
    # 링크드 리스트의 head를 지금 head의 다음 노드로 지정해준다
    self.head = self.head.next
```
경우가 두 개밖에 없기 때문에 else문을 사용해서 두 번째 경우를 찾습니다.

head 노드를 더 이상 찾을 수 없게 해주는 동시에 인덱스 1에 있는 노드를 head로 만들어 줘야 되는데요. 이때 그냥 self.head 속성이 현재 head 노드의 다음 노드를 가리키게 하면 됩니다. 그럼 링크드 리스트 안에 원래 head 노드를 가리키는 레퍼런스는 없어지고, 링크드 리스트의 가장 앞 노드가 한 순서 뒤로 밀렸으니까 head 노드를 삭제했다고 할 수 있겠죠?

#### 삭제하는 데이터 리턴
```python
def pop_left(self):
    """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정한다"""
    data = self.head.data  # 삭제할 노드를 미리 저장해놓는다

    # 지우려는 데이터가 링크드 리스트의 마지막 남은 데이터일 때
    if self.head is self.tail:
        self.head = None
        self.tail = None
    else: 
        self.head = self.head.next

    return data  # 삭제된 노드의 데이터를 리턴한다
```
이렇게 메소드 가장 위 부분에 삭제하는 노드의 데이터를 변수에 저장하고, 마지막에 리턴해 주면 됩니다.

코드가 제대로 실행되는지 볼게요.

#### 테스트 코드
```python
# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 여러 데이터를 링크드 리스트 앞에 추가
linked_list.prepend(11)
linked_list.prepend(9)
linked_list.prepend(5)
linked_list.prepend(3)
linked_list.prepend(2)

print(linked_list) # 링크드 리스트 출력

# 가장 앞 노드 계속 삭제
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())

print(linked_list) # 링크드 리스트 출력
print(linked_list.head)
print(linked_list.tail)
```

### 실습 결과
```
2
3
5
7
11
|
None
None
```
[main4_12.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/main/Data%20Structure/main4_12.py) 참고
