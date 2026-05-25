n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Please write your code here.

def line(*x1, *x2):
    if x2 in x1:
        return 'Yes'
    else:
        return 'No'

print(line(x1 ,x2))