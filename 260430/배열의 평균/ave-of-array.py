arr = []

for _ in range(2):
    cnt_arr = list(map(int, input().split()))
    arr.append(cnt_arr)
    
print(round(sum(arr[0])/len(arr[0]),1), round(sum(arr[1])/len(arr[1]),1))

for i in range(4):
    print(  round(  (arr[0][i] + arr[1][i])/ 2  ,1)   , end = ' ')
print()
print(  round( sum(arr[0]+arr[1])/8,1)  )



