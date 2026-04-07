n = int(input())


# Please write your code here.
def check_number(n):

    digit_sum = (n // 10) + (n % 10)
    # 짝수인지 확인
    if n % 2 == 0 and digit_sum % 5 ==0:
        return 'Yes'
    else:
        return 'No'


print(check_number(n))


