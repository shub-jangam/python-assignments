class Employee():
    def __init__(self,employee_name, employee_id, employee_salary):
        self.name = employee_name
        self.emp_id = employee_id
        self.salary = employee_salary
    
    def Display(self):
        print("Name :" + self.name , end= "")
        print(", ID :" + self.emp_id, end = "")
        print(", Salary :" , self.salary, end= "")
        
def main():
    emp1 =  Employee("Rohit", "ABC-101", 25000)
    emp1.Display()

if __name__ == "__main__":
    main()