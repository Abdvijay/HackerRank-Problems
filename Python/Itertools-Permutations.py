# Sample Input

# HACK 2

# Sample Output

# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH

# Explanation

# All possible size 2 permutations of the string "HACK" are printed in lexicographic sorted order.

from itertools import permutations

cmd = list(input().split())
letters = []
num = int(cmd[1])
word = cmd[0]

for lt in word:
    letters.append(lt)

sort = sorted(letters)
perm = list(permutations(sort,num))
for i in perm:
    print(''.join(i))