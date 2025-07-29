# Sample Input

# 12

# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

if __name__ == '__main__':
    n = int(input())
    lst = []
    for _ in range(n):
        cmd = list(input().split())
        if cmd[0] == 'insert':
            lst.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == 'print':
            print(lst)
        elif cmd[0] == 'remove':
            lst.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            lst.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            lst.sort()
        elif cmd[0] == 'pop':
            lst.pop()
        else:
            lst.reverse()