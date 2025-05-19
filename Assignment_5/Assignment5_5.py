    
def main():
    print("Enter a Number : ", end = "")
    no1 =  int(input())
    chek = lambda x : x%2==0
    print(no1 ," is Even Number") if chek(no1) else print(no1, " is a Odd Number")

if __name__ =="__main__":
    main()