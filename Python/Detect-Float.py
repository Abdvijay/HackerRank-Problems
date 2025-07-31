# Output Format

# Output True or False for each test case.

# Sample Input

# 4
# 4.0O0
# -1.00
# +4.54
# SomeRandomStuff

# Sample Output

# False
# True
# True
# False

n = int(input())
lst = []
for _ in range(n):
    val = input()
    flag = True
    
    if val and val[0] in '+-':
        val_check = val[1:]
    else:
        val_check = val
        
    for i in val_check:
        if i.isalpha():
            flag = False
            break
    
    dot = any([i == '.' for i in val_check])
    
    double_sign = True
    
    valid_chars = all(c.isdigit() or c == '.' for c in val_check)
    
    if len(val) >= 2 and val[0] in '+-' and val[1] in '+-':
        double_sign = False
        
    if flag and dot and val_check.count('.') == 1 and double_sign and valid_chars:
        lst.append("True")
    else:
        lst.append("False")
for res in lst:
    print(res)