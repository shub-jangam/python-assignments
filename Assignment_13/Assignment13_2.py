class BankAccount:
    ROI = 10.0

    def __init__(self):
        self.Name = 0.0
        self.amount = 0.0

    def Accept(self, Name , Amount):
        self.Name = Name
        self.amount = Amount
    
    def Display(self):
        print("Account name " + self.Name )

    def Deposit(self, depositeAmount):
        if depositeAmount >0:
            self.amount = self.amount + depositeAmount 
            print("Ammount deposited - ",depositeAmount ," Current balance is : " ,self.amount)
        else :
            print("Please provide Valid amount")
        return self.amount
    
    def Withdraw (self ,withdrawAmount):
        if withdrawAmount< self.amount:
            self.amount = self.amount - withdrawAmount
            print("Withdrawal Completed !!")
            print("Balance Amount - ", self.amount)
        else:
            print("Insuffient Balence !!" + "Currrent Account Balenace is :", self.amount)

    def CalculateInterest(self):
        # A = P (1+rt)
        ret  = self.amount * (1+((BankAccount.ROI/100) *6))
        return  ret  
    
    def Display(self):
        print(self.Name +" has ", self.amount ,"in the bank account.")

    
def main():
    
    bank1  = BankAccount()
    bank1.Accept("MR.ABC",10000)

    print("AccountCreated With name : "+ bank1.Name +" With deposite : ", bank1.amount)
    bank1.Deposit(10000)
    bank1.Withdraw(5500)
    bank1.Withdraw(4500)
    bank1.Withdraw(2000)
    interestAmount = bank1.CalculateInterest()
    print("Interest Amount :", interestAmount)
    bank1.Display()
    
    bank2  = BankAccount()
    bank2.Accept("MR.DEF",100000)
    print("AccountCreated With name : "+ bank1.Name +" With deposite : ", bank1.amount)
    bank2.Deposit(-10000)
    bank2.Deposit(5500)
    bank2.Deposit(4500)
    bank2.Deposit(2000)
    bank2.Display()

if __name__ == "__main__":
    main()