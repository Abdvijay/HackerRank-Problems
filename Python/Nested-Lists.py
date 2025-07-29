# Sample Input

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Output 

# Berry
# Harry

# Explanation

# There are  students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

n = int(input())
students = []
score_lst = []
for _ in range(1,n+1):
    name = input()
    score = float(input())
    students.append([name,score])
    score_lst.append(score)
uni_score = sorted(set(score_lst))
second_lowest = uni_score[1]
result = []
for student in students:
    if student[1] == second_lowest:
        result.append(student[0])
result.sort()
for name in result:
    print(name)