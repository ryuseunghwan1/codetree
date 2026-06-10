n, m = map(int, input().split())

# Please write your code here.


# N x M 크기의 2차원 배열을 0으로 초기화
answer = [[0] * m for _ in range(n)]

count = 1

# 대각선 인덱스의 합(k)은 0부터 (n - 1) + (m - 1)까지 증가합니다.
for k in range(n + m - 1):
    # 각 대각선에서는 row가 0부터 n-1까지 증가할 수 있습니다.
    for row in range(n):
        # row + col = k 이므로, col은 k - row가 됩니다.
        col = k - row
        
        # col이 올바른 배열 범위(0 이상 m 미만) 안에 있는 경우에만 숫자를 채웁니다.
        if 0 <= col < m:
            answer[row][col] = count
            count += 1

# 결과 출력하기
for row in range(n):
    print(*(answer[row]))