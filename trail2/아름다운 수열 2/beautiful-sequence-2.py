n, m = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(map(int, input().split()))

print(sum(1 for i in range(n - m + 1) if sorted(a[i:i + m]) == b))