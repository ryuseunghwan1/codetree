x1, x2, x3, x4 = map(int, input().split())

# Please write your code here.
cnt_1 = []
cnt_2 = []

result = 'nonintersecting'

for i in range(x1, x2+1):
    cnt_1.append(i)

for j in range(x3, x4+1):
    cnt_2.append(j)

for m in cnt_1:
    if m in cnt_2:
        result = 'intersecting'
        
print(result)