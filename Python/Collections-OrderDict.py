# Sample Input

# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30

# Sample Output

# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    items = OrderedDict()
    for _ in range(n):
        data = list(input().split())
        if data[1].isdigit():
            name = data[0]
            price = int(data[1])
        else:
            name = ' '.join(data[:-1])
            price = int(data[-1])
        
        if name in items:
            items[name] += price
        else:
            items[name] = price
    for name, price in items.items():
        print(name, price)