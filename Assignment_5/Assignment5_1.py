def arthematic (Value1 , Value2):
    sum  = Value1 + Value2
    print("Sum : ",sum)
    sub =  Value1 + Value2
    print("Differnce : ", sum)
    multi = Value1 * Value2
    print("Product : ", multi)
    div =  Value1 / Value2 
    print("Division : ", div)
    
def main():
    
    print("Enter first number : ", end = "")
    no1 =  int(input())
    
    print("Enter Second Number : " , end ="")
    no2 = int(input())

    if no2 !=0 :
        arthematic(Value1=no1, Value2 = no2)
    else:
        print("Second number cant be zero , Division will fail ")

if __name__ =="__main__":
    main()