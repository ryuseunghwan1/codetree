A = input()

# Please write your code here.

def string(A):

    cnt = A[0]
    cnt_2 = 0
    for i in A[:]:
        if i != cnt:
            cnt_2 += 1

    if cnt_2 == 0:
        return 'No'
    else:
        return 'Yes'
        
print(string(A))