N = int(input())

# Please write your code here.

def conti(N):
    if N == 1:
        return 1

    return conti(N-1) + N

print(conti(N))