# Basic Syntax: List comprehension in Python is a concise and readable way to create lists in a single line, using a simple syntax.

# [expression for item in iterable if condition]

# Example 1 :  Create a list of squares of numbers from 1 to 5

# sq = [x * x for x in range(1,6)]

# Example 2 : Create a tuple of even numbers from 1 to 10

# even = tuple(i for i in range(1,11) if i % 2 == 0)

# Example 3: Convert set of strings to uppercase

# words = {'Vijay','Swathi'}

# upper = [w.upper() for w in words]

# print(set(upper))

# Input Format

# Four integers  x, y, z and n, each on a separate line.

# Constraints

# Print the list in lexicographic increasing order.

# Sample Input 0

# 1
# 1
# 1
# 2
# Sample Output 0

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


# Print an array of the elements that do not sum to n = 2.

x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i,j,k] for i in range(x+1)
                  for j in range(y+1)
                  for k in range(z+1)
                  if i+j+k != n]

print(result)