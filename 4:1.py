class Employee:
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    def details(self):
        return f"Name: {self.name}\nEmployee ID: {self.employee_id}\nDepartment: {self.department}"

employee1 = Employee("Ashlin", "11", "Btech")
print(employee1.details())


