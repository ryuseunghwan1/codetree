n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.


for a, b in queries:
    total = 0
    for j in range(a, b):
        total += arr[j[j-1]
    print(total)   
