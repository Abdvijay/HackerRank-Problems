# Output Format : Print the runner-up score.

# Sample Input

# 5
# 2 3 6 6 5

# Sample Output  =  5

if __name__ == '__main__':
    n = int(input())
    lst = list(map(int,input().split()))
    result = set(lst)
    final = list(result)
    print(final[-2])

# Another way

# n = int(input())
# lst = map(int,input().split())
# result = list(set(lst))
# result.sort()
# print(result[-2])