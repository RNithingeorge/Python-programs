start, end = map(int, input().split())

leap_years = [year for year in range(start, end+1) if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0]

print("The number of leap years between", start, "and", end, "is", len(leap_years))
