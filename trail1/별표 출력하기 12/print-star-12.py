N = int(input())

# i는 행(row), j는 열(column)을 나타냅니다.
for i in range(N):
    for j in range(N):
        # 1. 첫 번째 행(i == 0)은 무조건 별을 출력합니다.
        # 2. 그 외의 행에서는 j가 홀수이면서, 행의 번호가 열의 번호보다 작거나 같을 때(i <= j) 별을 출력합니다.
        if i == 0 or (j % 2 == 1 and i <= j):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    # 한 행의 출력이 끝나면 줄바꿈
    print()