# Output Format

# Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

# Sample Input

# 5
# 12 9 61 5 14 

# Sample Output

# True

# Explanation

# Condition 1: All the integers in the list are positive.
# Condition 2: 5 is a palindromic integer.

# Hence, the output is True.

if __name__ == '__main__':
    n = int(input())
    cmd = list(map(int,input().split()))
    all_pos = all([num > 0 for num in cmd])
    pal = any([str(num) == str(num)[::-1] for num in cmd])
    print(all_pos and pal)