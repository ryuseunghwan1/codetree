n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def is_subsequence(A, B):
    n = len(A)
    m = len(B)
    
    # A에서 시작 위치를 하나씩 이동
    for i in range(n - m + 1):
        if A[i:i+m] == B:
            return 'Yes'
    
    return 'No'

print(is_subsequence(a,b))
