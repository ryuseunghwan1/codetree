matrix = []
matrix_2 = []
total_matrix = []

row = 3
col = 3

# 첫 번째 행렬 입력
for i in range(row):
    line = input().split()
    while not line: # 빈 줄이면 다시 읽기
        line = input().split()
    matrix.append(list(map(int, line)))

# 두 번째 행렬 입력
for i in range(row):
    line = input().split()
    while not line: # 빈 줄이면 다시 읽기
        line = input().split()
    matrix_2.append(list(map(int, line)))

# 결과 계산 및 출력 (기존과 동일)
for i in range(row):
    for j in range(col):
        print(matrix[i][j] * matrix_2[i][j], end=" ")
    print()