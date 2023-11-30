doc=input()
if doc.endswith('.jpeg'):
    print('photo document')
elif doc.endswith('.doc'):
    print('word document')
elif doc.endswith('.xls'):
    print("Excel document")
elif doc.endswith('.ppt'):
    print("powerpoint document")
else:
    print("Invalid document")
   
