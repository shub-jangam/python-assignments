squ = lambda x : x**2
cub = lambda x: x*x*x
def main():
    print("Enter No : ")
    no = int(input())
    square  = squ(no)
    print("Square of No : " ,square)
    cube = cub(no)
    print("Cube of No : ", cube)  
    pass
if __name__ == "__main__":
    main()