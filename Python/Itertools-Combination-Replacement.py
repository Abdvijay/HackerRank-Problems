# Sample Input

# HACK 2
# Sample Output

# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK

from itertools import combinations_with_replacement

lst = list(input().split())
word = lst[0]
count = int(lst[1])

result = sorted(combinations_with_replacement(sorted(word),count))
for i in result:
    print(''.join(i))