class Calculator():
    def __init__(self , no1, no2):
        self.value1 = no1
        self.value2 = no2
    
    def Add(self):
        return self.value1 + self.value2

    def Sub(self):
        return self.value1 - self.value2

    def div(self):
        return self.value1 / self.value2

    def multi(self):
        return self.value1 * self.value2

def main():
    try :
        print("Welcome to Calculatro Program !!")
        no1 = float(input("Entre Value 1 : "))
        no2 = float(input("Enter Value 2 : "))
        op = getOpration()
        switch_opration(op ,no1 , no2)
    except ValueError as ValE:
        print("Accepted user Input is Number and string is provied, Error message ->", ValE)

def getOpration():
    print("Use below Symbol for Oprations")
    print("Additon : + " ,"Subration : - " ,"Sivivson : / ", "Multifaction : * " )
    opration  = input()
    if opration in ('+', '-' ,'*' ,'/'):
        print("seleted Opration is ", opration)
    else:
        opration = ""
    return opration

def switch_opration(argument, no1, no2):
    ans = 0.0
    obj1 =Calculator(no1 , no2)
    match argument:
        case '+':
           ans = obj1.Add()
        case '-':
            ans = obj1.Sub()
        case '/':
            try :
                ans =obj1.div()
            except ZeroDivisionError as zeroE:
                print(zeroE)
        case '*':
           ans =  obj1.multi()
    print(ans)
         
if __name__ == "__main__":
    main()