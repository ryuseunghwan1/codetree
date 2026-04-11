text = input()
pattern = input()

# Please write your code here.
def instring():
    sh = []
    cnt = 0

    for i in text:
    
        sh.append(i)

        if pattern not in sh:
            cnt += 1
        else:
            break

    return cnt - len(pattern)

print(instring())