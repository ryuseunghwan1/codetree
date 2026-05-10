N = int(input())

# Please write your code here.
def f(N):

    if N == 1:
        return 1
    elif N == 2:
        return 2

    return f(N // 3) + f(N - 1)

print(f(N))