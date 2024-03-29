# 2 그래프 탐색

23.02.06

## 01. 그래프 탐색이란?
- 하나의 시작점 노드에서 연결된 노드들을 모두 찾는 것
- 그래프 순회라고도 함
- 너비 우선 탐색(BFS, Breadth First Search)와 깊이 우선 탐색(DFS, Depth First Search)이 있음

## 02. BFS(Breadth First Search) 개념
- 그래프를 너비 우선적으로 탐색
- 하나의 노드에 인접한 모든 노드를 우선적으로 탐색하고 다음 노드로 넘어가는 방법 

## 03. 큐
- BFS 알고리즘에서 큐가 굉장히 중요한 역할을 함
- FIFO 구조
- python에서는 deque로 구현

## 04. BFS 알고리즘
- 시작 노드를 방문 표시 후, 큐에 넣음
- 큐에 아무 노드가 없을 때까지:
    - 큐 가장 앞 노드를 꺼낸다
    - 꺼낸 노드에 인접한 노드들을 모두 보면서:
        - 처음 방문한 노드면:
            - 방문한 노드 표시를 해준다
            - 큐에 넣어준다

## 05. BFS로 연결된 역 찾기

[main2_05.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/353558ffcd0136a3001d25b66ce1b0c5324d89c7/Data%20Structure/3%20Graph/2%20Graph%20Search/main2_05.py) 참고

## 06. BFS 알고리즘 시간 복잡도 분석

### 정리
전처리: $O(V)$  
큐에서 노드 넣고 빼기: $O(V)$  
인접한 노드들을 도는데 걸리는 시간: $O(E)$  

이걸 다 더해보면 $O(2V + E)$인데, 앞의 2는 무시해도 되니까 총 $O(V + E)$의 시간 복잡도가 걸린다고 할 수 있습니다.

## 07. DFS(Depth First Search) 개념
- 그래프를 깊이 우선적으로 탐색
- 하나의 노드에서 시작해서 최대한 깊이, 멀리 가는 탐색 방법

## 08. 스택
- DFS 알고리즘에서 스택이 굉장히 중요한 역할을 함
- LIFO 구조
- python에서는 deque로 구현

## 09. DFS 알고리즘
- 시작 노드를 옅은 회색 표시 후, 스택에 넣음
- 스택에 아무 노드가 없을 때까지:
    - 스택 가장 위 노드를 꺼낸다
    - 노드를 방문 (진한 회색) 표시한다
    - 인접한 노드들을 모두 보면서:
        - 처음 방문하거나 스택에 없는 노드면:
            - 옅은 회색 표시를 해준다
            - 스택에 넣어준다

## 10. DFS로 연결된 역 찾기
[main2_10.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/fededdb3cb85cdb7578ccdf15806759138020f3d/Data%20Structure/3%20Graph/2%20Graph%20Search/main2_10.py) 참고

## 11. DFS 알고리즘 시간 복잡도 분석

### 정리
전처리: $O(V)$  
스택에서 노드 넣고 빼기: $O(V)$  
인접한 노드들을 도는데 걸리는 시간: $O(E)$  

이걸 다 더해보면 $O(2V + E)$인데요. 앞에 2는 무시해도 되니까 총 $O(V + E)$의 시간 복잡도가 걸린다고 할 수 있습니다.
