    
def main():
    print("Enter Lenght: ")
    l =  int(input())
    print("Enter width")
    w = int(input())
    area = lambda x,y : (x*y)
    perimeter = lambda x,y : (x+y)*2
    print("Area : " ,area(l,w))
    print("Perimeter : " ,perimeter(l,w))

if __name__ =="__main__":
    main()