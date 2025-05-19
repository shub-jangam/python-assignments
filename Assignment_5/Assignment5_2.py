def ChkVowel(Value1):
    vowel = ('a','e','i','o','u')
    if Value1.lower() in vowel:
        return True
    else :
        False
        
    
def main():
    
    print("Enter a Char : ", end = "")
    Chr =  input()
    
    if len(Chr) == 1 :
        ret = ChkVowel(Value1=Chr)
        if ret == True:
            print("'"+Chr+"'"+ " Is a vowel !!")
        else:
           print("'"+Chr+"'"+ " Is a consonant !!") 
    else:
        print("Excepted len of the input value is one ")

if __name__ =="__main__":
    main()