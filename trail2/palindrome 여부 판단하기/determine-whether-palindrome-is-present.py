A = input()

# Please write your code here.
def palindrome(A):
    if A[:] == A[::-1]:
        return 'Yes'
    else:
        return 'No'

print(palindrome(A))