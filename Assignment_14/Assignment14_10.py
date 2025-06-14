class Employee():
    def __init__(self, Name, Salary, dept):
        self.name =  Name
        self.__salary =Salary
        self._department = dept
    
    def Display(self):
        print(self.name)
        print(self.__salary)
        print(self._department)

def main():
    obj =Employee("ABC" , 220000, "Mech")
    obj.Display()
    print("Outside Class Access Types")
    print(obj.name)
    print(obj._department)
    try:
        print(obj.__salary) 
    except Exception as eobj:
        print(eobj)

if __name__ == "__main__":
    main()    
