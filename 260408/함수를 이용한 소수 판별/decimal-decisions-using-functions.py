a, b = map(int, input().split())

def so_func(a, b):
    total = 0

    for i in range(a, b + 1):
        if i < 2:
            continue  # 0, 1은 소수 아님

        is_prime = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            total += i

    return total

print(so_func(a, b))