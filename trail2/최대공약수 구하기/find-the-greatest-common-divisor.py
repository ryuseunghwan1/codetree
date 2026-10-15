n, m = map(int, input().split())

n_sq = []
m_sq = []
# Please write your code here.

for i in range(1, n+1):
    if n % i == 0:
        n_sq.append(i)

for j in range(1, m+1):
    if m % j == 0:
        m_sq.append(j)


gcd = max(set(n_sq) & set(m_sq))
print(gcd)