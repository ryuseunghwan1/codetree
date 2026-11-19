a, b, x, y = map(int, input().split())

# Please write your code here.

arrive = max(x, y)
depart = min(x,y)

if b - arrive <= b - a:
    print(abs(a-b) + (arrive - depart) + (b-arrive))
else:
    print(b-a)