word1 = input()
word2 = input()

# Please write your code here.
word1_sort = sorted(word1)
word2_sort = sorted(word2)

word1_sort = ''.join(word1_sort)
word2_sort = ''.join(word2_sort)

if word1_sort == word2_sort:
    print('Yes')
else:
    print('No')