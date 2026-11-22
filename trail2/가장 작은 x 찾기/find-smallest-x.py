n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.

x = 1

for a, b in ranges:
    val = x * 2 
    
    if not ( a <= val <= b):
        break

    x += 1

print(x)
