a, b, x, y = map(int, input().split())

no_tp   = abs(a - b)
x_to_y  = abs(a - x) + abs(y - b)
y_to_x  = abs(a - y) + abs(x - b)

print(min(no_tp, x_to_y, y_to_x))