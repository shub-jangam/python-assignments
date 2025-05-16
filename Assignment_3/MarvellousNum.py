def ChkPrime(no):
    result =  list()
    for i in range(1 ,no ,1):
        if no%i ==0 and i >0 :
            result.append(i)
    return result