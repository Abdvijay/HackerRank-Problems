# Sample Input

# 3
# 1 0
# 2 $
# 3 1

# Sample Output

# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$'
# 3

if __name__ == '__main__':
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    for entry in lst:
        try:
            a,b = map(int,entry.split())
            result = a // b
            print(result)
        except ZeroDivisionError:
            print(f'Error Code: integer division or modulo by zero')
        except ValueError as e:
            print(f'Error Code: {e}')