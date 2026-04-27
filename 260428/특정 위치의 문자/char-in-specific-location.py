arr = ['L', 'E', 'B', 'R', 'O', 'S']
idx = -1
N = input()

for i, char in enumerate(arr):
    if char == N:
        idx = i

if idx == -1:
    print('None')
else:
    print(idx)