
year = int(input())

# 1. 4의 배수이고, 100의 배수가 아닐 때 -> 윤년
# 2. 또는 400의 배수일 때 -> 윤년
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("true")
else:
    print("false")