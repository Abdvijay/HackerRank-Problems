# Output Format

# Output True or False for each test case on separate lines.

# Sample Input

# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2

# Sample Output

# True 
# False
# False
# Explanation

# Test Case 01 Explanation

# Set A = {1 2 3 5 6}
# Set B= {9 8 5 6 3 2 1 4 7}

# All the elements of set A are elements of set B.
# Hence, set A is a subset of set B.

n = int(input())
result = []
for _ in range(n):
    a_num = int(input())
    a_set = set(map(int,input().split()))
    b_num = int(input())
    b_set = set(map(int,input().split()))
    flag = a_set.issubset(b_set)
    result.append(flag)
for i in result:
    print(i)