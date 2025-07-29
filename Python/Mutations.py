# Sample Input

# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character = 'k'
# Sample Output

# abrackdabra

if __name__ == '__main__':
    string = list(input().split())
    result = []
    cmd = list(input().split())
    index = 0
    for s in string[0]:
        if index == int(cmd[0]):
            result.append(cmd[1])
            index += 1
        else:
            result.append(s)
            index += 1
    print(''.join(result))

# string = input().strip()
# index, char = input().split()
# index = int(index)

# result = string[:index] + char + string[index+1:]
# print(result)