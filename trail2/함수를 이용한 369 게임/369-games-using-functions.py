a, b = map(int, input().split())

# Please write your code here.

def num_count(a, b):
    cnt = 0

    for i in range(a, b+1):
        
        if i % 3 == 0:
            cnt += 1
        else:
           
            for digit in str(i):
                if digit in ['3', '6', '9']:
                    cnt += 1
                    break   
    
    return cnt

print(num_count(a, b))