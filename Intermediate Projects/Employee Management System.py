class Employee:
    employee_details = []

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        Employee.employee_details.append({'Name': self.name, 'Employee ID': self.employee_id, 'Salary': self.salary})

    def display_info(self):
        print(f"Name: {self.name}\n"
              f"Employee ID: {self.employee_id}\n"
              f"Salary: {self.salary}")
        
class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

    def increase_salary(self, increment):
        total_salary = (self.salary * increment/100)+self.salary
        print(f"{self.name} new salary after a {increment}% increase: ${int(total_salary)}")


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    def increase_salary(self, increment):
        total_salary = (self.salary * increment/100)+self.salary
        print(f"{self.name} new salary after a {increment}% increase: ${int(total_salary)}")
