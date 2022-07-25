class Person(object):

    def _init_(self,name,dob,department):
        self.name = name
        self.dob = dob
        self.department = department

    def Display(self):
        print("Name: ",self.name)
        print("DOB: ",self.dob)
        print("Department: ",self.department)

class Student(Person):
    comp = 0
    it = 0
    def _init_(self,name,dob,department,prn,year,cgpa):
        self.prn = prn
        self.year = year
        self.cgpa = cgpa
        Person._init_(self, name, dob, department)

        if department == "COMPUTER":
            Student.comp += cgpa

        elif department == "IT":
            Student.it += cgpa
            

    def Stu_Display(self):
        print("Student's Name: ",self.name)
        print("Student's DOB: ",self.dob)
        print("Student's Department: ",self.department)
        print("Student's PRN: ",self.prn)
        print("Student's Year: ",self.year)
        print("Student's CGPA: ",self.cgpa)
        

class Employee(Person):
    def _init_(self,name,dob,department,emp_id,salary):
        self.emp_id = emp_id
        self.salary = salary
        Person._init_(self, name, dob, department)

    def Emp_Display(self):
        print("Employee Name: ",self.name)
        print("Employee DOB: ",self.dob)
        print("Employee Department: ",self.department)
        print("Employee ID: ",self.emp_id)
        print("Employee Salary: ",self.salary)
class Lab_ast(Employee):
    counter = 0
    delete = 0
    
    def _init_(self,name,dob,department,emp_id,salary,lab):
        self.lab = lab
        Employee._init_(self,name,dob,department, emp_id, salary)
        Lab_ast.counter += salary
        Lab_ast.delete  = emp_id
        
            

    def Emp_Lab(self):
        print("Employee Name: ",self.name)
        print("Employee DOB: ",self.dob)
        print("Employee Department: ",self.department)
        print("Employee ID: ",self.emp_id)
        print("Employee Salary: Rs.",self.salary)
        print("Lab Name : ",self.lab)

    

    

    

class Faculty(Employee):
    counter = 0
    def _init_(self,name,dob,department,emp_id,salary,Sub_teching,No_RP,qualification):
        self.Sub_teching = Sub_teching
        self.No_RP = No_RP
        self.qualification = qualification
        Employee._init_(self,name,dob,department, emp_id, salary)
        Faculty.counter += salary

    def Faculty_Display(self):
        print("Employee Name: ",self.name)
        print("Employee DOB: ",self.dob)
        print("Employee Department: ",self.department)
        print("Employee ID: ",self.emp_id)
        print("Employee Salary: Rs.",self.salary)
        print("Subject Teaching: ",self.Sub_teching)
        print("No. of Research Papers: ",self.No_RP)
        print("Qualification: ",self.qualification)
        
        


lab1 = Lab_ast("Mrs. Sneha","02-03-1989","COMPUTER",101,124550,"Python Programming")
lab2 = Lab_ast("Mrs. Sakshi","02-03-1990","COMPUTER",102,124550,"Operating System")
lab3 = Lab_ast("Mrs. Pooja","02-03-1990","COMPUTER",103,124550,"DLM")


fact1= Faculty("Prof. Netak","09-06-1987","COMPUTER",201,125000,"Operating System",0,"B.Tech")
fact2= Faculty("Prof. Laddha","09-06-1987","COMPUTER",202,125000,"Microprocessor",2,"M.Tech")
fact3= Faculty("Prof. Snehal","09-06-1987","COMPUTER",203,150000,"Machine Learning",4,"PhD")


stud1 = Student("Sneha Sanjay tembe","08-08-2003","COMPUTER",2130331245504,"SECOND YEAR",8.75)
stud2 = Student("Pooja Pradeep Deokar","03-10-2003","COMPUTER",2130331245503,"SECOND YEAR",8.75)
stud3 = Student("Trupti Tejas Mahabale","02-05-2002","COMPUTER",2130331245502,"SECOND YEAR",8.50)
stud4 = Student("Tanvi Sanjay Palkar","22-03-2003","COMPUTER",2130331245501,"SECOND YEAR",9.75)


stud5 = Student("Harsh Gujral","20-01-1999","IT",2130331246504,"SECOND YEAR",7)
stud6 = Student("Anubhav Bassi","03-07-2001","IT",2130331265503,"SECOND YEAR",8)
stud7 = Student("Zakir Khan","02-12-2000","IT",2130331246502,"SECOND YEAR",8)
stud8 = Student("Tanmay Bhat","22-11-2002","IT",2130331246501,"SECOND YEAR",8)


print("\t \t ---MENU---\n \
        1: Display Data of Lab Assistants. \n \
        2: Display Data of Faculty. \n \
        3: Diplay Data of Students. \n \
        4: Display Total Salary of all employees. \n \
        5: Display Average CGPA of  students department wise. \n \
        6: Delete Data of Employee or Student: \n \
        7: To Exit:  ")

choice = int(input("Enter Choice: "))
while choice != 7:
    
    if choice == 1:
        #Lab Assistant Object
        print("Details of Lab Assistant")
        
        lab1.Emp_Lab()
        print()
        
        lab2.Emp_Lab()
        print()
        
        lab3.Emp_Lab()
        print()
        

    elif choice == 2:
        
        print("Details of Faculty")    
        fact1.Faculty_Display()
        print()
        
        fact2.Faculty_Display()
        print()
        
        fact3.Faculty_Display()
        print()
        
    elif choice == 3:
        
        print()
        print("Details of Student")
        stud4.Stu_Display()
        print()
        stud3.Stu_Display()
        print()
        stud2.Stu_Display()
        print()
        stud1.Stu_Display()
        print()
        stud5.Stu_Display()
        print()
        stud6.Stu_Display()
        print()
        stud7.Stu_Display()
        print()
        stud8.Stu_Display()
        print()

    elif choice == 4:
        total = 0
        total += Lab_ast.counter
        total += Faculty.counter
        print("Total Salary of all Employees: Rs.",total)

    elif choice == 5:

        print("Average CGPA of COMPUTER Department---> ",Student.comp/4)
        print("Average CGPA of IT Department----> ",Student.it/4)

    elif choice == 6:
        e_id = int(input("ENTER EMPLOYEE ID or PRN OF EMPLOYEE or STUDENT TO BE DELETED: "))
        if lab1.emp_id == e_id:
            print("Employee Named {0} is Fired!".format(lab1.name))
            del lab1
            print()
            lab2.Emp_Lab()
            print()
            lab3.Emp_Lab()

        elif lab2.emp_id == e_id:
            print("Employee Named {0} is Fired!".format(lab1.name))
            del lab2
            print()
            lab1.Emp_Lab()
            print()
            lab3.Emp_Lab()

        elif lab3.emp_id == e_id:
            print("Employee Named {0} is Fired!".format(lab1.name))
            del lab3
            print()
            lab1.Emp_Lab()
            print()
            lab2.Emp_Lab()

        elif fact1.emp_id == e_id:
            print("Employee Named {0} is Fired!".format(fact1.name))
            del fact1
            print()
            fact2.Faculty_Display()
            print()
            fact3.Faculty_Display()

        elif fact2.emp_id == e_id:
            print("Employee Named {0} is Fired!".format(fact2.name))
            del fact2
            print()
            fact1.Faculty_Display()
            print()
            fact3.Faculty_Display()

        elif fact3.emp_id == e_id:
            print("Employee Named {0} is Fired!".format(fact3.name))
            del fact3
            print()
            fact1.Faculty_Display()
            print()
            fact2.Faculty_Display()

        elif stud1.prn == e_id:
            print("Student Named {0} is removed!".format(stud1.name))
            print()
            del stud1
            stud4.Stu_Display()
            print()
            stud3.Stu_Display()
            print()
            stud2.Stu_Display()
            print()
            stud5.Stu_Display()
            print()
            stud6.Stu_Display()
            print()
            stud7.Stu_Display()
            print()
            stud8.Stu_Display()
            print()

        elif stud2.prn == e_id:
            print("Student Named {0} is removed!".format(stud2.name))
            print()
            del stud2
            stud4.Stu_Display()
            print()
            stud3.Stu_Display()
            print()
            stud1.Stu_Display()
            print()
            stud5.Stu_Display()
            print()
            stud6.Stu_Display()
            print()
            stud7.Stu_Display()
            print()
            stud8.Stu_Display()
            print()

        elif stud3.prn == e_id:
            print("Student Named {0} is removed!".format(stud3.name))
            print()
            del stud3
            stud4.Stu_Display()
            print()
            stud2.Stu_Display()
            print()
            stud1.Stu_Display()
            print()
            stud5.Stu_Display()
            print()
            stud6.Stu_Display()
            print()
            stud7.Stu_Display()
            print()
            stud8.Stu_Display()
            print()
        elif stud4.prn == e_id:
            print("Student Named {0} is removed!".format(stud4.name))
            print()
            del stud4
            stud3.Stu_Display()
            print()
            stud2.Stu_Display()
            print()
            stud1.Stu_Display()
            print()
            stud5.Stu_Display()
            print()
            stud6.Stu_Display()
            print()
            stud7.Stu_Display()
            print()
            stud8.Stu_Display()
            print()

        elif stud5.prn == e_id:
            print("Student Named {0} is removed!".format(stud5.name))
            del stud5
            stud4.Stu_Display()
            print()
            stud3.Stu_Display()
            print()
            stud2.Stu_Display()
            print()
            stud1.Stu_Display()
            print()
            stud6.Stu_Display()
            print()
            stud7.Stu_Display()
            print()
            stud8.Stu_Display()
            print()

        elif stud6.prn == e_id:
            print("Student Named {0} is removed!".format(stud6.name))
            print()
            del stud6
            stud4.Stu_Display()
            print()
            stud3.Stu_Display()
            print()
            stud2.Stu_Display()
            print()
            stud1.Stu_Display()
            print()
            stud5.Stu_Display()
            print()
            stud7.Stu_Display()
            print()
            stud8.Stu_Display()
            print()

        elif stud7.prn == e_id:
            print("Student Named {0} is removed!".format(stud7.name))
            print()
            del stud7
            stud4.Stu_Display()
            print()
            stud3.Stu_Display()
            print()
            stud2.Stu_Display()
            print()
            stud1.Stu_Display()
            print()
            stud5.Stu_Display()
            print()
            stud6.Stu_Display()
            print()
            stud8.Stu_Display()
            print()

        elif stud8.prn == e_id:
            print("Student Named {0} is removed!".format(stud8.name))
            print()
            del stud8
            stud4.Stu_Display()
            print()
            stud3.Stu_Display()
            print()
            stud2.Stu_Display()
            print()
            stud1.Stu_Display()
            print()
            stud5.Stu_Display()
            print()
            stud6.Stu_Display()
            print()
            stud7.Stu_Display()
            print()
        

        else:
            print("You Entered Wrong Employee ID or Student PRN")
            print()
    print()
    choice = int(input("Enter Choice: "))
