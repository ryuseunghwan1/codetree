num = int(input())

if num % 4 == 0:
    if num % 100 == 0 and num % 400 > 0:
        print('false')
    else:
        print('true')
else:
    print('false')