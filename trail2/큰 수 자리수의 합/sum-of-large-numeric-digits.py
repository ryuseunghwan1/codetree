a, b, c = map(int, input().split())

# Please write your code here.
cnt = a*b*c
def f(cnt):
    
    if cnt < 10:
        return cnt % 10
    
    return f(cnt//10) + f(cnt%10)

print(f(cnt))