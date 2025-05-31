i = 0
def Display(no):
    global i
    if (no > i):
        i= i+1
        print(i , end ="\t")
        Display(no)
        

def main():  #stack fream 
    Display(5)
 
if __name__ =="__main__":
    main() 