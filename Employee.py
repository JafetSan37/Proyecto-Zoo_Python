from Person import Person
#Clase heredera de la clase Person
class Employee (Person):
    def __init__(self,name,last_name,birth_date,curp,rfc,salary,rol,hire_date,schedule):
        super().__init__(name,last_name,birth_date,curp)
        self.rfc = rfc
        self.salary = salary
        self.rol = rol
        self.hire_date = hire_date
        self.schedule = schedule
    #Métodos de la clase
    def set_salary(self,salary):
        self.salary = float(salary)
    def set_rfc(self,rfc):
        self.rfc = rfc
    def set_schedule(self,schedule):
        self.schedule = schedule
    def show_employee(self):
        return self.show_info() + f"\n   RFC: {self.rfc}\n   Salary: ${self.salary}\n   Posición: {self.rol}\n   Fecha de Contratación: {self.hire_date.show_date()}\n   Horario: {self.schedule}\n"
    def modify_employee(self):
        print("¿Qué aspecto desea modificar?\n1) Nombre\n2) Apellido\n3) Fecha de Nacimiento\n4) CURP\n5) RFC\n6) Salario\n7) Horario")
        selection = int(input("\n"))
        #En Python no existe el switch, por lo que se recurre al uso del if y else if
        #En los casos 1,2,3 y 4, se llaman a los métodos de la clase padre Person mediante super()
        if(selection==1):
            new_name = input("\nIngrese el nombre: ")
            self.set_name(new_name)
        elif(selection==2):
            new_last_name = input("\nIngrese el apellido: ")
            self.set_last_name(new_last_name)
        elif(selection==3):
            self.get_birth_date().modify_date()
        elif(selection==4):
            new_curp = input("\nIngrese CURP: ")
            self.set_curp(new_curp)
        elif(selection==5):
            rfc = input("\nIngrese el RFC: ")
            self.set_rfc(rfc)
        elif(selection==6):
            salary = float(input("\nIngrese el salario: "))
            self.set_salary(salary)
        elif(selection==7):
            schedule = input("\nIngrese nuevo horario: ")
            self.set_schedule(schedule)
        else:
            print("\nOpción no válida")
        print(f"\nEmpleado modificado:\n{self.show_employee()}")