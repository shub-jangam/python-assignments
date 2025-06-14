class Rectangle():
    def __init__(self,lenght, width, ):
        self.lenght = lenght
        self.width = width
    
    def Area(self):
        ret = self.lenght * self.width
        print(" Area :" ,  ret , end= "")
    
    def perimeter(self):
            ret = (self.lenght + self.width)*2
            print(", Perimeter :" ,  ret , end= "")
    
        
def main():
    obj1 =  Rectangle(10,5)
    obj1.Area()
    obj1.perimeter()

if __name__ == "__main__":
    main()