class Student():

    school_name = ""
    
    def __init__(self,name , roll_no,school_name):
        self.name= name
        self.roll_no = roll_no
        Student.school_name = school_name
      
    def display(self):
        print("School Name : " ,Student.school_name)
        print("Student Name" , self.name)
        print("Roll No :" , self.roll_no)

def main():
    b1 = Student("Mark", "1234","Marvellous Info School")
    b1.display()

    
if __name__ == "__main__":
    main()