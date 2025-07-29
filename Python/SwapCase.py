# Sample Input 0

# HackerRank.com presents "Pythonist 2".

# Sample Output 0

# hACKERrANK.COM PRESENTS "pYTHONIST 2".

def Swapcase(string):
    result = []
    for s in string:
        if s.isalpha():
            if s.islower():
                result.append(s.upper())
            elif s.isupper():
                result.append(s.lower())
        else:
            result.append(s)
    return ''.join(result)

if __name__ == '__main__':
    string = input().strip()
    result = Swapcase(string)
    print(result)