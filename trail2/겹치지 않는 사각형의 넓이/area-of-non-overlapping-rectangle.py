x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
def squar(x1, y1, x2, y2, mx1, my1, mx2, my2):
    w = min(x2, mx2) - max(x1, mx1)
    h = min(y2, my2) - max(y1, my1)

    if w < 0:
        w = 0
    if h < 0:
        h = 0

    return w * h

cnt_1 = (x2[0] - x1[0]) * (y2[0] - y1[0])
cnt_2 = (x2[1] - x1[1]) * (y2[1] - y1[1])

overlap_A = squar(x1[0], y1[0], x2[0], y2[0], x1[2], y1[2], x2[2], y2[2])
overlap_B = squar(x1[1], y1[1], x2[1], y2[1], x1[2], y1[2], x2[2], y2[2])

print( (cnt_1+cnt_2) - (overlap_A + overlap_B)  )