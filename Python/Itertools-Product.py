# Sample Input

#  1 2
#  3 4
# Sample Output

#  (1, 3) (1, 4) (2, 3) (2, 4)

from itertools import product
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

tup = product(a_list,b_list)
for i in tup:
    print(i,end=" ")