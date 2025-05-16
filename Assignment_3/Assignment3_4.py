def Chkfrequnecy(listdata,ChkNum):
    frequnecy = 0
    for i in listdata:
        if i == ChkNum:
             frequnecy = frequnecy+1 
    return frequnecy

def main():
    print("Input: Number of element ",end = "")
    no = int(input())
    result = list()

    for i in range(no):
        print("Enter the No : ", end = "\t")
        no2 = int(input())
        result.append(no2)
    print("Enter no to Check frequnecy : ",end  = "")
    ChkNum = int(input())
    output = Chkfrequnecy(result, ChkNum)

    print("frequnecy count : ", output)
    
if __name__ == "__main__":
    main()