class Book():
    def __init__(self):
        self.__price= 0
        
    def getPrice(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

def main():
    b1 = Book()
    #b1.set_price(200)
    print(b1.getPrice())
    
if __name__ == "__main__":
    main()