fact = 0
index_1 = 0

def Display(no):
    global fact
    global index_1

    if (len(no) > index_1):
        fact = fact+ int(no[index_1])
        index_1 = index_1 +1   
        Display(no)

def main():  #stack fream 
    Display("1234")
    print(fact)
if __name__ =="__main__":
    main() 