# Task
# The provided code stub reads an integer,n , from STDIN. For all non-negative integers i<n, print i*i.

# Input Format

# The first and only line contains the integer, n.

# Output Format

# Print  lines, one corresponding to each i.

# Sample Input 0

# 5
# Sample Output 0

# 0
# 1
# 4
# 9
# 16

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)