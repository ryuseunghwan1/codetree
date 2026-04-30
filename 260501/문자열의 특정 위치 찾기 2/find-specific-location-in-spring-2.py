n = ['apple', 'banana', 'grape', 'blueberry', 'orange']
new = input()
cnt = 0

for i in n:
    if new == i[2] or new == i[3]:
        print(i)
        cnt+=1
        
print(cnt)
