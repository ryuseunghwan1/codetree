a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.

def clean(a, b, c, d):
    cnt_1 = b - a
    cnt_2 = d - c
    cnt_3 = 0
    
    if d > a:
        cnt_3 = d - a
    
    return cnt_1 + cnt_2 - cnt_3

print(clean(a, b, c, d))

