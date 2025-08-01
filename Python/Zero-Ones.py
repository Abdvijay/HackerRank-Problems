# Output Format

# First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.

# Sample Input

# 3 3 3

# Sample Output

# [[[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]

#  [[0 0 0]
#   [0 0 0]
#   [0 0 0]]]

# [[[1 1 1]
#   [1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]

#  [[1 1 1]
#   [1 1 1]
#   [1 1 1]]]

# Explanation

# Print the array built using numpy.zeros and numpy.ones tools and you get the result as shown.

import numpy

tup = tuple(map(int,input().split()))
print(numpy.zeros(tup,dtype=int))
print(numpy.ones(tup,dtype=int))