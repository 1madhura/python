#Program to check whether the given year is leap year
year = 2004
if (year % 400 == 0) and (year % 100 ==0):
    print("year is a leap year",year)
elif (year % 4 == 0) and (year % 100 != 0):
    print("year is a leap year",year)
else:
    print("year is not a leap year",year)
