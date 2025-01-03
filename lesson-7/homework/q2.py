class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.empId = employee_id
        self.name = name
        self.position = position
        self.salary = salary

class EmployeeManager:
    FILE_NAME = "employees.txt"
    def __init__(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                self.data_list = file.read()
        except FileNotFoundError:
            with open(self.FILE_NAME, "w") as file:
                pass
    
    def add_employee(self):
        employee_id = input("Enter Employee ID: ").strip()
        if self.employee_exists(employee_id):
            print("Employee ID already exists. Try again.")
            return
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")

        employee = Employee(employee_id, name, position, salary)
        with open(self.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def employee_exists(self):
