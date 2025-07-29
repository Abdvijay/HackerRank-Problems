# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

# Sample Input 0

# 3

# Sample Output 0

# Weird

# Explanation 0

# n = 3
# n is odd and odd numbers are weird, so print Weird.

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0 :
        print("Weird")
    else:
        if 2 <= n and n <= 5:
            print("Not Weird")
        elif 6 <= n and n <= 20:
            print("Weird")
        elif 20 < n:
            print("Not Weird")