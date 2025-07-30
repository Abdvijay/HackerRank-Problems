# Sample Input

# STDIN   Function
# -----   --------
# 5 2     group A size n = 5, group B size m = 2
# a       group A contains 'a', 'a', 'b', 'a', 'b'
# a
# b
# a
# b
# a       group B contains 'a', 'b'
# b

# Sample Output

# 1 2 4
# 3 5
# Explanation

# 'a' appeared 3 times in positions 1,2 and 4.
# 'b' appeared 2 times in positions 3 and 5.
# In the sample problem, if 'c' also appeared in word group B, you would print -1.

if __name__ == '__main__':
    a_num, b_num = map(int,input().split())
    a_group = []
    b_group = []
    for _ in range(a_num):
        ch = input()
        a_group.append(ch)
    for _ in range(b_num):
        ch = input()
        b_group.append(ch)
    for b_ch in b_group:
        index = 0
        pos = []
        flag = False
        for a_ch in a_group:
            index += 1
            if b_ch == a_ch:
                flag = True
                pos.append(index)
        print(pos)
        if not flag:
            print(-1)
        