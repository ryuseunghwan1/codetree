import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    first = list(map(int, data[1:4]))
    second = list(map(int, data[4:7]))

    # 원형 다이얼에서 두 수의 거리가 2 이내인지 확인
    def close(x, y):
        d = abs(x - y)
        return min(d, n - d) <= 2

    # 세 자리 모두 target 조합과 가까운지 확인
    def matches(combo, target):
        return all(close(combo[i], target[i]) for i in range(3))

    count = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                combo = (a, b, c)
                if matches(combo, first) or matches(combo, second):
                    count += 1

    print(count)

main()

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    first  list(map(int, data[1:4]))

    def close(x, y):
        d= abs(x-y)
        return min(d, n-)