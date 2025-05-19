
def ChkVoteEligible(Value1):
    if Value1 >= 18:
        return True
    else :
        False
        
    
def main():
    
    print("Enter a  Age : ", end = "")

    age =  int(input())  
    
    ret = ChkVoteEligible(Value1=age)
     
    if ret == True :
        print("Eligible for Vote !!")
    else:
        remainingAge = 18 - age
        print("Not Eligible to Vote ,You will be become Eligible for Voting after : ",  remainingAge , "years." )

if __name__ =="__main__":
    main()