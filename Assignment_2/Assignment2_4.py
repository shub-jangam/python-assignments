def getFactor(no):
    result =  list()
    for i in range(1 ,no ,1):
        if no%i ==0:
            result.append(i)
    return result

def main():
    print("Enter no  to print addtion of its Factor : ")
    no1 = int(input())
    print("Include the No itself while calculating factor ? yes : no ")
    add_no = input()
    if add_no.lower() == "yes":
        no1 = no1 +1
    
    result = getFactor(no1)
    print(result)
    print("Additon of factor is ", sum(result))


if __name__ == "__main__":
    main()