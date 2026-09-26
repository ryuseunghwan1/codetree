import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    xs = [int(data[1 + 2*i]) for i in range(n)]
    ys = [int(data[2 + 2*i]) for i in range(n)]

    def dist(a, b):
        return abs(xs[a] - xs[b]) + abs(ys[a] - ys[b])

    total = 0
    for i in range(n - 1):
        total += dist(i, i + 1)

    best_save = 0
    for i in range(1, n - 1):  # 첫 번째, 마지막 체크포인트 제외
        save = dist(i - 1, i) + dist(i, i + 1) - dist(i - 1, i + 1)
        best_save = max(best_save, save)

    print(total - best_save)

main()