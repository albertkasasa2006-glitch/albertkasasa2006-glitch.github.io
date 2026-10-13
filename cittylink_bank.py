"""
Name: Kasasa Albert Bwete
reg no: S26B38-008
access number: B39110

This program processes customers for citylink mini-bank, it checks account eligibiity and minimum deposits.

"""

def check_eligibility(Age,Account_type):
    if Account_type=="S": #SAVINGS
         return(True)
    elif Account_type=="C": #CURRENT
        return(True)
    elif Account_type== "T": #STUDENT
         if Age <=25:
            return(True)
         else:
             return(False)
    else:
        return(False)

def get_minimum_deposit(Account_type):

    if Account_type=="S":
        return(50_000)
    elif Account_type=="C":
        return(100_000)
    else:
        return(20_000)

n=int(input("Enter number of customers: "))
accounts_opened=0
total_deposited=0
for i in range(1,n+1):
    print(f"Client{i}:")


    Name = input("Enter the name of the customer: ")
    Age = int(input("Enter the age of the customer: "))
    Account_type = input("Enter the type of account: ")

    if check_eligibility(Age, Account_type):
        customer_deposit=int(input("Enter the customer deposit: "))
        minimum_deposit = get_minimum_deposit(Account_type)

        if customer_deposit >= minimum_deposit:
            accounts_opened += 1
            total_deposited += customer_deposit
            print (f"Account opened successfully for {Name}. Balance, {customer_deposit}")
        else:
            print(f"Deposit too low. Minimum deposit required for{Account_type} account is {minimum_deposit}")
    else:
        if Account_type == "T":
            print("Sorry, student accounts are only for age 25 or below.")
        else:
            print("Invalid account type entered.")

print("SESSION SUMMARY")
print("Accounts opened:",accounts_opened)
print("Total deposited:", total_deposited)
        
    
