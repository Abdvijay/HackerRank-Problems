# Output Format

# Print True if set A is a strict superset of all other N sets. Otherwise, print False.

# Sample Input

# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12

# Sample Output

# False

# a_set = set(map(int,input().split()))
# n = int(input())
# final = []
# for _ in range(n):
#     b_set = set(map(int,input().split()))
#     result = a_set.issuperset(b_set)
#     final.append(result)
# for i in final:
#     if str(i) == 'False':
#         print("False")
#         break
# else:
#     print("True")


a_set = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    b_set = set(map(int, input().split()))
    if not a_set.issuperset(b_set):
        print("False")
        break
else:
    print("True")