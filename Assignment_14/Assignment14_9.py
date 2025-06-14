class Product():
    
    def __init__(self, name, price):
        self.name  = name 
        self.price = price
    
    def __eq__(self, value):
        if isinstance(value, Product):
            return self.price == value.price
        return False
    
def main():
    p1 = Product("Python" ,22000)
    p2 = Product("PPA", 22000)
    p3 = Product("LB",21000)

    print(p1 == p2)
    print(p1 == p3)

if __name__ == "__main__":
    main()