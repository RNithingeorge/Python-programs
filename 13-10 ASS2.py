#write a code for restraunt bill
#offer promo code HOLI-50%,SUNDAY-40%
vb=200
cb=300
mb=400
print('*****Welcome to python restraunt')
cname=input('Enter customer name:')#ravi
cphno=input('Enter Phno:')#12345
vbq=int(input('Enter no of vb packets'))#2
cbq=int(input('Enter no of cb packets'))#2
mbq=int(input('Enter no of mb packets'))#0
pc=input('Enter promo code:')#HOLI
bill=(vb*vbq)+(cb*cbq)+(mb*mbq)
if pc=='HOLI' or pc=='holi':
    disc=bill*50/100#500
elif pc=='SUNDAY' or pc=='sunday':
    disc==bill*40/100
elif bill>=2000:
    disc=bill*20/100
elif bill>=1000:
    disc=bill*10/100
elif bill>=500:
    disc=bill*5/100
else:
    disc=bill*3/100
tbill=bill-disc#500
gst=tbill*12/100#60
obill=tbill+gst
print('customer name:',cname)
print('customer phno:',cphno)
print('bill:',bill)
print('Discount:',disc)
print('Gst 12%:',gst)
print('Bill to be paid:',obill)
print('**Thank you!Visit Again***')
