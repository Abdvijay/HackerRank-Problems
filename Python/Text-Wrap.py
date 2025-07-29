# Sample Input

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

if __name__ == '__main__':
    string = input()
    letter_count = int(input())
    result = []
    index = 0
    word = ''
    for s in string:
        word += s
        index += 1
        if index == letter_count:
            result.append(word)
            word = ''
            index = 0
    if word:
        result.append(word)
    print('\n'.join(result))