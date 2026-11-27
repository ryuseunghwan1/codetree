pos = list(map(int, input().split()))

# Please write your code here.

a = abs( pos[0] - pos[1]   ) - 1
b = abs(pos[1] - pos[2] )  - 1

print(min(a,b))