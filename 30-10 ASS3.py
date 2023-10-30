amt=int(input())
tt=0
fh=0
th=0
oh=0
ft=0
twenty=0
ten=0
five=0
two=0
one=0
while(amt>=2000):
    tt=tt+1
    amt=amt-2000
while(amt>=500):
    fh=fh+1
    amt=amt-500
while(amt>=200):
    th=th+1
    amt=amt-200
while(amt>=100):
    oh=oh+1
    amt=amt-100
while(amt>=50):
    ft=ft+1
    amt=amt-50
while(amt>=20):
    twenty=twenty+1
    amt=amt-20
while(amt>=10):
    ten=ten+1
    amt=amt-10
while(amt>=5):
    five=five+1
    amt=amt-5
while(amt>=2):
    two=two+1
    amt=amt-2
while(amt>=1):
    one=one+1
    amt=amt-1
if tt>0:
    print('2000:'+str(tt))
if fh>0:
    print('500:'+str(fh))
if th>0:
    print('200:',th)
if oh>0:
    print('100:',oh)
if ft>0:
    print('50:',ft)
if twenty>0:
    print('20:',twenty)
if ten>0:
    print('10:',ten)
if five>0:
    print('5:',five)
if two>0:
    print('2:',two)
if one>0:
    print('1:',one)
