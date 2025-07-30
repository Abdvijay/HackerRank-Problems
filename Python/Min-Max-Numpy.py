# Sample Input

# 4 2
# 2 5
# 3 7
# 1 3
# 4 0

# Sample Output

# 3
# Explanation

# The min along axis 1 = [2,3,1,0] 
# The max of [2,3,1,0]  = 3

import numpy as np
r,c = map(int,input().split())
lst = []
for _ in range(r):
    val = list(map(int,input().split()))
    lst.append(val)
minimum = np.min(lst,axis=1)
print(np.max(minimum))