import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    segs = [(int(data[1 + 2*i]), int(data[2 + 2*i])) for i in range(n)]
    segs.sort()                      # x1 기준 정렬
    x2 = [b for _, b in segs]

    INF = float('inf')
    # prefix_max[i]: 0~i-1번 선분의 x2 최댓값
    prefix_max = [-INF] * n
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i-1], x2[i-1])

    # suffix_min[i]: i+1~n-1번 선분의 x2 최솟값
    suffix_min = [INF] * n
    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(suffix_min[i+1], x2[i+1])

    ans = sum(1 for i in range(n)
              if prefix_max[i] < x2[i] < suffix_min[i])
    print(ans)

main()