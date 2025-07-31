# Output Format

# Print the averages of all students on separate lines.

# The averages must be correct up to 1 decimal place.

# Sample Input

# 5 3
# 89 90 78 93 80
# 90 91 85 88 86  
# 91 92 83 89 90.5

# Sample Output

# 90.0 
# 91.0 
# 82.0 
# 90.0 
# 85.5    

column, row = map(int,input().split())
marks = []
for _ in range(row):
    mark = list(map(float,input().split()))
    marks.append(mark)
result = zip(*marks)
for i in result:
    print(sum(i)/len(i))