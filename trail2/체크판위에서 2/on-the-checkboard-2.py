R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

ans = 0

for r1 in range(R):
    for c1 in range(C):
        for r2 in range(r1 + 1, R):
            for c2 in range(c1 + 1, C):
                # 이동할 때마다 색이 서로 달라야 함 (번갈아 가며 바뀌어야 함)
                if (
                    grid[0][0] != grid[r1][c1] and
                    grid[r1][c1] != grid[r2][c2] and
                    grid[r2][c2] != grid[R - 1][C - 1]
                ):
                    ans += 1

print(ans)