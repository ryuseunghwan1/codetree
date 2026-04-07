a, b = map(int, input().split())

# Please write your code here.

def num_count(a, b):
    
    cnt = 1

    for i in range(a, b+1):
        if i%10 in [3, 6, 9] or i // 3 in [3,6,9] or i % 3 ==0:
            cnt += 1
    
    return cnt

print(num_count(a, b))

    