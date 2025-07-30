# Output Format

# Print the sum of the elements of set  on a single line.

# Sample Input

# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5

# Sample Output

# 4

n = int(input())
s = set(map(int, input().split()))

c = int(input())
for _ in range(c):
    cmd = input().split()
    if cmd[0] == 'pop':
        if s:
            s.pop()
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))  # will error if not present
    elif cmd[0] == 'discard':
        s.discard(int(cmd[1])) # safe if not present
print(sum(s))