class Number:

    def __init__(self, number):
        self.value = number
    
    def getFactor(self):
        tempList = []
        for i in range(1 ,self.value+1 ,1):
            if self.value%i ==0:
                tempList.append(i)
        return tempList

    def sumfactor(self):
        listOfFactor = self.getFactor()
        return sum(listOfFactor)

    def isPrime(self):
        if self.value <= 1:
            return False
        for i in range(2, self.value):
            if self.value % i == 0:
                return False
        return True

    def isPerfectNum(self):
        sum = self.sumfactor()
        sum = sum - self.value
        if sum == self.value:
            return True
        else:
            return False

def main():
    n = Number(28)
    print("List of Factor : " ,n.getFactor())
    print("Sum of Factor : " ,n.sumfactor())
    print("IS Prime number ?  " ,n.isPrime())
    print("IS Perfect number ? ", n.isPerfectNum())

    print()

    n2 = Number(38)
    print("List of Factor : " ,n2.getFactor())
    print("Sum of Factor : " ,n2.sumfactor())
    print("IS Prime number ?  " ,n2.isPrime())
    print("IS Perfect number ? ", n2.isPerfectNum())
    
if __name__== "__main__":
    main()
    