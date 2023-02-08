# 3 최단 경로 알고리즘

23.02.07

## 01. 최단 경로 알고리즘이란?

### 최단 경로(Shortest Path)
- 두 노드 사이 경로 중 가장 거리가 짧은 경로

### 최단 경로 알고리즘
- 최단 경로를 구하는 구체적인 방법들
- 그래프의 종류와 특성에 따라 다양한 방법이 있음
- BFS, Dijkstra 등

<br/><br/>

## 02. BFS predecessor
BFS는 원래 그래프를 탐색하는 방법이지만, 조금만 수정하면 최단 경로 알고리즘으로 만들 수 있음.  
노드에 visited 변수 외에 predecessor(~이전에 온 것) 변수 추가해줌.  
#### predecessor
- BFS를 할 때 특정 노드에 오기 직전의 노드  
- 시작 노드를 제외하고 각 노드에 predecessor 저장하면 최단 경로를 찾을 수 있음

<br/><br/>

## 03. 최단 경로용 BFS
- BFS를 하면서 각 노드가 어디에서 왔는지 predecessor를 저장해준다
- 원하는 경로의 시작점과 종착점이 주어지면, 종착점부터 시작점까지 predecessor를 따라간다
- 이를 뒤집으면 최단 경로가 된다
- Backtracking이라고 부름

### 최단 경로용 BFS
- 시작 노드를 방문 표시 후, 큐에 넣음
- 큐에 아무 노드가 없을 때까지:
  - 큐 가장 앞 노드를 꺼낸다
  - 꺼낸 노드의 인접한 노드들을 모두 보면서:
    - 처음 방문한 노드면:
      - 방문한 노드 표시를 해준다
      - predecessor 변수를 큐에서 꺼낸 노드로 설정
      - 큐에 넣어준다

### Backtracking
- 현재 노드를 경로에 추가한다
- 현재 노드의 predecessor로 간다
- predecessor가 없을 때까지 위 단계들 반복

<br/><br/>

## 04. BFS로 찾은 경로가 최단 경로인 이유
- BFS 알고리즘은 시작점에서 가장 가까이 있는 노드 순서대로 접근  
- 거리가 1인 노드를 모두 방문해야 그 다음에 거리가 2인 노드를 방문
- 만약 어떤 노드에 도착했다면, 가장 짧은 거리를 통해 접근한 것
- 만약 더 짧은 거리가 있었다면, 그 이전 거리 단계에서 접근했어야 함
- 경로에 포함된 모든 노드가 위의 논리를 따르고, 그 최단 경로는 predecessor를 통해 오는 것
- 따라서 BFS로 찾은 경로는 최단 경로이게 됨

<br/><br/>

## 05. BFS 최단 경로용으로 바꾸기

[main3_05.py](https://github.com/jaehyun-dev/Today-I-Learned/blob/55c068892341b71a5d695e918682c1072fa0d55e/Data%20Structure/3%20Graph/3%20Shortest%20Path%20Algorithm/main3_05.py) 참고

<br/><br/>

23.02.08

## 06. Dijkstra 알고리즘 변수들

### Dijkstra 알고리즘
- 가중치 그래프의 최단 경로를 찾는 알고리즘
- 노드에 distance, predecessor, complete 세 가지 변수를 저장해야 함

#### distance
- 특정 노드까지의 "최단 거리 예상치"(현재까지 아는 정보로 계산한 최단 거리)

#### predecessor
- 현재까지 최단 경로에서 바로 직전의 노드

#### complete
- 노드까지의 최단 경로를 찾았다고 표시하기 위한 변수
- 처음에 False, 확실한 최단 경로 찾으면 True로 수정

<br/><br/>

## 07. 엣지 Relaxation
- 새로 찾은 경로의 distance가 현재 distance보다 작은지 확인하고 업데이트 해주는 것
- distance와 predecessor를 업데이트
- A에서 B로 가는 경로를 확인해서 업데이트하면, 엣지 (A, B)를 relax한다고 표현
