# 2 그래프 탐색

23.02.06

## 01. 그래프 탐색이란?
- 하나의 시작점 노드에서 연결된 노드들을 모두 찾는 것
- 그래프 순회라고도 함
- 너비 우선 탐색(BFS, Breadth First Search)와 깊이 우선 탐색(DFS, Depth First Search)이 있음

## 02. BFS(Breadth First Search) 개념
- 그래프를 너비 우선적으로 탐색
- 그래프를 수평적으로 탐색 

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
