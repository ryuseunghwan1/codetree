R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

ans = 0

# 중간에 거쳐 갈 2개의 점(r1, c1)과 (r2, c2)를 완전탐색으로 찾습니다.
for r1 in range(R):
    for c1 in range(C):
        for r2 in range(r1 + 1, R):
            for c2 in range(c1 + 1, C):
                # 1. 시작점(0,0) -> 첫 번째 점(r1,c1)
                # 2. 첫 번째 점(r1,c1) -> 두 번째 점(r2,c2)
                # 3. 두 번째 점(r2,c2) -> 도착점(R-1, C-1)
                # 위 이동 과정에서 각각 칸의 색깔이 모두 달라야 합니다.
                if (
                    grid[0][0] != grid[r1][c1] and
                    grid[r1][c1] != grid[r2][c2] and
                    grid[r2][c2] != grid[R - 1][C - 1]
                ):
                    ans += 1

print(ans)