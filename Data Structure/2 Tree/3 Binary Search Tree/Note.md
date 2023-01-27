# 3 이진 탐색 트리

23.01.25

## 01. 이진 탐색 트리란

### 이진 탐색 트리(Binary Search Tree)  

힙은 데이터를 정렬할 때 사용할 수도 있고, 우선순위 큐라는 추상 자료형을 구현할 때 사용할 수도 있음  
이진 탐색 트리는 딕셔너리나 세트라는 추상 자료형을 구현하는 데 쓸 수 있음  

이진 탐색 트리는 이진 트리이면서, 왼쪽의 모든 노드는 부모 노드보다 작아야 하고, 오른쪽의 모든 노드는 부모 노드보다 큰 속성을 만족해야 함  
이진 탐색 트리를 이용하면, 원하는 노드를 찾을 수 있음  
찾고자 하는 데이터를 현재 노드 데이터와 비교해서, 작으면 왼쪽 자식, 크면 오른쪽 자식으로 가면 됨  
이렇게 데이터를 찾는 연산을 **탐색**이라고 함  
이번 챕터에서 이진 탐색 트리에 데이터를 저장, 탐색, 삭제하는 방법, 그리고 이진 탐색 트리를 활용하는 방법 배울 것

<br/><br/>

## 02. 이진 탐색 트리 노드 구현  

힙은 완전 이진 트리이기 때문에 배열로 구현했지만, 이진 탐색 트리는 완전 이진 트리라는 보장이 없기 때문에, 배열이나 파이썬 리스트로 구현하지 않는다!  
대신 노드 클래스를 정의한 후, 노드 인스턴스를 생성한 뒤 연결해준다  

 이진 트리 노드 클래스에서 부모 노드 레퍼런스를 추가해주면 됨  
 더블리 링크드 리스트에서 앞과 뒤 노드의 레퍼런스를 저장했듯이, 이진 탐색 트리 노드는 왼쪽 자식, 오른쪽 자식, 부모 노드까지 총 3개의 레퍼런스를 가짐  
 
 [main3_02.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/6d8732f13c6e250bc8646547b68d73afecd58ffc/Data%20Structure/2%20Tree/3%20Binary%20Search%20Tree/main3_02.py) 참고

<br/><br/>

## 03. 이진 탐색 트리 출력

### in-order 순회
이진 탐색 트리에는 굉장히 재미있는 특성이 하나 더 있는데요. 전에 배웠던 in-order 순회, 기억나시나요?

이런 트리를:  
![image](https://bakey-api.codeit.kr/files/2393/7HTQHF?name=1.png)  
in-order 순회하면서 노드의 값을 출력하면 A, B, C, D, E, F, G, H, I의 순서대로 출력됩니다.

기억이 안 나는 분들을 위해 다시 정리하면 in-order 순회는
1. 왼쪽 부분 트리를 in-order 순회한다
2. 현재 노드의 데이터를 출력한다
3. 오른쪽 부분 트리를 in-order 순회한다

의 순서로 전체 트리를 순회합니다. 그래도 기억이 안 나시면 챕터 1을 복습하고 오세요.

### in-order 순회와 이진 탐색 트리
이진 탐색 트리를 in-order 순회하면 저장된 데이터들을 정렬된 순서대로 출력할 수 있습니다. 아래와 같은 이진 탐색 트리가 있다고 했을 때  
![image](https://bakey-api.codeit.kr/files/2393/TGgyjv?name=2.png)  
트리의 root 노드(8이 있는 노드)를 in-order 순회 함수의 파라미터로 넘겨주면 트리 안에 있는 데이터를:

1, 3, 4, 6, 7, 8, 10, 13, 14

처럼 정렬된 순서대로 출력할 수 있는 거죠.

### BinarySearchTree 클래스
이전에 구현해 본 in-order 순회 함수를 재활용해서 이진 탐색 트리를 나타내는 BinarySearchTree 클래스에 트리 속의 데이터를 순서대로 출력하는 메소드, print_sorted_tree 메소드를 작성할게요.
```python
def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None


    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root 노드를 in-order로 출력한다
```

이제 트리를 출력할 때는 print_sorted_tree 메소드를 사용하겠습니다!

<br/><br/>

## 04. 이진 탐색 트리 삽입  
### 이진 탐색 트리 삽입
- 삽입 이후에도 이진 탐색 트리 속성이 유지되어야 함!  
1. 새로운 노드 생성
2. root 노드부터 비교하면서 저장할 위치 찾음(새로운 노드가 비교하는 노드보다 작으면 왼쪽, 크면 오른쪽으로 보내다가, 빈 자리가 나면 그곳이 저장할 위치)
3. 찾은 위치에 새롭게 만든 노드 연결

### 삽입 시간 복잡도  
트리의 높이(h)를 이용해서 시간 복잡도를 분석함  
1. 새로운 노드 생성: $O(1)$
2. root 노드부터 비교하면서 저장할 위치 찾음: $O(h)$
3. 찾은 위치에 새롭게 만든 노드 연결: $O(1)$

즉 삽입 시간 복잡도는 $O(1 + h + 1) = O(h)$

<br/><br/>

## 05. 이진 탐색 트리 삽입 구현  
### 실습 설명
이번 과제에서는 이진 탐색 트리에 데이터를 삽입하는 함수를 구현해 보겠습니다.  
이전 영상에서 본 대로 데이터 삽입 연산을 단계별로 정리하면 아래와 같습니다.  
1. 새로운 노드를 생성합니다.
2. root 노드부터 데이터를 비교하면서 새로운 노드를 저장할 위치를 찾습니다.
    - 새로운 노드의 데이터가 더 크면, root 노드의 오른쪽 부분 트리에 저장돼야 하고
    - 더 작으면, root 노드의 왼쪽 부분 트리에 저장돼야 합니다.
3. 찾은 위치에 새로운 노드를 저장합니다

이 내용을 코드로 작성해 봅시다.

BinarySearchTree 클래스의 insert() 메소드는 self, 새로운 데이터 data를 파라미터로 받습니다. 그리고 이진 탐색 트리 안에서 알맞는 위치에 data를 갖는 새로운 노드를 삽입하죠.

그런데 데이터를 삽입할 때 만약 이진 탐색 트리에 노드가 하나도 없는 경우는 어떻게 해야 할까요? 그럴 땐 그냥 새 노드를 root 노드로 만들면 됩니다. 그 경우에 대한 처리는 이미 코드로 작성해 두었습니다. 템플릿의 insert()  메소드 안에서 data를 갖는 새로운 노드 new_node를 root 변수에 지정한 부분을 보세요.

이런 특수한 경우를 제외한 일반적인 경우에서의 데이터 삽입을 위한 코드를 직접 작성해 보세요.

### 실습 결과
```
2
3
4
5
7
8
9
11
14
17
19
```

<br/><br/>

### 해설
#### temp 변수 정의와 반복문
새로운 노드를 저장할 위치를 찾기 위해서는 일단 root 노드에서부터 그 위치를 찾아서 내려가야 하는데요. 위치를 찾을 때 임시 변수이자 도우미 변수인 temp를 정의할게요. temp는 맨 처음엔 root 노드로 초기화합니다. 나중에 이 변수가 저장하는 노드를 계속 바꿔 줄게요.
```python
temp = self.root  # 비교 대상이 되는 노드를 담기 위한 임시 변수, root 노드로 초기화한다
```
temp와 삽입하려는 데이터를 비교해 가면서 new_node를 저장할 위치를 찾아 가야 되는데요.

원하는 위치를 찾을 때까지 반복문을 돌리면 됩니다. 반복문이 한 번 돌 때마다 temp 노드와 삽입하려는 데이터를 비교해 주는 거죠. 코드로 나타내면 이렇게 할 수 있습니다.
```python
# 원하는 위치를 찾아간다
while temp is not None:
      if data > temp.data:  # 삽입하려는 데이터가 현재 노드 데이터보다 크다면

      else:  # 삽입하려는 데이터가 현재 노드 데이터보다 작다면
```
#### data가 temp.data 보다 클 경우
data가 temp의 데이터보다 크다는 건 new_node가 temp의 오른쪽 부분 트리에 저장돼야 한다는 말입니다.

이 때 temp가 오른쪽 자식이 없으면 어떻게 해야 할까요? 바로 new_node를 temp의 오른쪽 자식으로 저장하면 됩니다.

이때 해야할 작업은 다음과 같습니다.
- temp를 new_node의 부모 노드로 지정한다.
- new_node를 temp의 오른쪽 자식으로 지정한다.

temp가 오른쪽 자식이 있을 때는 어떻게 하면 될까요? temp의 오른쪽 자식으로 가서 다시 new_node와 데이터의 크기를 비교하는 작업을 또 해주면 됩니다.

코드로는 이렇게 쓰면 됩니다.
```python
    # 원하는 위치를 찾아간다
    while temp is not None:
        if data > temp.data:  # 삽입하려는 데이터가 현재 노드 데이터보다 크다면
            # 오른쪽 자식이 없으면 새로운 노드를 현재 노드 오른쪽 자식으로 만듦
            if temp.right_child is None:
                new_node.parent = temp
                temp.right_child = new_node
                return
            # 오른쪽 자식이 있으면 오른쪽 자식으로 간다
            else:
                temp = temp.right_child
```

#### data가 temp.data 보다 작을 경우
data가 temp의 데이터보다 작은 경우도 볼게요.
```python
    else:  # 삽입하려는 데이터가 현재 노드 데이터보다 작다면
        # 왼쪽 자식이 없으면 새로운 노드를 현재 노드 왼쪽 자식으로 만듦
        if temp.left_child is None:
            new_node.parent = temp
            temp.left_child = new_node
            return
        # 왼쪽 자식이 있다면 왼쪽 자식으로 간다
        else:
            temp = temp.left_child
```
data가 temp.data보다 큰 경우와 비슷하게 생각하시면 됩니다. data가 temp의 데이터보다 작다는 말은 new_node가 temp의 왼쪽 부분 트리에 저장되어야 한다는 말입니다.

이 때 temp가 왼쪽 자식이 없다면 그냥 new_node를 temp의 왼쪽 자식으로 만들면 됩니다.

- temp 를 new_node의 부모 노드로 만든다.
- new_node를 temp의 왼쪽 자식으로 만든다.

temp가 왼쪽 자식이 있다면 거기로 간 다음에 다시 위치를 찾아 주면 되죠.

### 모범 답안
코드를 정리하면 이렇게 되겠죠? (코드가 너무 길어서 insert() 메소드만 보여드립니다.)
```python
    def insert(self, data):
        """이진 탐색 트리 삽입 메소드"""
        new_node = Node(data)  # 삽입할 데이터를 갖는 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        # 코드를 쓰세요
        temp = self.root  # 저장하려는 위치를 찾기 위해 사용할 변수. root 노드로 초기화한다

        # 원하는 위치를 찾아간다
        while temp is not None:
            if data > temp.data:  # 삽입하려는 데이터가 현재 노드 데이터보다 크다면
                # 오른쪽 자식이 없으면 새로운 노드를 현재 노드 오른쪽 자식으로 만듦
                if temp.right_child is None:
                    new_node.parent = temp
                    temp.right_child = new_node
                    return
                # 오른쪽 자식이 있으면 오른쪽 자식으로 간다
                else:
                    temp = temp.right_child
            else:  # 삽입하려는 데이터가 현재 노드 데이터보다 작다면
                # 왼쪽 자식이 없으면 새로운 노드를 현재 노드 왼쪽 자식으로 만듦
                if temp.left_child is None:
                    new_node.parent = temp
                    temp.left_child = new_node
                    return
                # 왼쪽 자식이 있다면 왼쪽 자식으로 간다
                else:
                    temp = temp.left_child
```

### 테스트 코드
작성한 코드가 제대로 돌아가는지 확인해 볼게요.
```python
# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 이진 탐색 트리 출력
bst.print_sorted_tree()
```

### 실습 결과
```
2
3
4
5
7
8
9
11
14
17
19
```

[main3_05.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/30b51af7659c54f7eac05855fa3a52e1b49bc643/Data%20Structure/2%20Tree/3%20Binary%20Search%20Tree/main3_05.py) 참고

<br/><br/>

## 06. 이진 탐색 트리 탐색

탐색: 저장한 데이터를 찾는 연산  
- 특정 데이터를 갖는 노드를 리턴하는 연산  

루트 노드부터 시작해서, 찾고자 하는 데이터가 현재 노드보다 작으면 왼쪽, 크면 오른쪽으로 이동하며 찾는다
1. root 노드에서 시작
2. 주어진 노드의 데이터와 탐색하려는 데이터 비교
3. 탐색하려는 데이터가 더 크면 노드의 오른쪽 자식으로 간다
4. 탐색하려는 데이터가 더 작으면 노드의 왼쪽 자식으로 간다
5. 찾을 때까지 2~4 반복
6. 탐색하려는 노드를 찾으면 리턴한다

### 탐색 시간 복잡도
트리의 높이를 h라고 하면, 가장 깊은 노드를 찾는 경우 시간이 가장 오래 걸림  
탐색 시간 복잡도: $O(h + 1) = O(h)$

<br/><br/>

## 07. 이진 탐색 트리 탐색 구현

### 실습 설명
이번 과제에서는 이진 탐색 트리 탐색 연산을 구현해 볼게요.

탐색 연산을 일반화하면 이렇게 나타낼 수 있었는데요.  
1. root 노드부터 노드의 데이터와 탐색하려는 데이터를 비교합니다.
2. 탐색하려는 데이터가 더 크면 노드의 오른쪽 자식으로, 작으면 왼쪽 자식으로 갑니다.
3. 데이터를 찾을 때까지 위 단계들을 반복합니다.

BinarySearchTree 클래스의 search() 메소드를 써서 탐색 연산을 구현해 볼게요. search는 self 이외에 파라미터로 data를 받고, 트리 안에서 data를 갖는 노드를 찾아서 리턴합니다. data를 갖는 노드가 트리에 없으면 None을 리턴합니다.

### 실습 결과
```
7
19
2
None
```

<br/><br/>

### 해설
삽입할 때와 마찬가지로 temp 변수를 이용해서 원하는 노드를 찾아갈 건데요. root 노드로 초기화합니다.
```python
temp = self.root  # 탐색용 변수, root 노드로 초기화
```
반복문을 이용해서 탐색을 합니다.
```python
# 원하는 데이터를 갖는 노드를 찾을 때까지 돈다
while temp is not None:
```
반복문을 돌면서 data와 temp의 데이터를 계속 비교할 건데요. 세 가지 경우가 있겠죠?  
1. data == temp.data
2. data < temp.data
3. data > temp.data

```python
# 원하는 데이터를 갖는 노드를 찾을 때까지 돈다
while temp is not None:
    # 원하는 데이터를 갖는 노드를 찾으면 리턴
    if data == temp.data:
        return temp
    # 원하는 데이터가 노드의 데이터보다 크면 오른쪽 자식 노드로 간다
    if data > temp.data:
        temp = temp.right_child
    # 원하는 데이터가 노드의 데이터보다 작으면 왼쪽 자식 노드로 간다
    else:
        temp = temp.left_child
```
원하는 데이터를 갖는 노드를 찾으면 해당 노드를 리턴합니다.

원하는 데이터가 temp의 데이터보다 크면 오른쪽 자식으로 가서 다시 탐색합니다. (새로운 temp로 반복문이 다시 돌아간다.)

원하는 데이터가 temp의 데이터보다 작으면 왼쪽 자식으로 가서 다시 탐색합니다. (새로운 temp로 반복문이 다시 돌아간다.)

반복문이 끝날 때까지 원하는 노드를 찾지 못했다는 건 트리 안에 원하는 데이터를 갖는 노드가 없다는 뜻이겠죠? 이때는 그냥 None을 리턴합니다.  
```python
    return None
```

### 모범 답안
코드를 정리하면 이렇게 되겠죠? (코드가 너무 길어서 search() 메소드만 보여드립니다.)
```python
def search(self, data):
    """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다"""
    temp = self.root  # 탐색용 변수, root 노드로 초기화

    # 원하는 데이터를 갖는 노드를 찾을 때까지 돈다
    while temp is not None:
        # 원하는 데이터를 갖는 노드를 찾으면 리턴
        if data == temp.data:
            return temp
        # 원하는 데이터가 노드의 데이터보다 크면 오른쪽 자식 노드로 간다
        if data > temp.data:
            temp = temp.right_child
        # 원하는 데이터가 노드의 데이터보다 작으면 왼쪽 자식 노드로 간다
        else:
            temp = temp.left_child

    return None # 원하는 데이터가 트리에 없으면 None 리턴
```

### 테스트 코드
코드가 제대로 돌아가는지 확인해 볼게요.
```python
# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 노드 탐색과 출력
print(bst.search(7).data)
print(bst.search(19).data)
print(bst.search(2).data)
print(bst.search(20))
```

### 실습 결과
```
7
19
2
None
```
원하는 노드가 있으면 잘 찾아오고, 없으면 None을 리턴하는 걸 확인할 수 있습니다.

[main3_07.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/d1f761601f723e4db82d15a85ed3ea5f746aaa93/Data%20Structure/2%20Tree/3%20Binary%20Search%20Tree/main3_07.py) 참고

<br/><br/>

## 08. find_min 메소드

### 실습 설명
이번 실습에서 다룰 메소드는 이진 탐색 트리의 기본 연산은 아닌데요. 좀 색다른 연산입니다. 이진 탐색 트리에서 가장 작은 노드를 찾아주는 메소드죠.

정적 메소드 find_min()은 파라미터로 node를 받습니다. node를 뿌리로 갖는 부분 트리 안에서 가장 작은 노드를 리턴해 주죠. 이게 무슨 말인지 조금 헷갈리실 수 있으신데요.

예를 들어서 이런 이진 탐색 트리가 있다고 합시다. 그럼 find_min() 메소드의 파라미터로 root 노드를 리턴해 주면 트리 전체에서 가장 작은 노드가 리턴되는 거죠. 여기서는 1이 저장된 노드겠죠? 5가 저장된 노드를 find_min() 메소드의 파라미터로 넘기면 이 노란색 박스 안에 있는 부분 트리 안에서 가장 작은 노드, 그러니까 이번에도 1이 저장된 노드가 리턴됩니다. 하나만 더 볼게요. 14가 저장된 노드를 find_min() 메소드의 파라미터로 넘기면 이 빨간색 박스 안에 있는 부분 트리 안에서 가장 작은 노드 12가 리턴됩니다.

![image](https://bakey-api.codeit.kr/files/2398/CA3pKj?name=1.png)  
주어진 노드를 뿌리로 갖는 부분 트리에서 가장 작은 노드를 리턴해 주는 정적 메소드 find_min()을 완성해 보세요!

### 실습 결과
```
2
8
```

<br/><br/>

### 해설
먼저 이번에도 도우미 변수 temp를 정의합니다. 맨 처음에는 파라미터로 받은, 부분 트리의 root 노드로, 초기화합니다.
```python
temp = node  # 도우미 변수. 파라미터 node로 초기화
```
temp보다 작은 노드가 있으면 어디 있을까요? 이진 탐색 트리의 속성을 생각해 보세요. temp의 왼쪽 부분 트리에 있겠죠? 그럼 temp의 왼쪽 자식으로 내려갑니다. (temp = temp.left_child) 이런 식으로요.

그럼 새로운 temp보다 작은 노드가 있으면 어디 있을까요? 이때도 temp의 왼쪽 부분 트리에 있습니다. 또 temp의 왼쪽 자식으로 내려갑니다.

언제 더 이상 temp보다 작은 노드가 없다고 확신할 수 있을까요?

바로 temp가 더 이상 왼쪽 자식이 없을 때입니다. 바로 그때의 temp가 파라미터 node를 뿌리로 갖는 부분 트리에서 가장 작은 노드라고 확신할 수 있습니다. 코드로 나타내면 이렇게 되죠.
```python
# temp가 node를 뿌리로 갖는 부분 트리에서 가장 작은 노드일 때까지 왼쪽 자식 노드로 간다
while temp.left_child is not None:
    temp = temp.left_child
```
더이상 왼쪽 자식이 없을 때 while문을 빠져나와서 현재 temp에 저장된 노드를 리턴하면 되겠죠?
```python
    return temp
```

### 모범 답안
코드를 정리하면 이렇게 됩니다 (전체 코드가 너무 길어서 find_min() 메소드만 보여드립니다)
```python
@staticmethod
def find_min(node):
    """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
    # 코드를 쓰세요
    temp = node  # 도우미 변수. 파라미터 node로 초기화

    # temp가 node를 뿌리로 갖는 부분 트리에서 가장 작은 노드일 때까지 왼쪽 자식 노드로 간다
    while temp.left_child is not None:
        temp = temp.left_child      

    return temp  
```

### 테스트 코드
코드가 제대로 돌아가는지 확인해 볼게요.
```python
# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

print(bst.find_min(bst.root).data)  # 전체 이진 탐색 트리에서 가장 작은 노드
print(bst.find_min(bst.root.right_child).data)  # root 노드의 오른쪽 부분 트리에서 가장 작은 노드
```

### 실습 결과
결과가 원하는 대로 나오는 걸 확인할 수 있습니다.
```
2
8
```

[main3_08.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/74e2a827f595b217e573d0b78ad6c0315f0d659f/Data%20Structure/2%20Tree/3%20Binary%20Search%20Tree/main3_08.py) 참고

<br/><br/>

23.01.27

## 09. 이진 탐색 트리 삭제 I
- 삭제하려는 데이터를 갖는 노드를 먼저 찾아야 됨
- 경우 1: 삭제하려는 데이터가 leaf 노드의 데이터일 때
    - leaf 노드, 즉 삭제하려는 노드 부모 노드의 왼쪽(혹은 오른쪽) 자식 노드 레퍼런스를 None으로 지정
- 경우 2: 삭제하려는 데이터 노드가 하나의 자식 노드만 있을 때
    - 삭제하려는 노드의 자식 노드가 부모 노드의 자리를 차지하면 됨
    - 삭제하려는 노드의 부모 노드의 자식 노드 레퍼런스를 삭제하려는 노드의 자식 노드로 지정하고,
    - 삭제하려는 노드의 자식 노드의 부모 노드 레퍼런스를 삭제하려는 노드의 부모 노드로 지정하면 됨