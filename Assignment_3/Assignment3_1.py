def listadd(listdata):
    output = 0
    for i in listdata:
        output = output + i
    return output

def main():
    print("Input: Number of element ",end = "")
    no = int(input())
    result = list()

    for i in range(no):
        print("Enter the No : ", end = "\t")
        no2 = int(input())
        result.append(no2)
    
    print(result)
    output = listadd(result)

    print(output)
if __name__ == "__main__":
    main()