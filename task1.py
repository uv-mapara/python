name=input("student name:")

a=int(input("Enter marks of science:"))
b=int(input("Enter marks of maths:"))
c=int(input("Enter marks of gujarati:"))
d=int(input("enter marks of english:"))

total=a+b+c+d

if name=='Rushan':
    print("total marks:",total)
    print("average is:",total/4)
elif name=='Arshad':
    print("total marks:",total)
    print("average is:",total/4)
elif name=='Uvesh':   
    print("total marks:",total)
    print("average is:",total/4)
else:
    print("wrong name")
    