    
def main():
    print("Enter temp in celsius : ", end = "")
    no1 =  int(input())
    fahrea = lambda x : (x* (9/5)+32)
    print("Tempeture in Fahrenheit: ",fahrea(no1), "F")

if __name__ =="__main__":
    main()