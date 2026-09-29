# 변수 선언, 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

# 출력
if a >= 1: 
    for _ in range(b):
        print(a, end="")
else:
    print('0'