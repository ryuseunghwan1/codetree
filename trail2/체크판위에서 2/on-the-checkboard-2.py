import sys

def main():
    data = sys.stdin.read().split()
    R, C = int(data[0]), int(data[1])
    # 칸이 공백으로 구분되든 붙어 있든 처리
    s = "".join(data[2:])
    grid = [s[i*C:(i+1)*C] for i in range(R)]

    start, end = grid[0][0], grid[R-1][C-1]
    if start == end:
        print(0)
        return

    # cnt[i][j] = (1..i-1, 1..j-1)이 아니라,
    # 행 0..i-1, 열 0..j-1 영역에서 '중간1 후보'(시작과 다른 색, 첫 행/열 제외) 개수
    cnt = [[0] * (C + 1) for _ in range(R + 1)]
    for i in range(R):
        for j in range(C):
            is_p1 = 1 if (i >= 1 and j >= 1 and grid[i][j] != start) else 0
            cnt[i+1][j+1] = cnt[i][j+1] + cnt[i+1][j] - cnt[i][j] + is_p1

    ans = 0
    # 중간2: 시작과 같은 색, 마지막 행/열 제외
    for i in range(1, R - 1):
        for j in range(1, C - 1):
            if grid[i][j] == start:
                # 행 0..i-1, 열 0..j-1 에 있는 중간1 후보 수
                ans += cnt[i][j]
    print(ans)

main()