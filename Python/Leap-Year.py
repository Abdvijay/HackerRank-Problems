def LeapYear(year):
    flag = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0 :
            flag = True
    return flag

if __name__ == "__main__":
    year = int(input())
    result = LeapYear(year)
    print(result)