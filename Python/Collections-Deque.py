# Sample Input

# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

# Sample Output

# 1 2

from collections import deque

n  = int(input())
d = deque()
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'append':
        d.append(int(cmd[1]))
    elif cmd[0] == 'appendleft':
        d.appendleft(int(cmd[1]))
    elif cmd[0] == 'pop':
        d.pop()
    else:
        d.popleft()
for i in d:
    print(i,end=" ")