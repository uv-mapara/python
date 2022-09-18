def removedigit():
    a=open('demofile.txt','r')
    r=a.read()
    b=[]
    a.close()

    for i in r:
        if not i.isdigit():
            b.append(i)
    print("".join(b))
    f = open("demofile2.txt", "a")
    f.write("".join(b))
    f.close()
    
    
def  removealpha():
    a=open('demofile.txt','r')
    r=a.read()
    b=[]
    a.close()

    for i in r:
        if not i.isalpha():
            b.append(i)
    print("".join(b))
    f = open("demofile2.txt", "a")
    f.write("".join(b))
    f.close()
    
removedigit()
