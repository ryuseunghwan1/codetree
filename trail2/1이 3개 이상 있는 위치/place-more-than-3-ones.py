n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 방향을 나타내는 dx, dy 배열
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

total_ans = 0 # 조건(1이 3개 이상)을 만족하는 칸의 총 개수

# 격자의 모든 칸을 순회
for i in range(n):
    for j in range(n):
        cnt = 0 # 각 칸마다 인접한 1의 개수를 세기 위해 0으로 초기화
        
        # 현재 칸(i, j)에서 상하좌우 4방향을 검사
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            
            # 격자 범위를 벗어나지 않는지 확인
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 1:
                    cnt += 1
                    
        # 인접한 칸 중 1의 개수가 3개 이상이면 정답 카운트 증가
        if cnt >= 3:
            total_ans += 1
            
print(total_ans)