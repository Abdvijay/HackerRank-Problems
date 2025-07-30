# Sample Input

# 08 05 2015

# Sample Output

# WEDNESDAY

# Explanation

# The day on August 5th  2015 was WEDNESDAY.

import datetime,calendar

mon,date,year = map(int,input().split())
day = datetime.date(month=mon,day=date,year=year)
print(day.strftime("%A").upper())