# Sample Input

# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}

# Sample Output (Ascending order)

# 5
# 9
# 11
# 12

M = int(input())
set_a = set(map(int,input().split()))
N = int(input())
set_b = set(map(int,input().split()))

result = set_a.symmetric_difference(set_b)
for i in sorted(result):
    print(i)