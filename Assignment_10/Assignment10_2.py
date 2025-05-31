multi = lambda x, y : x*y

def main():
    value1  = 0 
    value2 = 0

    try:
        print("Input 1st no : ",end = "")
        value1 = int(input())
        print("Input 2st no : ",end = "")
        value2 = int(input())
    except Exception as eobj:
        print("Error Ocuured while Acceopting user Input, Please find the Details ", eobj)
    print("Output", multi(value1 , value2))
if __name__ == "__main__":
    main()