n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.

x = 1
while True:                      # 바깥: x 후보 바꾸기
    val = x
    ok = True

    for a, b in ranges:          # 안쪽: 이 x로 단서 전부 확인
        val *= 2                 # 누적해서 2를 곱하기
        if not (a <= val <= b):
            ok = False
            break                # 안쪽 for만 빠져나감 → 다음 x로

    if ok:                       # 모든 단서 통과
        print(x)
        break

    x += 1                       # 실패했으니 다음 후보