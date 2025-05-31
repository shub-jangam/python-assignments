class Circle:
    pi =3.14 

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumfernace = 0.0
    
    def Accept(self,r):
        self.radius = r

    def CalculateArea(self):
        self.area = Circle.pi * self.radius * self.radius
        return self.area
    
    def CalculateCircumfernce(self):
        self.circumfernace = 2*Circle.pi *self.radius
        return self.circumfernace

    def Display(self):
        print("Radius of Circle : ", self.radius)
        print("Area of Circle : ", self.area)
        print("Circumfernce of Circle : ", self.circumfernace)
        
def main():
    Obj1 = Circle()
    Obj1.Accept(5.0)
    Obj1.CalculateArea()
    Obj1.CalculateCircumfernce()
    Obj1.Display()
    print("**********New Object************")
    Obj2 = Circle()
    Obj2.Accept(1.0)
    Obj2.CalculateArea()
    Obj2.CalculateCircumfernce()
    Obj2.Display()

if __name__ =="__main__":
    main()