# Sample Input
#
# 3

# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# Sample Output

# 56.00

if __name__ == '__main__':
    n = int(input())
    names  = []
    marks = []
    for _ in range(n):
        student = list(input().split())
        names.append(student[0])
        marks.append([float(x) for x in student[1:]])
    dic = dict(zip(names,marks))
    value = input()
    avg = 0
    if value in dic:
            sum = sum(dic[value])
            avg = sum / len(dic[value])
    print(f'{avg:.2f}')

# Another way

# if __name__ == '__main__':
#     n = int(input())
#     students = {}
#     for i in range(n):
#         student = input().strip().split()
#         name = student[0]
#         marks = list(map(float,student[1:]))
#         students[name] = marks
#     query_name = input().strip()
#     if query_name in students.keys():
#         result = sum(students[query_name])/len(students[query_name])
#         print(f'{result:.2f}')