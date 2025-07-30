# Output Format

# Output 2 lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

# Sample Input

# 4
# bcdef
# abcdefg
# bcde
# bcdef

# Sample Output

# 3
# 2 1 1

from collections import OrderedDict
if __name__ == '__main__':
    n = int(input())
    lst = OrderedDict()
    for _ in range(n):
        data = input()
        if data in lst:
            lst[data] += 1
        else:
            lst[data] = 1
    print(len(lst))
    for i in lst:
        print(lst[i],end=" ")