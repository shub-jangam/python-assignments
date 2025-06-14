class BankAccount():
    def __init__(self, accountNo, Name ,Balance):
        self.account_no = accountNo
        self.name  = Name
        self.balance = Balance
    
    def deposite(self, amount):
        self.balance = self.balance +amount
        return self.balance
    
    def withdraamount (self, amount):
        if self.balance> amount:
            self.balance = self.balance - amount
        else:
            print("Insufficent balance !!")
    
    def display_balance(self):
        return self.balance
    
    
def main():
    cust1 =  BankAccount("ABC-1234", "marvellous", 1.0)
    print("Current Account balance Is : ", cust1.display_balance())
    
    try:
        amount = float (input("Enter Amount to deposite : "))
        if amount> 0:
            cust1.deposite(amount)
            print("Current Account balance Is : ", cust1.display_balance())
        else:
            print("Enter postive value")

        amount = float (input("Enter Amount to w : "))

        if amount> 0:
            cust1.withdraamount(amount)
            print("Current Account balance Is : ", cust1.display_balance())
        else:
            print("Enter postive value")
    except ValueError as ValE:
        print("Accepted user Input is Number and string is provied, Error message ->", ValE)

if __name__ =="__main__":
    main()    
    
        