import Arithmetic


def main():
    print("This Arithemetic Program ")
    
    print("Enter First No : ")
    no1 = float(input())
    
    print("Enter second No : " )
    no2 = float(input())

    if no2== 0:
        print("Second enterted no cant be Zero !! , Please provide a Non- Zero Number")
        print("Please re-run the program !!") 
    else:
        add = Arithmetic.Add(no1 , no2)
        print("Two Number addition is ",  add)

        sub = Arithmetic.Sub(no1 , no2)
        print("Two Number Subtration is ", sub)

        mult = Arithmetic.Mult(no1 , no2)
        print("Two Number Subtration is ", mult)

        div = Arithmetic.Div(no1 , no2)
        print("Two Number Subtration is ", div)

if __name__ == "__main__":
    main()