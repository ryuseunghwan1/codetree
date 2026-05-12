MAX_N = 5

class codename:
    def __init__(self, codename):
        self.codename = codename

class score:
    def __init__(self, score):
        self.score = score

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
a = tuple(zip(codenames, scores))


sorted_a = sorted(a, key=lambda x: x[1])
min_tuple = sorted_a[0]
print(f"{min_tuple[0]} {min_tuple[1]}")