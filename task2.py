name=input("student name:")

if name=='Rushan':
    a=int(input("Enter marks of science:"))
    b=int(input("Enter marks of maths:"))
    c=int(input("Enter marks of gujarati:"))
    d=int(input("enter marks of english:"))
    
    total=a+b+c+d
    
    print("total marks:",total)
    print("average:",total/4)
    
elif name=='Arshad':
     a=int(input("Enter marks of science:"))
     b=int(input("Enter marks of maths:"))
     c=int(input("Enter marks of gujarati:"))
    
     total=a+b+c
     
     print("total marks:",total)
     print("average:",total/3)
elif name=='Uvesh':
     a=int(input("Enter marks of science:"))
     b=int(input("Enter marks of maths:"))
    
     total=a+b
     
     print("total marks:",total)
     print("average:",total/2)
else:
    print("wrong name,please check your name")
     
     