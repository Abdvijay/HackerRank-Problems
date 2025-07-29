# Sample Input

# ABCDCDC
# CDC

# Sample Output

# 2

string = input()
sub_string = input()
lst = []
count = 0
for i in range(len(string)-len(sub_string)+1):
    lst.append(string[i:i+len(sub_string)])
for data in lst:
    if data == sub_string:
        count += 1
print(count)