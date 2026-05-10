N = int(input())

# Please write your code here.
def f(N):
    if N == 1:
        return 2
    elif N == 2:
        return 4

    return (f(N - 2) * f(N -1)) % 100

print(f(N))