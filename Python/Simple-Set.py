# Sample Input

# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France 
# Sample Output

# 5

# Explanation

# UK and France repeat twice. Hence, the total number of distinct country stamps is 5 (five).

n = int(input())
lst = []
for _ in range(n):
    country = input()
    lst.append(country)
result = set(lst)
print(len(result))