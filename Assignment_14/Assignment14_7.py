class Person():
    def __init__(self , name , age):
        self.name = name 
        self.age = age
        print("Name " , self.name)
        print("age" , age)

class Teachaer(Person):
    def __init__(self, name , age , subject, salary):
        super().__init__(name , age)
        self.subject =subject
        self.salary = salary
        Teachaer.display(self)

    def display(self):
        print(self.subject)
        print(self.salary)

def main():
    t1 = Teachaer("AbC",28 ,"C++", 22000)

if __name__ == "__main__":
    main()
