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