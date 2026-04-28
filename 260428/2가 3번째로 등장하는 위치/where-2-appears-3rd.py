n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
two = 0
idx = 0
for i in a:
    if i == 2:
        idx += 1
        two += 1
    else:
        idx += 1

    if two == 3:
        break

print(idx)