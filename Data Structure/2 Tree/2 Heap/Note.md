# 2 힙

23.01.18  

## 01. 힙이란?  

### 힙
두 개의 조건을 만족하는 트리  
1. 형태 속성: 힙은 완전 이진 트리이다(높이: $O(lg(n))$  
2. 힙 속성: 모든 노드의 데이터는 자식 노드들의 데이터보다 크거나 같다  

힙을 활용하는 두 가지 방법  
1. 정렬 문제 해결  
2. 우선순위 큐 구현

<br/><br/>

## 02. 정렬 문제  

### 정렬
- 여러 개의 데이터 요소들을 특정 순서로 배치하는 것  
- 예시)
```python
[4, 1, 6, 2, 8, 5]

[1, 2, 4, 5, 6, 8]  # 오름차순 정렬

[8, 6, 5, 4, 2, 1]  # 내림차순 정렬
```

### 정렬 알고리즘: 데이터를 재배치하는 구체적인 방법  
- 삽입 정렬
- 선택 정렬
- 퀵 정렬
- 합병 정렬
등

### 힙 정렬  
힙을 사용한 정렬 알고리즘  

<br/><br/>

## 03. 배열로 구현한 힙  

### 힙 구현하기

완전 이진 트리는 동적 배열, 파이썬에서는 리스트를 이용해 나타낼 수 있음  
힙도 완전 이진 트리이기 때문에 동적 배열로 나타냄  
![image](https://user-images.githubusercontent.com/71001479/213174986-07cfcb37-cdf3-4482-b383-26e77817ea88.png)

왼쪽 자식 인덱스: 인덱스 * 2  
오른쪽 자식 인덱스: 인덱스 * 2 + 1  

<br/><br/>

## 04. 힙 만들기 I  

![image](https://user-images.githubusercontent.com/71001479/213175569-e65f6921-16f2-4ce9-b738-bd6dc293dce4.png)

이 트리가 힙 속성을 지키려면 어떻게 해야 할까?  

1. 노드2의 데이터 5와 자식 노드들의 데이터 14, 9를 비교한다  
2. 왼쪽 자식의 데이터 14가 제일 크니 5와 바꿔준다
3. 부모 노드의 데이터가 14가 됐고, 자식 노드들은 부모 노드보다 작아졌다  
4. 그 다음으로 위치를 바꿔준 5가 힙 속성을 지키고 있는지 확인한다  
5. 5와 자식 노드들을 비교해서 가장 큰 11을 5와 바꿔준다  
6. 이렇게 힙 속성을 지키지 않는 노드가 있을 때마다 그 노드가 맞는 위치를 찾을 때까지 재배치한다  

이런 방법을 **heapify**라고 함  
일반화해서, heapify는 파라미터로 노드 하나를 받음  
부모 노드, 왼쪽 자식, 오른쪽 자식 중에 가장 큰 것을 고름  
가장 큰 노드가 부모 노드가 아니라면 가장 큰 노드를 부모 노드와 바꿔줌  
부모 노드가 가장 크면 아무것도 안 해도 됨  
기존의 부모 노드가 밑으로 갔는데, 그 노드가 또 힙 속성을 어길 수 있음  
힙 속성이 충족될 때까지 반복함  

#### 시간 복잡도
최악의 경우: 루트 노드가 가장 작아서, 계속 밑으로 내려가서 leaf 노드까지 내려가는 경우  
이 경우 노드는 트리의 높이만큼 데이터를 비교하고 재배치한다  
힙은 완전 이진 트리이기 때문에 높이가 $O(lg(n))$이기 때문에 최악의 경우 시간 복잡도도 마찬가지로 $O(lg(n))$  

<br/><br/>

## 05. heapify 함수 구현

### 실습 설명
이번 과제에서는 heapify() 함수를 직접 구현해 볼게요. 혹시 heapify() 함수가 무슨 작업을 하는지 정확히 이해가 안 되신 분은 이전 영상을 다시 보고 오세요.

heapify() 함수는 아래 세 가지 파라미터를 받습니다.
- 완전 이진 트리를 나타내는 리스트, tree
- heapify 하려는 노드의 인덱스, index
- 트리로 사용하는 리스트의 길이, tree_size (배열의 0번째 인덱스는 None으로 설정했기 때문에 실제로 총 노드 수보다 1이 큽니다.)

그리고 파라미터로 받은 tree의 index번째 노드가, 힙 속성을 유지하도록 트리 안의 노드들을 재배치합니다. (앞으로 “index" 번째 노드는 그냥 줄여서 “노드 index"라고 하겠습니다.)

heapify() 함수가 이런 기능을 하려면 아래와 같은 상세 작업을 순서대로 해야 합니다.

1. 부모 노드(heapify하려는 현재 노드), 왼쪽 자식 노드, 오른쪽 자식 노드, 이 3가지 노드 중에서 가장 큰 값을 가진 노드가 무엇인지 파악합니다.
2. (1)가장 큰 값을 가진 노드가 부모 노드라면 그 상태 그대로 둡니다. (2)가장 큰 값을 가진 노드가 자식 노드 중에 있다면 그 자식 노드와 부모 노드의 위치를 바꿔 줍니다.
3. 기존의 부모 노드가 자식 노드로 내려갔을 때, 다시 힙 속성을 어길 수도 있습니다. 힙 속성이 충족될 때까지 1~2 단계를 반복합니다.

이때 단계 2-(2)를 보면 heapify() 함수 내에는 두 노드의 위치를 바꿀 수 있는 기능이 필요하다는 걸 알 수 있습니다. 이런 기능을 하는 swap() 이라는 함수를 미리 작성해 뒀는데요. swap() 함수는 아래 두 가지 파라미터를 받습니다.
- 리스트로 구현한 완전 이진 트리, tree
- 두 인덱스, index_1과 index_2

그리고 트리 내에서 두 인덱스에 해당하는 두 노드의 위치를 바꿔주죠. heapify() 함수의 내부 코드를 작성할 때 swap() 함수를 사용해 보세요.

### 실습 결과
```
[None, 15, 14, 12, 11, 9, 10, 6, 2, 5, 1]
```

<br/><br/>

### 해설
먼저 heapify()의 첫 번째 단계를 어떻게 할 수 있을지 생각해 봅시다.

1. 부모 노드(heapify하려는 현재 노드), 왼쪽 자식 노드, 오른쪽 자식 노드, 이 3가지 노드 중에서 가장 큰 값을 가진 노드가 무엇인지 파악합니다.

```python
largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

# 왼쪽 자식 노드의 값과 비교
if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
    largest = left_child_index
```

largest 변수에는 3가지 노드 중 가장 큰 값을 가진 노드의 인덱스를 저장할 건데요. 일단은 부모 노드의 데이터가 가장 크다고 설정합니다.

그래서 처음에 largest 변수에는 부모 노드의 인덱스가 저장돼 있습니다.

그 다음 부모 노드의 값을 왼쪽 자식 노드의 값과 비교합니다. 여기서 아래 내용들을 확인합니다.

1. 먼저 왼쪽 자식 노드가 있는지, 없는지부터 확인한다.(왼쪽 자식 노드의 인덱스가 유효한 범위 내에 있는지 확인) 0 < left_child_index < tree_size
2. 왼쪽 자식 노드의 값이 부모 노드의 값보다 큰지 확인한다. tree[largest] < tree[left_child_index]
3. 왼쪽 자식 노드의 값이 더 큰 경우에는 largest 변수에 왼쪽 자식 노드의 인덱스를 저장한다.

그 다음, 같은 방식으로 largest의 값과 오른쪽 자식 노드의 값을 비교합니다.
```python
# 오른쪽 자식 노드의 값과 비교
if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
    largest = right_child_index
```

이 과정을 거치고 나면 이제 largest 변수에는 아래 세 가지 노드 중 최댓값을 가진 노드의 인덱스를 갖게 됩니다.
- 부모 노드(heapify하려는 현재 노드)
- 왼쪽 자식 노드
- 오른쪽 자식 노드

이때 최댓값을 가진 노드가 부모 노드라면 아무런 작업을 하지 않아도 됩니다. 이미 힙 속성을 만족하고 있으니까요. 하지만 최댓값을 가진 노드가 왼쪽 자식 노드이거나 오른쪽 자식 노드라면 아래 코드를 수행해야 합니다.
```python
if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
    swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
    heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를 대상으로 또 heapify 함수를 호출한다
```
위의 코드를 해석하면 다음과 같습니다.
  (1) 부모 노드와 최댓값을 가진 노드의 위치를 바꿔 준다.
  (2) 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를 대상으로 또 heapify() 함수를 호출한다.

즉, heapify() 함수는 재귀 함수인 겁니다. 이렇게 하면 heapify하려고 했던 최초의 부모 노드는 힙 속성을 만족할 때까지 그 위치가 변경되어 갈 겁니다.

### 모범 답안
코드를 정리하면 이렇게 되겠죠?
```python
def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다
```

### 테스트 코드
코드가 제대로 작동하는지 확인해 봅시다.
```python
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree)
```

### 실습 결과
```
[None, 15, 14, 12, 11, 9, 10, 6, 2, 5, 1]
```

완전 이진 트리의 노드 2(값이 5인 노드)의 위치가 힙 속성을 만족하는 곳으로 잘 바뀝니다.

[main2_05.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/1bdd680ae6e7db6016292be940f99f80a65dfbac/Data%20Structure/2%20Tree/2%20Heap/main2_05.py) 참고

<br/><br/>

23.01.20

## 06. 힙 만들기 II

### heapify
heapify 함수에 어떤 노드를 넣어주면 어떻게 될까?  
파라미터로 넘기는 노드가 힙 속성을 지킬 수 있도록 힙에서 위치를 찾아간다  
(leaf 노드는 heapify 해도 자식 노드가 없기 때문에 위치가 바뀌지 않음)  

마지막 노드부터 루트 노드까지 heapify를 차례로 적용하면, 위쪽 노드를 heapify할 때 그 노드를 루트 노드로 하는 부분 트리는 힙 속성 이미 지키고있음(heapify 이미 했기 때문)  

완전 이진 트리가 파이썬 리스트로 구현되어 있을 때, 마지막 인덱스부터 첫 인덱스까지 차례로 heapify를 호출하면, heap으로 만들 수 있음.  

heapify의 시간 복잡도는 $O(lg(n))$, 트리의 노드 개수 $(n)$만큼 반복, 따라서

### 힙을 만드는 데 걸리는 시간: $O(nlg(n))$  

<br/><br/>

## 07. 힙 정렬

### 힙 정렬
- 힙을 이용한 정렬 알고리즘!  
- 힙을 만든다
- root와 마지막 노드를 바꿔준다
- (바꾼 노드는 없는 노드 취급한다)
- 새로운 노드가 힙 속성을 지킬 수 있게 heapify 호출
- 모든 인덱스를 돌 때까지 반복
- Q. 내림 차순으로 정렬하고 싶으면?
- A. 힙 속성을 반대로 바꾸고 똑같은 알고리즘을 적용하면 된다!

<br/><br/>

## 08. 힙 정렬 구현하기

### 실습 설명
이번 과제에서는 영상에서 본 힙 정렬을 직접 구현해 볼게요.

어떤 리스트 하나가 있다고 합시다. 이때 그 리스트를 힙 정렬하려면 아래 과정들을 거치면 됩니다.
1. 먼저 리스트를 힙으로 만듭니다.
2. root 노드와 마지막 노드의 위치를 바꿉니다. 마지막 위치로 간 기존의 root 노드는 이제 힙에서 없다고 가정합니다.
3. 새로운 root 노드가 힙 속성을 지킬 수 있게 heapify합니다.
4. 힙에 남아있는 노드가 없도록 단계 2 ~ 3을 반복합니다.

힙 정렬을 하기위해 heapsort()라는 함수를 구현해 볼게요. heapsort() 함수는 정렬할 리스트를 tree라는 파라미터로 받아서 힙 정렬합니다. 이때 저번 과제에서 완성한 heapify() 함수를 사용할게요.

### 실습 결과
```
[None, 1, 1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 10]
```

<br/><br/>

### 해설

#### 힙 만들기

힙 정렬을 하려면 파라미터로 받은 리스트, tree를 먼저 힙으로 만들어야 합니다.  
힙을 만드는 방법, 생각나시나요? 가장 마지막 위치의 노드부터 root 노드까지 역순으로 heapify해 주면 됩니다. (왜 그래야 하는지 기억이 안 나시면 이전 영상 힙 만들기 II 를 다시 보고 오세요)  

이것을 코드로 작성하면 아래와 같습니다.
```python
# 마지막 노드부터 root 노드까지 heapify를 해준다 
for index in range(tree_size-1, 0, -1):
    heapify(tree, index, tree_size)
```
이 코드가 실행되고 나면 리스트 tree는 힙이 됩니다.

#### 힙 정렬
그 다음에는 힙 정렬을 위한 아래의 나머지 단계들을 수행하면 됩니다.
1. root 노드와 마지막 노드의 위치를 바꿉니다. 마지막 위치로 간 기존의 root 노드는 이제 힙에서 없다고 가정합니다.
2. 새로운 root 노드가 힙 속성을 지킬 수 있게 heapify합니다.
3. 힙에 남아있는 노드가 없도록 단계 2 ~ 3을 반복합니다.  

먼저 2 단계는 아래와 같이 코드를 쓰면 됩니다.
```python
for i in range(tree_size-1, 0, -1):
    swap(tree, 1, i)  # root 노드와 마지막 인덱스를 바꿔준 후
    # 여기에 코드를 작성하세요
```
root 노드와 가장 마지막 노드의 위치를 계속 swap() 함수로 바꿔줍니다. 마지막 위치로 간 root 노드는 힙에서 없는 것으로 간주됩니다. 따라서 마지막 노드의 인덱스는 매번 1씩 줄어들게 됩니다.

root 노드와 가장 마지막 노드의 위치를 한번 바꾸고 난 후에는 남은 리스트가 다시 힙이 되도록 새로운 root 노드를 heapify해야 합니다. 이때 이미 맨 뒤에 있는 노드를 하나씩 무시하고, 나머지만 가지고 heapify를 하려면 어떻게 해야 할까요?

heapify() 함수의 파라미터 tree_size의 역할에 대해서 잘 생각해 보세요.
```python
def heapify(tree, index, tree_size):
```
tree_size는 현재 트리에 들어있는 노드의 수를 나타냅니다. heapify() 함수의 내용 일부를 다시 잠깐 볼까요?
```python
# 왼쪽 자식 노드의 값과 비교
if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
    largest = left_child_index

# 오른쪽 자식 노드의 값과 비교
if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
    largest = right_child_index
```
tree_size는 해당 인덱스가 유효한지, 그러니까 해당 인덱스에 노드가 존재하는지를 판단하는 기준으로 사용됩니다. 즉, 리스트에 아무리 많은 노드들이 있다고 해도 결국 heapify의 대상은 tree_size 값을 통해 결정됩니다. 이 사실을 잘 활용하면 될 것 같은데, 어떻게 하면 좋을까요?

매번 heapify()를 호출할 때, 파라미터 tree_size도 1씩 줄여가면 됩니다. 그럼 힙 맨 뒤 노드들을 하나씩 무시해가면서 heapify를 할 수 있습니다.

정리하면 아래 코드처럼 heapify() 함수를 호출하면 됩니다.
```python
# 마지막 인덱스부터 처음 인덱스까지
for i in range(tree_size-1, 0, -1):
    swap(tree, 1, i)  # root 노드와 마지막 인덱스를 바꿔준 후
    heapify(tree, 1, i)  # root 노드에 heapify를 호출한다
```
현재 i는 tree_size - 1부터 시작해서 계속 1씩 감소하는데요. 이 i를 heapify() 함수의 파라미터 tree_size로 넘겨주면 heapify() 함수가 인식하는 리스트의 크기가 매번 줄어듭니다. 즉, tree라는 전체 리스트의 사이즈는 그대로지만 실제로 heapify의 대상이 되는 리스트의 크기는 하나씩 줄어들게 되는 겁니다. 이렇게 하면 힙 맨 뒤 노드들은 하나씩 무시하고, 점점 더 작게 인식되는 리스트에서, 매번 새로운 root 노드를 heapify할 수 있겠죠?

### 모범 답안
작성한 코드를 정리해 볼게요.
```python
def heapsort(tree):
    """힙 정렬 함수"""
    tree_size = len(tree)

    # 마지막 인덱스부터 처음 인덱스까지 heapify를 호출한다 
    for index in range(tree_size-1, 0, -1):
        heapify(tree, index, tree_size)

    # 마지막 인덱스부터 처음 인덱스까지
    for i in range(tree_size-1, 0, -1):
        swap(tree, 1, i)  # root 노드와 마지막 인덱스를 바꿔준 후
        heapify(tree, 1, i)  # root 노드에 heapify를 호출한다
```

### 테스트 코드
힙 정렬 코드를 제대로 작성했는지 봅시다.
```python
# 실행 코드
data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
heapsort(data_to_sort)
print(data_to_sort)
```

### 실습 결과
```
[None, 1, 1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 10]
```
노드가 오름차순으로 정렬됩니다. 실제로 힙 정렬을 구현해보니 뿌듯하죠?

[main2_08.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/0dea9764ca328b9bbc683dfe4f408202cc915d8c/Data%20Structure/2%20Tree/2%20Heap/main2_08.py) 참고

<br/><br/>

23.01.21

## 09. 힙 정렬 시간 복잡도 + 평가  

### 힙 정렬 시간 복잡도
힙 정렬이 얼마나 효율적인 정렬 방법인지 알아볼게요. 힙 안에 있는 노드의 개수를 $n$이라고 했을 때 힙 정렬의 시간 복잡도는 어떻게 될까요? 힙 정렬의 각 단계를 보면서 생각해볼게요. 힙 정렬의 각 단계는 아래와 같은데요.
1. 먼저 리스트를 힙으로 만듭니다.
2. root 노드와 마지막 노드의 위치를 바꿉니다. 마지막 위치로 간 기존의 root 노드는 이제 힙에서 없다고 가정합니다.
3. 새로운 root 노드가 힙 속성을 지킬 수 있게 heapify합니다.
4. 힙에 남아있는 노드가 없도록 단계 2 ~ 3을 반복합니다.

1번째 단계인 리스트를 힙으로 만드는 데 걸리는 시간은 $O(nlg(n))$입니다. 그 이유는 이전 영상에서 배웠습니다. 한 번의 heapify를 할 때의 시간 복잡도가 $O(lg(n))$이고 노드의 수가 총 $n$개이므로 그렇다고 했었죠?

2번째 단계는 그냥 두 노드의 위치를 바꿔 주는 작업이기 때문에 노드의 개수 $n$과는 상관없이 항상 $O(1)$입니다.

3번째 단계는 새로운 root 노드에 heapify를 하는 겁니다. 이때의 시간 복잡도는 $O(lg(n))$이라고 했죠? 그럼 2번째 단계와 3번째 단계를 합치면 $O(lg(n)+1)$, 즉, $O(lg(n))$입니다.

4번째 단계는 2~3 단계를, 힙에 남아있는 노드가 없을 때까지 반복합니다. 힙에는 총 $n$개의 노드가 있으므로 2, 3, 4단계의 시간 복잡도를 종합하면 $O(nlg(n))$이라고 할 수 있겠네요.

정리하면
- 힙을 만드는 데 $O(nlg(n))$
- 만든 힙에서 매번 root 노드를 뽑고 남은 것들을 다시 힙으로 만들어주는 작업을 반복하는 데 $O(nlg(n))$이 걸립니다.

그럼 힙 정렬의 총 시간 복잡도는 $O(nlg(n)+nlg(n))$으로 $O(2nlg(n))$이고,  
시간 복잡도에서 상수는 무시되니까 결국 $O(nlg(n))$이라고 할 수 있습니다.

힙 정렬은 $O(nlg(n))$의 시간 복잡도를 가지는 정렬 알고리즘인 겁니다.

### 다른 정렬 알고리즘들과의 비교
다른 정렬 알고리즘들에 비해 이게 얼마나 빠른 건지 생각해봅시다. 아래 표에는 힙 정렬과 가장 대표적인 정렬 알고리즘 4개의 시간 복잡도가 있습니다.

| **정렬 알고리즘** |          **시간 복잡도**         |
|:-----------------:|:--------------------------------:|
|     선택 정렬     |             $O(n^2)$             |
|     삽입 정렬     |             $O(n^2)$             |
|     합병 정렬     |            $O(nlg(n))$           |
|      퀵 정렬      | 평균 $O(nlg(n))$ (최악 $O(n^2)$ ) |
|      힙 정렬      |            $O(nlg(n))$           |

힙 정렬은 선택 정렬과 삽입 정렬 $(O(n^2))$보다는 좋고, 합병 정렬과 퀵 정렬 $(O(nlg(n)))$과는 비슷한 성능을 내는 정렬 방법이라는 걸 알 수 있습니다.

<br/><br/>

23.01.22

## 10. 우선순위 큐

### 힙
힙은 대표적으로 두 가지 목적으로 사용됨.  
1. 정렬
2. 우선순위 큐 구현  

### 우선순위 큐
큐나 스택과 같은 추상 자료형  
추상자료형: 내부적인 구현보다 기능에 집중하게 해주는 개념  

원래 큐는 먼저 들어가면 먼저 나오는 FIFO  
우선순위 큐
- 데이터를 저장할 수 있다
- 저장한 데이터가 우선순위 순서대로 나온다
- 예시) 가장 큰 데이터가 우선순위가 가장 높으면 데이터가 큰 순서대로 나옴  
### 코드
```python
# 최대 우선순위 큐
priority_queue = MaxPrioirityQueue()

# 우선순위 큐에 데이터 삽입
priority_queue.add(5)
priority_queue.add(2)
priority_queue.add(7)
priority_queue.add(8)

# 우선순위 큐 데이터 추출(삭제)
print(priority_queue.pop())
print(priority_queue.pop())
print(priority_queue.pop())
print(priority_queue.pop())
```
### 출력 결과
```
8
7
5
2
```

우선순위가 가장 높은 데이터부터 처리하고 싶을 때 유용하게 쓸 수 있는 추상 자료형  
예시) 고객문의를 처리하는데, 가장 불만도가 높은 문의부터 처리하고 싶을 때, 고객등급이 높은 고객부터 처리하고 싶을 때 등  

힙을 이용하면 우선순위 큐를 효율적으로 구현할 수 있다!

<br/><br/>

23.01.23

## 11. 힙에 데이터 삽입하기  
1. 힙의 마지막 인덱스에 데이터를 삽입한다
2. 삽입한 데이터와 부모 노드의 데이터를 비교한다
3. 부모 노드의 데이터가 더 작으면 둘의 위치를 바꿔준다
4. 2~3의 과정을 새로 삽입한 노드가 제 위치를 찾을 때까지 반복한다 

<br/><br/>

## 12. 힙 데이터 삽입 구현하기

### 실습 설명
이번 과제에서는 힙에 데이터를 삽입하는 것을 구현해 볼게요.

먼저 우선순위 큐를 PriorityQueue라는 클래스로 정의하고 그 안에 힙을 두겠습니다.  
PriorityQueue 클래스에는 heap이라는 인스턴스 변수가 있고, 그것은 파이썬의 리스트를 가리킵니다. 가장 처음 heap에는 None이라는 원소 하나만 있는데요. 이제 이 힙에 데이터를 하나씩 삽입하려고 합니다.

힙에 데이터를 삽입하는 메소드의 이름은 insert()입니다. insert() 메소드는 데이터를 삽입할 때 리스트가 계속 힙의 속성을 유지하도록 하는 기능도 포함해야 합니다.

insert() 메소드로 데이터를 삽입할 때 이루어져야 하는 일을 순서대로 정리하면 아래의 3단계로 나눌 수 있습니다.

  1. 힙의 마지막 인덱스에 노드를 삽입합니다.

  2. (1)삽입한 노드와 그 부모 노드를 비교해서 부모 노드가 더 작으면 둘의 위치를 바꿉니다. (2)삽입한 노드와 그 부모 노드를 비교해서 부모 노드가 더 크면 그대로 둡니다.

  3. 2-(1)의 경우에는 삽입한 노드가 올바른 위치를 찾을 때까지 2 단계를 반복합니다.

이때 2 단계와 3 단계의 작업을 하는 별도의 함수 reverse_heapify()를 정의할게요.  
reverse_heapify 함수는 다음과 같은 파라미터를 받습니다.
- 리스트로 구현한 완전 이진 트리, tree
- 삽입된 노드의 인덱스, index

그리고 삽입된 노드를 힙 속성을 유지할 수 있는 위치로 이동시킵니다.

이전에 배운 heapify() 함수가 위에 있는 노드를 아래로 이동시켜서 힙 속성을 유지했다면 reverse_heapify() 함수는 아래에 있는 노드를 위로 이동시켜서 힙 속성을 유지하는 거죠.

reverse_heapify() 함수만 완성되면 insert() 메소드를 완성하는 건 간단해요.  
insert()  함수는 다음과 같은 파라미터를 받습니다.
- self
- 삽입하는 데이터, data

insert() 메소드는 (1) 리스트, heap의 마지막에 새로운 데이터를 삽입하고 (2) 그 마지막 인덱스를 reverse_heapify() 함수에 파라미터로 넘겨서 호출하면 됩니다.

### 실습 결과
```
[None, 13, 9, 11, 3, 6, 1, 10]
```

<br/><br/>

### 해설

#### reverse_heapify() 함수
reverse_heapify()  함수부터 써볼게요. heapify() 함수에서 했던 것처럼, 부모 노드의 값과 자식 노드의 값을 비교하면 되는데요.

게다가 reverse_heapify() 함수는 2개의 노드만 비교하면 되기 때문에 훨씬 간단하죠.
```python
def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    parent_index = index // 2  # 삽입된 노드의 부모 노드의 인덱스 계산

    # 부모 노드가 존재하고, 부모 노드의 값이 삽입된 노드의 값보다 작을 때
      if 0 < parent_index < len(tree) and tree[index] > tree[parent_index]:
          swap(tree, index, parent_index)  # 부모 노드와 삽입된 노드의 위치 교환
          reverse_heapify(tree, parent_index)  # 삽입된 노드를 대상으로 다시 reverse_heapify 호출  
```
먼저 아래처럼 부모 노드의 인덱스를 구합니다.
```python
parent_index = index // 2
```
그리고 아래 두 가지를 확인합니다.
- 부모 노드의 인덱스가 유효한지 즉, 부모 노드가 존재하는지
- 부모 노드의 값이, 삽입된 노드의 값보다 작은지

만약 부모 노드의 값이 더 작으면 swap() 함수를 써서 두 노드의 위치를 바꿔 줍니다. 그럼 새로 삽입된 노드가 부모 노드가 되겠죠. 그 노드의 인덱스를 파라미터로 넘겨서 다시 reverse_heapify()를 호출합니다.

reverse_heapify() 함수도 heapify() 함수 때처럼 재귀 함수인 겁니다.

#### PriorityQueue 클래스의 insert() 메소드
insert() 메소드는 인스턴스 변수 heap의 맨 뒤에 데이터를 추가하고, 그렇게 추가된 데이터(삽입된 노드)를 대상으로  reverse_heapify() 함수를 호출하면 됩니다.
```python
def insert(self, data):
    """삽입 메소드"""
    self.heap.append(data)  # 힙의 마지막에 데이터 추가
    reverse_heapify(self.heap, len(self.heap)-1)
```
간단하죠? 이렇게 하면 insert() 메소드로 데이터를 삽입할 때 리스트, heap은 언제나 힙 속성을 유지하게 됩니다.

### 모범 답안
위 코드를 하나로 정리해 볼게요.
```python
def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    parent_index = index // 2  # 삽입된 노드의 부모 노드의 인덱스 계산

    # 부모 노드가 존재하고, 부모 노드의 값이 삽입된 노드의 값보다 작을 때
    if 0 < parent_index < len(tree) and tree[index] > tree[parent_index]:
        swap(tree, index, parent_index)  # 부모 노드와 삽입된 노드의 위치 교환
        reverse_heapify(tree, parent_index)  # 삽입된 노드를 대상으로 다시 reverse_heapify 호출


class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙


    def insert(self, data):
        """삽입 메소드"""
        self.heap.append(data)  # 힙의 마지막에 데이터 추가
        reverse_heapify(self.heap, len(self.heap)-1) # 삽입된 노드(추가된 데이터)의 위치를 재배치


    def __str__(self):
        return str(self.heap)
```

### 테스트 코드
코드가 제대로 실행되는지 확인해 봅시다.
```python
# 테스트 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue)
```

### 실습 결과
```
[None, 13, 9, 11, 3, 6, 1, 10]
```
데이터가 일단 priority_queue (우선순위 큐)에 잘 삽입됩니다. 그리고 데이터를 출력해보니 데이터가 삽입될 때 priority_queue 내부에 있는 힙의 ‘힙 속성’을 유지하면서 저장되는 것을 알 수 있습니다.

[main2_12.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/9ee776a2c028a18af509475831434581e5164879/Data%20Structure/2%20Tree/2%20Heap/main2_12.py) 참고

<br/><br/>

23.01.24

## 13. 힙에서 최고 우선순위 데이터 추출하기

### 힙에서 root 노드 데이터 추출하기
가장 큰 숫자가 우선순위가 높다고 가정하고, 이를 추출하려고 할 때
- root 노드가 가장 큰 숫자이기에, root 노드의 데이터를 변수에 넣어두고, 마지막 노드와 교체
- 마지막 노드(가장 큰 숫자)를 힙에서 삭제
- root 노드가 가장 작은 숫자로 heap 속성을 지키지 않기 때문에, heapify 하여 힙 속성 지키게 함
- 변수에 저장해둔 가장 큰 노드를 return함

<br/><br/>

## 14. 힙 우선순위 데이터 추출 구현

### 실습 설명
이번 과제에서는 힙에서 가장 우선순위가 높은 데이터를 추출하는 함수를 구현해 볼게요.  
이전 영상에서 배운 데이터 추출의 과정을 정리해 보면 아래의 네 단계로 정리할 수 있습니다.  
1. root 노드와 마지막 노드의 위치를 바꿉니다.
2. 마지막 위치로 간 원래 root 노드의 데이터를 별도 변수에 저장하고, 노드는 힙에서 지웁니다.
3. 새로운 root 노드를 대상으로 heapify해서 망가진 힙 속성을 복원합니다.
4. 2단계에서 따로 저장해 둔 최우선순위 데이터를 리턴합니다.

이렇게 나타낼 수 있었는데요.

이 기능을 PriorityQueue 클래스의 extract_max()라는 메소드로 구현해 볼게요.

extract_max() 메소드는 파라미터로 self만 받고, heap에서 가장 우선 순위가 높은 데이터를 추출(지우면서 리턴)합니다.

**이번 과제에서는 PriorityQueue 클래스를 제외한 나머지 코드는 heapify_code.py 파일에 옮겨 놨습니다. 실제 코드 작성은 main.py에서 하시면 됩니다!**

### 실습 결과
```
13
11
10
9
6
3
1
```

<br/><br/>

### 해설
extract_max() 메소드는 다음 네 단계를 순서대로 구현하면 됩니다.  
1. root 노드와 마지막 노드의 위치를 바꿉니다.
2. 마지막 위치로 간 원래 root 노드의 데이터를 별도 변수에 저장하고, 노드는 힙에서 지웁니다.
3. 새로운 root 노드를 대상으로 heapify해서 망가진 힙 속성을 복원합니다.
4. 2단계에서 따로 저장해 둔 최우선순위 데이터를 리턴합니다.

아래 코드를 참고해 주세요.
```python
def extract_max(self):
    """최우선순위 데이터 추출 메소드"""
    swap(self.heap, 1, len(self.heap) - 1)  # root 노드와 마지막 노드의 위치 바꿈
    max_value = self.heap.pop()  # 힙에서 마지막 노드 추출(삭제)해서 변수에 저장
    heapify(self.heap, 1, len(self.heap))  # 새로운 root 노드를 대상으로 heapify 호출해서 힙 속성 유지
    return max_value  # 최우선순위 데이터 리턴
```
단계 순으로 다시 보여드릴게요.  
- 1단계
```python
swap(self.heap, 1, len(self.heap) - 1)  # root 노드와 마지막 노드의 위치 바꿈
```
- 2단계
```python
max_value = self.heap.pop()  # 힙에서 마지막 노드 추출(삭제)해서 변수에 저장
```
- 3단계
```python
heapify(self.heap, 1, len(self.heap))  # 새로운 root 노드를 대상으로 heapify 호출해서 힙 속성 유지
```
- 4단계
```python
return max_value  # 최우선순위 데이터 리턴
```

### 모범 답안
필요한 코드를 다 정리하면 이렇게 되겠죠?
```python
def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔 준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔 준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다


def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    parent_index = index // 2  # 삽입된 노드의 부모 노드의 인덱스 계산

    # 부모 노드가 존재하고, 부모 노드의 값이 삽입된 노드의 값보다 작을 때
    if 0 < parent_index < len(tree) and tree[index] > tree[parent_index]:
        swap(tree, index, parent_index)  # 부모 노드와 삽입된 노드의 위치 교환
        reverse_heapify(tree, parent_index)  # 삽입된 노드를 대상으로 다시 reverse_heapify 호출        


class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙

    def insert(self, data):
        """삽입 메소드"""
        self.heap.append(data)  # 힙의 마지막에 데이터 추가
        reverse_heapify(self.heap, len(self.heap)-1) # 삽입된 노드(추가된 데이터)의 위치를 재배치

    def extract_max(self):
        """최고 우선순위 데이터 추출 메소드"""
        swap(self.heap, 1, len(self.heap) - 1)  # root 노드와 마지막 노드의 위치 바꿈
        max_value = self.heap.pop()  # 힙에서 마지막 노드 추출(삭제)해서 변수에 저장
        heapify(self.heap, 1, len(self.heap))  # 새로운 root 노드를 대상으로 heapify 호출해서 힙 속성 유지
        return max_value  # 최우선순위 데이터 리턴

    def __str__(self):
        return str(self.heap)
```

### 테스트 코드
extract_max() 메소드가 제대로 작동하는지 확인해 볼게요.
```python
# 테스트 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
```

### 실습 결과
```
13
11
10
9
6
3
1
```
priority_queue(우선순위 큐)에서 데이터를 하나씩 추출해서 출력해 보니까 데이터가 내림차순으로 즉, 우선순위가 높은 순으로 추출되는 걸 볼 수 있습니다.

이제 우리는 priority_queue(우선순위 큐)에 새로운 데이터를 삽입하고 추출할 수 있습니다. 힙을 사용해서 마침내 완전한 하나의 우선순위 큐를 구현하는 데 성공한 겁니다!

[heapify_code.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/dffc53e52d2e243197a87d17c64a4f4f6675512b/Data%20Structure/2%20Tree/2%20Heap/heapify_code.py)  
[main2_14.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/dffc53e52d2e243197a87d17c64a4f4f6675512b/Data%20Structure/2%20Tree/2%20Heap/main2_14.py) 참고

<br/><br/>

## 15. 힙 삽입, 추출 시간 복잡도

### 힙의 삽입 연산 시간 복잡도
힙의 데이터(노드) 삽입의 시간 복잡도는 어떻게 될까요?

힙 안에 총 $n$개의 노드가 있다고 가정하고 데이터 삽입의 3단계를 다시 볼게요.

  1. 힙의 마지막 인덱스에 노드를 삽입합니다.
  2. (1)삽입한 노드와 그 부모 노드를 비교해서 부모 노드가 더 작으면 둘의 위치를 바꿉니다. (2)삽입한 노드와 그 부모 노드를 비교해서 부모 노드가 더 크면 그대로 둡니다.
  3. 2-1의 경우에는 삽입한 노드가 올바른 위치를 찾을 때까지 단계 2를 반복합니다.

- 1단계  
먼저 힙의 마지막에 노드를 삽입해야 합니다. 저희는 힙을 동적 배열로 구현했는데요. 동적 배열에 원소를 추가하는 것의 시간 복잡도를 분할 상환 분석하면 $O(1)$입니다.
- 2단계  
(1) 삽입된 노드의 값과 부모 노드의 값을 비교하는 건 $O(1)$이 걸립니다.  
(2) 삽입된 데이터가 더 큰 경우 부모 노드와의 위치를 바꿔주는 것도 마찬가지로 $O(1)$이 걸리죠.

즉, 2단계에서는 $O(2)$이 걸리는데 이건 $O(1)$과 같습니다.

- 3단계  
최악의 경우 2단계를 몇 번이나 반복해야할까요? 최악의 경우는 삽입한 데이터가 leaf 노드부터 시작해서 root 노드까지 올라가는 경우인데요. 그럼 힙의 높이만큼 2단계를 반복해야합니다. 힙의 높이는 $lg(n)$에 비례하니까 시간은 $O(lg(n))$입니다. 이 말은, 2단계의 시간인 $O(1)$를 최대 $O(lg(n))$번 반복할 수 있다는 말이니까 결국 시간 복잡도는 $O(lg(n))$이 걸립니다.

이것들을 모두 정리해보면

- 1단계의 $O(1)$
- 2단계, 3단계의 $O(lg(n))$

를 더해서 $O(1+lg(n))$이 되고 이건 곧 $O(lg(n))$과 같습니다.

결론적으로, 힙에 데이터(노드)를 삽입하는 연산의 시간 복잡도는 $O(lg(n))$입니다.

### 힙의 추출 연산 시간 복잡도
이제 힙에서 가장 우선 순위가 높은 데이터(노드)를 추출하는데 시간이 얼마나 걸리는지 알아봅시다. 이번에도 힙에 있는 노드의 개수를 $n$이라고 할게요.

단계별로 나눠서 봅시다.
1. root 노드와 마지막 노드의 위치를 바꿉니다.
2. 마지막 위치로 간 원래 root 노드의 데이터를 별도 변수에 저장하고, 노드는 힙에서 지웁니다.
3. 새로운 root 노드를 대상으로 heapify해서 망가진 힙 속성을 복원합니다.
4. 2단계에서 따로 저장해 둔 최우선순위 데이터를 리턴합니다.
- 1단계  
root 노드와 마지막 노드의 위치를 바꾸는 건 노드의 개수랑은 전혀 상관 없이 $O(1)$이 걸립니다.
- 2단계  
데이터를 변수에 지정하는 건 $O(1)$이 걸립니다. 저희는 힙을 동적 배열로 구현했는데요. 동적 배열에서 마지막 인덱스의 원소를 삭제하는 건 분할 상환 분석을 하면 $O(1)$이 걸립니다. 이 단계는 총 $O(1 + 1)$이 걸리니까 $O(1)$이 걸리는 겁니다.
- 3단계  
새로운 root 노드를 대상으로 heapify를 호출해서 망가진 힙 속성을 복원하는 단계입니다. 이전에 heapify는 $O(lg(n))$가 걸린다고 배웠습니다.
- 4단계  
변수를 리턴하는 건 한 번에 할 수 있습니다. $O(1)$이죠.

총 걸리는 시간을 더하면 $O(1 + 1 + lg(n) + 1)$이네요. 여기서 1은 다 무시해도 되니까, 힙에서 가장 우선 순위가 높은 데이터를 추출하는 연산의 시간 복잡도는 $O(lg(n))$인 겁니다.

<br/><br/>

## 16. 힙으로 구현한 우선순위 큐 평가

우선순위 큐를 구현할 때는 힙 말고도 다른 자료 구조들을 활용할 수도 있습니다. 예를 들어  
- 정렬된 동적 배열
- 정렬된 더블리 링크드 리스트  
으로도 우선순위 큐를 구현할 수 있는데요. 이번 레슨에서는 이 방법들을 사용하는 것과 힙을 사용하는 걸 한 번 비교해볼게요.

### 정렬된 동적 배열
먼저 정렬된 동적 배열부터 봅시다. 정렬된 동적 배열으로도 우선순위 큐를 구현할 수 있습니다. 데이터를 삽입하거나 추출해도, 동적 배열이 늘 정렬된 상태를 유지하게 하면 되는데요.

일단 동적 배열에 데이터가 정렬된 채(오름차순 또는 내림차순)로 있다고 가정하고 새로운 데이터를 삽입할 때를 생각해봅시다. 새로운 데이터를 정렬된 동적 배열에 삽입하려면 크게 두 가지 작업을 해야합니다.

(1) 먼저 새로운 데이터가 어느 위치에 들어가야 하는지를 찾고  
(2) 그 위치에 데이터를 넣어야 합니다.  
  - 삽입할 위치를 찾는 것은 이진 탐색을 사용하면 $O(lg(n))$이 걸립니다.  
  - 그리고 그 위치에 데이터를 삽입하는 건 최악의 경우 $O(n)$이 걸립니다.  
예를 들어 \[3, 5, 6, 8, 9] 이런 동적 배열이 있다고 합시다. 여기에 1을 삽입하려면 맨 앞에 삽입해야 하고 그럼 기존의 3, 5, 6, 8, 9를 각각 한 인덱스씩 뒤로 밀어서 저장해야 합니다. 바로 이럴 때 $O(n)$이 걸리는 거죠.

그럼 삽입 연산은 총 $O(lg(n)+n)$ 이 걸리고 이는 곧 $O(n)$과 같습니다.

결국, 정렬된 동적 배열에 데이터를 삽입하는 연산은 $O(n)$이 걸립니다.

데이터를 추출하는 연산은 얼마나 걸릴까요? 동적 배열이 항상 정렬된 상태라면 가장 우선순위가 높은 데이터는 항상 배열의 끝에 있을 겁니다. 그래서 추출할 때는 그냥 마지막 데이터를 삭제함과 동시에 리턴하면 됩니다.

동적 배열 맨 뒤에 있는 데이터를 추출하는 연산은 $O(1)$이 걸립니다.

결국, 정렬된 동적 배열에서 가장 우선순위가 높은 데이터를 추출하는 연산은 $O(1)$이 걸립니다.

### 정렬된 더블리 링크드 리스트
이번엔 정렬된 더블리 링크드 리스트로 우선순위 큐를 구현한다고 생각해봅시다.

우선 데이터 삽입이 얼마나 걸릴까요? 일단 데이터를 삽입해야 하는 위치를 찾아야 하는데요. 링크드 리스트에서는 이럴 때 선형 탐색을 해야 합니다. 그러니까 헤드 노드에서부터 순서대로 하나씩 노드를 확인하면서 삽입할 위치를 찾아야 하는데요. 총 노드 수가 $n$이라고 했을 때, 최악의 경우 $n$개의 노드를 다 봐야 합니다.

예를 들어, | 3 | 5 | 6 | 8 | 9 | 이렇게 정렬된 더블리 링크드 리스트에서 10를 삽입하고 싶으면 선형 탐색으로 3부터 9까지를 다 확인해야 합니다.

9 뒤에 삽입해야 한다는 걸 알기 위해 $n$개의 노드를 다 봐야 하는 거죠. 그러니까 삽입할 위치를 찾는 단계는 $O(n)$ 이 걸립니다.

그러면 삽입은 얼마나 걸릴까요? 위치만 정해지고 나면 링크드 리스트에서 데이터를 삽입하는 건 $O(1)$에 할 수 있습니다.

결국, 정렬된 더블리 링크드 리스트에 데이터를 삽입하는 것은 $O(1 + n)$이 걸리고, 이건 $O(n)$과 같습니다.

그럼 데이터 추출은 얼마나 걸릴까요? 더블리 링크드 리스트에서 마지막 데이터를 추출하는 데에는 $O(1)$이 걸립니다.

결국, 정렬된 더블리 링크드 리스트에서 가장 우선순위가 높은 데이터를 추출하는 데 $O(1)$이 걸리는 거죠.

### 힙
힙으로 우선순위 큐를 구현했을 때는 어땠나요? 힙에 데이터를 삽입하는 연산과 추출하는 연산의 시간 복잡도는 모두 $O(lg(n))$이었습니다.

위 내용을 모두 정리하면 아래 표와 같습니다.
|                             |  **데이터 삽입**  |  **데이터 추출**  |
|:---------------------------:|:-----------------:|:-----------------:|
|       정렬된 동적 배열      |      $O(n)$     |      $O(1)$     |
| 정렬된 더블리 링크드 리스트 |      $O(n)$     |      $O(1)$     |
|              힙             | $O(lg(n))$ | $O(lg(n))$ |

우선순위를 사용할 때  
- 정렬된 동적 배열이나 정렬된 더블리 링크드 리스트를 사용하면 데이터를 추출할 때 더 효율적
- 힙을 사용하면 데이터를 삽입할 때 더 효율적  
이라는 것을 알 수 있습니다.

### 우선순위 큐는 뭐로 구현하는 게 가장 좋을까?
만약 새로운 데이터를 삽입할 일이 많으면 힙으로,  
기존 데이터를 추출할 일이 더 많으면 정렬된 동적 배열이나 정렬된 더블리 링크드 리스트로 구현하는 게 좋을 겁니다.

이렇게 우선순위 큐와 같은 어떤 추상 자료형을 구현할 때는 특정 방식이 항상 더 낫다고 단정하기 힘듭니다. 단지, 개발자가 처한 상황에 따라 정답이 달라질 뿐이고, 개발자는 이러한 것을 잘 판단해야겠죠.

<br/><br/>

## 17. 힙 퀴즈

질문 1  
다음 중 힙에 대한 설명으로 옳지 않은 것을 고르시오.  
1 힙은 형태 속성 (힙은 완전 이진 트리다), 그리고 힙 속성(힙의 모든 노드의 데이터는 항상 자식보다 크거나/같아야 한다)을 지키는 트리 자료 구조다.  
2 힙을 잘 이용하면 데이터를 정렬시킬 수 있다. 이 알고리즘을 힙 정렬이라고 부른다.  
3 힙은 “우선순위 큐”라는 추상 자료형을 구현하는데 사용할 수 있다.  
4 힙은 일반적으로  노드 클래스를 구현하고, 인스턴스를 만든 후, 이 인스턴스들을 서로 연결시켜서 구현한다.  
5 옳지 않은 내용 없음  

질문 2  
다음 중 힙 정렬과 힙으로 구현한 우선 순위 큐에 대한 내용으로 옳지 않은 것을 모두 고르시오.  
1 힙 정렬은 $O(nlg(n))$이 걸리는 알고리즘이다.  
2 힙 정렬은 합병 정렬, 퀵 정렬과 비교해서 더 효율적인 알고리즘이라고 할 수 있다.  
3 힙 정렬은 선택 정렬, 삽입 정렬과 비교해서 더 효율적인 알고리즘이라고 할 수 있다.  
4 힙으로 구현한 우선순위 큐의 삽입, 추출 연산은 모두 $O(lg(n))$이다.  
5 우선 순위 큐를 힙으로 구현할 때와, 정렬된 배열로 구현할 때, 그리고 정렬된 링크드 리스트로 구현할 때 시간 복잡도의 차이는 없다.  

<br/><br/>

### 해설

질문 1  
정답 4  
퀴즈 해설: 힙은 형태 속성 때문에 항상 완전 이진 트리입니다. 그렇기 때문에 일반적으로 배열, 또는 파이썬 리스트를 써서 구현합니다.

질문 2  
정답 2, 5  
퀴즈 해설:  
2: 힙 정렬, 합병 정렬, 그리고 퀵 정렬은 모두 (평균)시간 복잡도가 $O(nlg(n))$입니다. 시간 복잡도 상으로는 세 알고리즘 모두 비슷하게 효율적인 거죠.  
5: 우선순위 큐를 정렬된 동적 배열, 정렬된 링크드 리스트, 그리고 힙으로 구현했을 때, 각 연산들의 시간 복잡도는 아래 표와 같습니다.  
|                             |  **데이터 삽입**  |  **데이터 추출**  |
|:---------------------------:|:-----------------:|:-----------------:|
|       정렬된 동적 배열      |      $O(n)$     |      $O(1)$     |
| 정렬된 더블리 링크드 리스트 |      $O(n)$     |      $O(1)$     |
|              힙             | $O(lg(n))$ | $O(lg(n))$ |  

힙과 다른 자료 구조들의 시간 복잡도가 다르다는 걸 알 수 있죠?
