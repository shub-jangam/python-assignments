
def main():
    print("Enter the Number : ", end = "")
    no = int(input())
    output  =1

    for i in range(1,11,1):
        output = no * i
        print(str(no)+ " X " + str(i) + " = " + str(output))
        #print(no, " X " , i,  " = " , output)
    
    # product = 1
    # step = 1
    # while step <=10:
    #     product = no * step
    #     print(no, " X " , step,  " = " , product)
    #     step = step+1

if __name__ =="__main__":
    main()

