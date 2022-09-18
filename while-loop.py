i=1
print( )
student=int(input("how many student:"))
k=1

while i<=student:
    print( )
    name=str(input(f"{k} student name:"))
    k+=1
    
    total=0
    j=1
    stnum=1
    subject=int(input("how many subject:"))
     
    while j<=subject:
        marks=int(input((f"Enter the mark for subject {stnum} of student:")))
        total=total+marks
        stnum+=1
        j+=1
    print("total marks:",total)
    average=total/subject
    print("average:",average)
    i=i+1