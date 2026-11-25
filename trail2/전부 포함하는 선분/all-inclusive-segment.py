n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.


ans = float('inf')

for i in range(n):
    
    others = []
    for j in range(n):
        if i != j:
            others.append(segments[j])

    left = min(a for a, b in others)
    right = max(b for a, b in others)

    ans = min(ans, right-left)

print(ans)


