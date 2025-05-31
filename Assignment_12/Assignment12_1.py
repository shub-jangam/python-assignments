class Demo:
    Value =0 

    def __init__(self, a, b):
        self.no1 = a
        self.no2 = b
    
    def fun(self):
        print("Inside Fun")
        print(self.no1)
        print(self.no2)

    def gun(self):
        print("Inside gun")
        print(self.no1)
        print(self.no2)
        
def main():
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.fun()
    Obj2.fun()

    Obj1.gun()
    Obj2.gun()

if __name__ =="__main__":
    main()