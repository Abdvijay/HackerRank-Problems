# Output Format

# For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

# Sample Input

# 2
# 9587456281
# 1252478965

# Sample Output

# YES
# NO

n = int(input())
result = []
for _ in range(n):
    number = input()
    if number[0] in ['7','8','9'] and len(number) == 10 and number.isdigit():
        result.append("YES")
    else:
        result.append("NO")
for i in result:
    print(i)