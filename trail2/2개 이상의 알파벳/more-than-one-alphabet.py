

A = input()

def set_func(A):
    if len(set(A)) >= 2:
        return 'Yes'
    else:
        return 'No'

print(set_func(A))