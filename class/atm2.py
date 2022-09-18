class account():
    balance=5000
    def view(self):
        return self.balance
    def deposit(self):
        amount=int(input("DEPOSIT AMOUNT:"))
        self.balance+=amount
        return self.balance
    def withdraw(self):
        amount=int(input("WITHDRAW AMOUNT:"))
        self.balance-=amount
        return self.balance
    def exit(self):
        exit()

x=account()
print("WELOME TO BANK OF BARODA")
a=[111,123,222,234,333]
pin=int(input("PIN PASSWORD:"))
for i in a:
    if i==pin:
        while True:
            print("CHOOSE YOUR OPTION: \n 1.VIEW BALANCE \n 2.DEPOSIT \n 3.WITHDRAW \n 4.EXIT")
            option=int(input("ENTER YOUR OPTION:"))
            if option==1:
                print(x.view())
            elif option==2:
                print(x.deposit())
            elif option==3:
                print(x.withdraw())
            elif option==4:
                print(x.exit())
            else:
                print("INVALID OPTION")
    else:
        print("INCORRECT PIN")


    
