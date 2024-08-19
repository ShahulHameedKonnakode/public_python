#Employee Management System

class Employee:
     def __init__(self):
        self.directory={}
        self.database={}
    
     def addEmployee(self,id_no, name, job, department):
        self.directory["Id"]=id_no
        self.directory["Name"]=name
        self.directory["Job"]=job
        self.directory["Department"]=department

        self.database[id_no]=self.directory
        print("\n✅ Employee Details are Added Successfully...Thank You")
        print(f"\nEmployee ID: {id_no}, Name: {name}, Job Title: {job}, Department: {department}")

     def look_up_an_employee(self,check_value):
        self.check_value=check_value
        if check_value in self.database:
             print("\nThe Employee Details:\nEmployee ID:",self.database[id_no]["Id"], "Name:",self.database[id_no]["Name"], "Job Title:",self.database[id_no]["Job"], "Department:",self.database[id_no]["Department"])
        else:
            print("The Employee Not Found")


     def update_employee_details(self,staff_data_to_change):
        if not staff_data_to_change in self.database:
            print("Employee Not Found")
        else:
            print("Please Enter Which Type of Data Do You Want to Update:  \n1.Employee Name\n2.Job Title\n3.Department of Employee")
            option=int(input("Please Enter an Option No.:  "))
            self.option=option
            
            if self.option == 1:
                name_to_change=input("Enter the New Name: ")
                self.database[staff_data_to_change].update({"Name":name_to_change})

            elif self.option == 2:
                job_to_change=input("Enter the New Job Title: ")
                self.database[staff_data_to_change].update({"Job":job_to_change})

            elif self.option == 3:
                department_to_change=input("Enter the New Name: ")
                self.database[staff_data_to_change].update({"Department":department_to_change})
            else:
                print("Please Enter a Valid Option")

     def delete_employee(self,del_employee):
        self.del_employee=del_employee
        if not del_employee in self.database:
            print("Employee Not Found")
        else:
            self.database.pop(self.del_employee)
            print("\n✅ Employee is Deleted Successfully...Thank You")

    




company=Employee()



# main


while True:
    menu={"1": "Add a new employee","2": "Look up an employee","3": "Change an existing employee's details","4": "Delete an employee","5": "Quit"}

    print("\n🔰 Employee Management System 🔰\n")
    print("Please Select an Option: ")

    for key,value in menu.items():
        print(f"{key}.{value}")



    choice=int(input("\nEnter Your Choice:  "))

    if choice == 1 :
        id_no=int(input("Enter the Employee ID No.:  "))
        name=input("Enter the Employee Name: ")
        job=input("Enter the Job Title: ")
        department=input("Enter the Department of Employee: ")
        

        company.addEmployee(id_no, name, job, department)

    elif choice == 2 :
        check_value=int(input("Enter Employee ID No.:  "))
        company.look_up_an_employee(check_value)

    elif choice == 3 :
        staff_data_to_change=int(input("Enter the Employee ID No.:  "))
        company.update_employee_details(staff_data_to_change)
        print("You Data is Successfully Updated...")

    elif choice == 4 :
        del_employee=int(input("Enter the Employee ID No.:  "))
        company.delete_employee(del_employee)

    elif choice == 5 :
        print("Employee Management System is Exiting......Good Bye! Have a Nice Day!!...")
        break
    else:
         print("Please Enter a Valid Option")
