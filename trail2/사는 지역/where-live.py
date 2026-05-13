n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
a = list(zip(name,  street_address, region))
a.sort()

print('name', a[-1][0])
print('addr', a[-1][1])
print('city', a[-1][2])
