n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

for i in range(n):

    for j in range(n):
        ans = 100

        left = 100
        right = 0
        
        if i != j:
            a, b = segments[j]

        left = max(left, a)
        right = min(b, right)

        ans = min(ans, right-left)
    
    print(ans)
    