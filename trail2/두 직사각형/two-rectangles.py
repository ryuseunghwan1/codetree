x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

def quar(x1, y1, x2, y2, a1, b1, a2, b2):
    # 좌, 우, 하, 상 4가지 방향 중 하나라도 완전히 떨어져 있다면 nonoverlapping
    if x2 < a1 or a2 < x1 or y2 < b1 or b2 < y1:
        return 'nonoverlapping'
    else:
        return 'overlapping'

print(quar(x1, y1, x2, y2, a1, b1, a2, b2))