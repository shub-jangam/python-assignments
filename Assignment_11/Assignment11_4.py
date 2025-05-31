ans = 1
index_1 = 0

def Display(no, power):
    global ans
    global index_1
    index_1 = index_1 + 1 
    if ( power>= index_1):
        ans = ans*no  
        Display(no, power)

def main():  #stack fream 
    Display(5 , 4)
    print(ans)
if __name__ =="__main__":
    main() 