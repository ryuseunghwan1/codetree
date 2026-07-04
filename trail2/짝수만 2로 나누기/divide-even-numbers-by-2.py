n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def even(arr):
    
    for i in range(n):
        if arr[i] % 2 ==0:
            arr[i] = arr[i] // 2
        
even(arr)

for i in arr:
    print(i, end=' ')