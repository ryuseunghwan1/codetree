N = int(input())
num = list(map(int, input().split()))

arr_2 = [i*i for i in num]
for i in arr_2:
    print(i, end=' ')