from Employee import Employee
from Date import Date
class Management(Employee):
    def __init__(self,name,last_name,birth_date,curp,rfc,salary,hire_date,schedule):
        super().__init__(name,last_name,birth_date,curp,rfc,salary,"Management",hire_date,schedule)
    def show_management(self):
        return self.show_employee()