n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def sh(n, m):
    cnt = []

    while m != 0:
        cnt.append(m) 

        if m % 2 == 0:
            m = m // 2
        else:
            m = m -1

    return cnt 

total = 0

for i in sh(n, m):
    total += A[i-1]

print(total)
        