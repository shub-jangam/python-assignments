fact = 1
def Display(no):
    global fact
    if (no > 0):
        fact = fact * no
        no= no-1
        Display(no)
        

def main():  #stack fream 
    Display(5)
    print(fact)
if __name__ =="__main__":
    main() 