# Output Format

# Print the different combinations of string  on separate lines.

# Sample Input

# HACK 2

# Sample Output

# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
lst = list(input().strip().split())
str = ''.join(sorted(lst[0]))
n = int(lst[1])

for i in range(1,n+1):
    for combo in combinations(str, i):
        print(''.join(combo))