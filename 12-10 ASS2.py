sno=int(input('enter sno'))
sname=input('enter student name')
group=input('enter student group')
s1=int(input('enter maths marks'))
s2=int(input('enter phy marks'))
s3=int(input('enter cs marks'))
total=s1+s2+s3
print(total)
avg=total//3
print(avg)
if avg>=90:
    print('O -Grade')
elif avg>=80:
    print('A-Grade')
elif avg>=70:
    print('B-grade')
elif avg>=60:
    print('C-grade')
elif avg>=50:
    print('D-Grade')
else:
    print('Pass')
