a, b = map(int, input().split())
arr = map(int, input().split())

arr_1 = list(arr)

s = 10000

def sum_diff(i, j):
    sum1 = arr_1[i] + arr_1[j]
    sum2 = sum(arr_1)
    return sum2 - sum1
    
for i in range(a):
    for j in range(i+1, a):
        s = min(s, sum_diff(i, j))    

print(s-b)