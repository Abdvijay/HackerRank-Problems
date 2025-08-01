# Output Format

# A list on a single line containing the cubes of the first N fibonacci numbers.

# Sample Input

# 5

# Sample Output

# [0, 1, 1, 8, 27]

cube = lambda x: x * x * x
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        a,b = 0,1
        lst = []
        lst = [ a,b ]
        for i in range(2,n):
            c = a+b
            lst.append(c)
            a = b
            b = c
    return lst

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))