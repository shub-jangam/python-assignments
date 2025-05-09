
def AddNum(number1, number2):
    ans = number1 +number2
    return ans 

def main():
    print("Enter Number No1 : " , end="")
    no1 = int(input())
    print("Enter Number No2 : " , end="")
    no2 = int(input()) 
       
    result  = AddNum(no1 , no2)
    print("output" ,result)

if __name__=="__main__":
    main()