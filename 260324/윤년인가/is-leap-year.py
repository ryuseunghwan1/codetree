four_year = int(input())

if four_year % 4 == 0:
    if not (four_year % 100 == 0) and (four_year % 400 > 0):
        print("true")
    else:
        print("false")