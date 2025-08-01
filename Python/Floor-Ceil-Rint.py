# Note
# In order to get the correct output format, add the line np.set_printoptions(legacy='1.13') below the numpy import.

# Input Format

# A single line of input containing the space separated elements of array .

# Output Format

# On the first line, print the  of A.
# On the second line, print the  of A.
# On the third line, print the  of A.

# Sample Input

# 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

# Sample Output

# [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
# [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
# [  1.   2.   3.   4.   6.   7.   8.   9.  10.]

import numpy as np
np.set_printoptions(legacy='1.13')
num = np.array(list(map(float,input().split())))

fl = np.floor(num)
print(fl)
ce = np.ceil(num)
print(ce)
ri = np.rint(num)
print(ri)