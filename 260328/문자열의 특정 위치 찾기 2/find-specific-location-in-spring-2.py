string = ['apple', 'banana', 'grape', 'blueberry', 'orange']
string_2 = input()
count = 0
for i in string:
    if i[2] == string_2 or i[3] == string_2:
        count += 1
        print(i)

print(count)