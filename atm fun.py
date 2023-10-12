# ATM
'''
credit
debit
min statement
exit
'''
def credit(credit_amount,amount):
    print(credit_amount+amount)
def debit(debitamount,amount):
    print(amount-debitamount)
def minstatement(amount):
    print(amount)
    
s='''
1.credit
2.debit
3.min statement
4.exit
'''
name = "lava"
passwords = "1234"
username = input("enter the username")
password= input("enter the password")
amount = 2000
if name == username and passwords==password:
    
    while True:
         print(s)
         option = int(input("Enter the option:"))
         if option == 1:
            credit_amount = float(input("enter the amount to credit:"))
            print("amount credited",credit(credit_amount,amount))
         elif option==2:
            deditamount = int(input("enter the amount to debit:"))
            if amount<deditamount:
              print("No balance pls enter below",amount)
            else:
              print("amount debited: pls collect cash",debit(deditamount,amount))
         elif option==3:
            print("amount:",minstatement(amount))
         elif option==4:
                break
 
else:
    print("incorrect")