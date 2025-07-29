# Output Format

# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

# Sample Input

# qA2
# Sample Output

# True
# True
# True
# True
# True

# any defintion :

#    In Python, any() is a built-in function used to check if at least one element in an iterable (like a list, tuple, set) is True.
#    Check if any string in a list matches a condition

# Example - Syntax : 
# names = ['john', 'alice', 'bob']
# print(any(name.startswith('a') for name in names))  # True

if __name__ == "__main__":
    string = input()
    print(any(s.isalnum() for s in string))
    print(any(s.isalpha() for s in string))
    print(any(s.isdigit() for s in string))
    print(any(s.isupper() for s in string))
    print(any(s.islower() for s in string))