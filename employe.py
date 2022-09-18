employees=int(input("How many employees:"))
print( )
total=0

for i in range(employees):
    name=str(input("Enter employees name:"))
    sallary=int(input("Enter salary:"))
    add=sallary*13/100
    total=sallary+add
    print("Add bonus:",add)
    print("total sallery with 13% add:",total)
    print( )