a = input()
result = ""

for ch in a:
    if ch.isalpha():   
        result += ch.upper()

print(result)