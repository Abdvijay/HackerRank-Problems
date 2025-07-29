# Sample Input

# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

# Sample Output

# 200

# Explanation

# Customer 1: Purchased size 6 shoe for $55.
# Customer 2: Purchased size 6 shoe for $45.
# Customer 3: Size 6 no longer available, so no purchase.
# Customer 4: Purchased size 4 shoe for $40.
# Customer 5: Purchased size 18 shoe for $60.
# Customer 6: Size 10 not available, so no purchase.

# Total money earned =  55 + 45 + 40 + 60 = $200

# from collections import Counter
# n = int(input())
# lst = list(map(int,input().split()))
# count = int(input())
# final = []
# for i in range(0,count):
#     purchase = list(map(int,input().split()))
#     if purchase[0] in lst:
#         final.append(purchase[1])
#         lst.remove(purchase[0])
# print(sum(final))

from collections import Counter
n = int(input())
lst = list(map(int,input().split()))

product = Counter(lst)
c = int(input())
amount = 0
for _ in range(c):
    size, price = map(int,input().split())
    if product[size] > 0:
        amount += price
        product[size] -= 1
print(amount)