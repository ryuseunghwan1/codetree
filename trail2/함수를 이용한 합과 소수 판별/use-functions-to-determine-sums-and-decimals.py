a, b = map(int, input().split())

# Please write your code here.


cnt = 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    

def digit_sum_even(n):
    return sum(map(int, str(n))) % 2 == 0

    

for i in range(a, b+1):
    if is_prime(i) and digit_sum_even(i):
        cnt += 1



print(cnt)
    

