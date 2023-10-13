year=int(input('Enter year'))
if year%4==0 and year%100!=0:
    print('Given year is leap year')
elif year%400==0:
    print('Given year is leap year')

else:
    print("Given year is not a leap year")
