n = int(input())

# Please write your code here.
def add(n):
    cnt = 0
    for i in range(1, n+1):
        cnt += i

    cnt_1 = cnt // 10

    return cnt_1

print(add(n))
        
