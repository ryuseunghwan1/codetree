# 2차원 배열을 구현해 각 줄마다 정수를 입력받습니다.
arr_2d = [
    list(map(int, input().split()))
    for _ in range(4)
]
    
# 각 줄의 합을 출력합니다.
for i in range(4):
    ans = 0
    for j in range(4):
        ans += arr_2d[i][j]
    print(ans)
