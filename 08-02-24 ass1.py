s={}
n=int(input('enter no of students:'))
for i in range(n):
    l=[]
    htno=int(input('enter htno:'))
    sname=input('enter name:')
    s1=int(input('enter maths:'))
    s2=int(input('enter physics:'))
    s3=int(input('enter cs:'))
    s4=int(input('enter dmdw:'))
    s5=int(input('enter dcn:')) 
    l.append(sname)
    l.append(s1)
    l.append(s2)
    l.append(s3)
    l.append(s4)
    l.append(s5)
    s[htno]=l
