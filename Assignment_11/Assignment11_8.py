i = 1

def Display(no):
    global i
    if (no >= 1):
        no = no-1
        print("*"*i)
        i= i+1
        Display(no)
        
def main():  #stack fream 
    Display(4)
 
if __name__ =="__main__":
    main() 