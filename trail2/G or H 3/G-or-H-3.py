n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# 최대 위치가 10000이므로 인덱스 10000까지 표현하기 위해 10001 크기로 선언합니다.
# 안전하게 10001개로 설정합니다.
MAX_R = 10000
arr = [0] * (MAX_R + 1)

for i, j in zip(x, c):
    if j == 'G':
        arr[i] = 1
    else:
        arr[i] = 2

total = 0

# 사진의 시작점 m은 1부터 MAX_R까지 움직일 수 있습니다.
for m in range(1, MAX_R + 1):
    # 사진의 끝점은 m + k가 되며, 이 값이 범위를 벗어나지 않도록 처리합니다.
    if m + k > MAX_R:
        # 끝점이 10000을 넘어가면 그 이후는 탐색할 필요가 없으므로 종료하거나 범위를 조절합니다.
        # 여기서는 m+k가 10000 이하인 구간까지만 보거나, 범위를 제한해 줍니다.
        end = MAX_R
    else:
        end = m + k
        
    cnt = 0
    # 사진의 크기가 K이므로 m부터 m+k까지(end까지 포함해야 하므로 end+1) 더해줍니다.
    for curr in range(m, end + 1):
        cnt += arr[curr]
        
    total = max(total, cnt)

print(total)