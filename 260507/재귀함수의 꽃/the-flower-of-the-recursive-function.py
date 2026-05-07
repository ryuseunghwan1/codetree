N = int(input())

# Please write your code here.
def flowers(N):

    if N == 0:
        return

    print(N, end= ' ')
    flowers(N-1)
    print(N, end=' ')

flowers(N)