n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.

rain_index = []
for i in range(n):
    if weather[i] == 'Rain':
        rain_index.append(i)

rain_index.sort(key = lambda idx: date[idx])
target = rain_index[0]

print(date[target], day[target], weather[target])