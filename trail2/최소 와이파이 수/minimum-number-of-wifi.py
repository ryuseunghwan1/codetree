n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

cnt = 0
i = 0
while i < n:
    if arr[i] == 1:          # 연결 안 된 사람 발견
        cnt += 1             # i+m 위치에 와이파이 설치
        i += 2 * m + 1       # 커버되는 칸만큼 건너뛰기
    else:
        i += 1               # 빈집이면 다음 칸으로

print(cnt)