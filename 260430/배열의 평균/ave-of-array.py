arr = []

for _ in range(2):
    cnt_arr = list(map(int, input().split()))
    arr.append(cnt_arr)
    
print(sum(arr[0])/len(arr[0]), sum(arr[1])/len(arr[1]))

for i in range(4):
    print((arr[0][i] + arr[1][i])/ 2, end = ' ')
print()
print(sum(arr[0]+arr[1])/8)



