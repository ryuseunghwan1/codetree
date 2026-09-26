n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_conins = 0

for i in range(n):
    for j in range(n-2):
        
        current_coins = grid[i][j] + grid[i][j+1] + grid[i][j+2]

        if current_coins > max_coins:
            max_coins = current_coins

print(current_coins)