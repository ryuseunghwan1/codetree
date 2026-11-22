N = int(input())
seat = input()

# Please write your code here.

ans = 0

for i in range(N):
    if seat[i] == '0':
        
        temp = list(seat)
        temp[i] = '1'

        pos = []
        for j in range(N):
            if temp[j] == '1':
                pos.append(j)

        min_dist = N
        for k in range(len(pos) - 1):
            min_dist = min(min_dist, pos[k+1] - pos[k])

        ans = max(ans, min_dist) 
        
print(ans)