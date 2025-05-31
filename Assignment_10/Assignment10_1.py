fun1 = lambda x :x **2

def main():
    no1 = 0
    try:
        print("Input : " ,end ="")
        no1 = int(input())
        ret =  fun1(no1)
        print("Output: ", ret)
    except Exception as eobj:
        print("Error Ouccred !! Please find the deatils -->  ", eobj)


if __name__== "__main__":
    main()
