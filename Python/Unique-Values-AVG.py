# Sample Input

# STDIN                                       Function
# -----                                       --------
# 10                                          arr[] size N = 10
# 161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]
# Sample Output

# 169.375
# Explanation

# Here, set is the set containing the distinct heights. Using the sum() and len() functions, we can compute the average.

if __name__ == '__main__':
    n = int(input())
    arr = set(map(int,input().split()))
    avg = sum(arr) / len(arr)
    print(f'{avg:.3f}')