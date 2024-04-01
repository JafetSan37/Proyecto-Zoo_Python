from Employee import Employee
from Date import Date
class Guide(Employee):
    def __init__(self,name,last_name,birth_date,curp,rfc,salary,hire_date,schedule):
        super().__init__(name,last_name,birth_date,curp,rfc,salary,"Guide",hire_date,schedule)
    def show_guide(self):
        return self.show_employee()