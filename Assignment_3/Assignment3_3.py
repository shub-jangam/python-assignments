def listadd(listdata):
    output = listdata [0] # Assign one from from list so we can avoid the 0 or non zero 
    for i in listdata:
        if i<output:
            output = i
    return output

def main():
    print("Input: Number of element ",end = "")
    no = int(input())
    result = list()

    for i in range(no):
        print("Enter the No : ", end = "\t")
        no2 = int(input())
        result.append(no2)

    output = listadd(result)

    print("Min Number", output)
if __name__ == "__main__":
    main()