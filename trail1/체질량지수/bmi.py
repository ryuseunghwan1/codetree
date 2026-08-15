h, w = map(int, input().split())

bmi = (10000*w)//(h**2)

if bmi >= 25:
    print(bmi)
    print("Obesity")
else:
    print(bmi)