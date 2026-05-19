
n = int(input())
price = list(map(int, input().split()))

# Please write your code here.


# 가장 먼저 만나는 가격을 최초의 최소 가격으로 설정합니다.
min_price = price[0]
max_profit = 0

# 두 번째 해의 가격부터 순서대로 확인합니다.
for i in range(1, n):
    # 현재 가격에서 지금까지의 최소 가격을 뺀 값을 계산합니다.
    current_profit = price[i] - min_price
    
    # 만약 이 값(이익)이 기존 최대 이익보다 크다면 업데이트합니다.
    if current_profit > max_profit:
        max_profit = current_profit
        
    # 지금까지 본 가격 중 가장 낮은 가격을 계속 업데이트합니다.
    if price[i] < min_price:
        min_price = price[i]

# 최종적으로 계산된 최대 이익을 출력합니다.
print(max_profit)