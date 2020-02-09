Space = ' ' * 25
print("%s (ATM Balance Information)" %Space)
import datetime
x= datetime.datetime.now()
print(x)
Account_Balance = 5000000
GovTax = 0.6
FedTax = 58
ATM = 18.75
Balance = int(input("Enter Amount: "))
print("You withdraw: ",Balance)
for i in range(1,999999999):
    if(Balance > 50000):
        amt = (Account_Balance-GovTax)
        amt1 = (amt-FedTax)
        FinalAmt = (amt1-ATM)
        print("Available Amount: ",FinalAmt)
              
    elif(Balance <= 50000):
        amt = (Account_Balance-FedTax)
        amt2 = (amt-ATM)
        print("Available Amount: ",amt2)
    break
else:
            print("You tried wrong function")