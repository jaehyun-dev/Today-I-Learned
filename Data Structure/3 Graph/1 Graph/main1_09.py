# 모든 요소를 0으로 초기화시킨 크기 6 x 6 인접 행렬
adjacency_matrix = [[0 for i in range(6)] for i in range(6)]

# 여기에 코드를 작성하세요
# 엣지 (영훈, 현승) 저장
adjacency_matrix[0][1] = 1
adjacency_matrix[1][0] = 1

# 엣지 (영훈, 동욱) 저장
adjacency_matrix[0][2] = 1
adjacency_matrix[2][0] = 1

# 엣지 (현승, 소원) 저장
adjacency_matrix[1][5] = 1
adjacency_matrix[5][1] = 1

# 엣지 (현승, 지웅) 저장
adjacency_matrix[1][3] = 1
adjacency_matrix[3][1] = 1

# 엣지 (동욱, 소원) 저장
adjacency_matrix[2][5] = 1
adjacency_matrix[5][2] = 1

# 엣지 (지웅, 소원) 저장
adjacency_matrix[3][5] = 1
adjacency_matrix[5][3] = 1

# 엣지 (지웅, 규리) 저장
adjacency_matrix[3][4] = 1
adjacency_matrix[4][3] = 1

# 엣지 (규리, 소원) 저장
adjacency_matrix[4][5] = 1
adjacency_matrix[5][4] = 1

print(adjacency_matrix)


'''실행 결과
[
[0, 1, 1, 0, 0, 0],
[1, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 1],
[0, 1, 0, 0, 1, 1],
[0, 0, 0, 1, 0, 1],
[0, 1, 1, 1, 1, 0]
]
'''

'''모범답안 보기 전 작성 코드
adjacency_matrix[0][1] = 1
adjacency_matrix[0][2] = 1
adjacency_matrix[1][0] = 1
adjacency_matrix[1][3] = 1
adjacency_matrix[1][5] = 1
adjacency_matrix[2][0] = 1
adjacency_matrix[2][5] = 1
adjacency_matrix[3][1] = 1
adjacency_matrix[3][4] = 1
adjacency_matrix[3][5] = 1
adjacency_matrix[4][3] = 1
adjacency_matrix[4][5] = 1
adjacency_matrix[5][1] = 1
adjacency_matrix[5][2] = 1
adjacency_matrix[5][3] = 1
adjacency_matrix[5][4] = 1

이렇게 써도 되기는 하겠지만, 중간에 누락될 수 있음
대칭적으로 작성해주는 게 좋을 듯
'''

