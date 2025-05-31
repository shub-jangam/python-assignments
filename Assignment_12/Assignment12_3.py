import random

class Arthematic:

    def __init__(self):
        self.value1 = 0.0
        self.value2 = 0.0
    
    def Accept(self,a ,b):
        self.value1 = a
        self.value2 = b

    def Addition(self):
       output = self.value1 + self.value2
       return output
       
    def Subtraction(self):
       output = self.value1  - self.value2
       return output
    
    def Division(self):
       output = self.value1 / self.value2
       return output
    
    def multi(self):
       output = self.value1 * self.value2
       return output
        
def main():

    my_list = [0, 1, 2, 3, 4, 5, 6]
    print("This is arthematic program")

    for i in range(3):
        print("*****New Object*****")
        v1 = random.choice(my_list) 
        print("Values for V1 : ", v1)
        v2 = random.choice(my_list)
        print("Values for V2 : ", v2)
        Obj1 = Arthematic()
        Obj1.Accept(a = v1 ,b =v2)
        add  = Obj1.Addition()
        print("Addition : ",add)
        subb=Obj1.Subtraction()
        print("SubTraction ",subb)
        multi =Obj1.multi()
        print("Multification : " ,multi)
        try:
            divison=Obj1.Division()
            print("Division : ", divison)
        except ZeroDivisionError as zobj:
            print("second parameter cant be zero")

if __name__ =="__main__":
    main()