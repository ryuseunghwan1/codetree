num = int(input())

# 예외 처리
if num == 1:
    print('*')
else:
    cell = 2  # 한 칸 너비

    # 첫 줄
    for _ in range(num):
        print(f"{'*':<{cell}}", end='')
    print()

    # 중간
    for i in range(1, num-1):
        # 왼쪽 별
        for j in range(num):
            if j < i or j == num-1:
                print(f"{'*':<{cell}}", end='')
            else:
                print(f"{'':<{cell}}", end='')
        print()

    # 마지막 줄
    for _ in range(num):
        print(f"{'*':<{cell}}", end='')
    print()