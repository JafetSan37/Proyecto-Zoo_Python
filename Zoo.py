from Guide import Guide
from Maintenance import Maintenance
from Management import Management
from Vet import Vet
from Visit import Visit
from Visitor import Visitor
"""from Animals import Animals"""
"""from Care import Care"""
from Date import Date
class Zoo:
    def __init__(self):
        self.__guides = []
        self.__maintenances = []
        self.__vets = []
        self.__managements = []
        self.__visitors = []
        self.__visits = []
        self.__animals = []
        self.__cares = []

    def add_employee(self):
        name = input("Ingrese el nombre: ")
        lastName = input("Ingrese el apellido: ")
        # Seleccionar fechas
        print("Fecha de Nacimiento")
        date_of_birth = self.__register_date()
        print("Fecha de contratación")
        hire_date = self.__register_date()
        if date_of_birth!=None and hire_date!=None:
            curp = input("Ingrese la curp: ")
            rfc = input("Ingrese el RFC: ")
            salary = float(input("Ingrese el salario: "))
            schedule = input("Ingrese el horario: ")
            print("Seleccione el tipo de empleado: \n1. Guia\n2. Veterinario\n3. Mantenimiento\n4. Administracion")
            opcion = int(input())
            if opcion == 1:
                self.__guides.append(Guide(name, lastName, date_of_birth, curp, rfc, salary, hire_date, schedule))
                print("Guia agregado con exito")
            elif opcion == 2:
                self.__vets.append(Vet(name, lastName, date_of_birth, curp, rfc, salary, hire_date, schedule))
                print("Veterinario agregado con exito")
            elif opcion == 3:
                self.__maintenances.append(Maintenance(name, lastName, date_of_birth, curp, rfc, salary, hire_date, schedule))
                print("Empleado de mantenimiento agregado con exito")
            elif opcion == 4:
                self.__managements.append(Management(name, lastName, date_of_birth, curp, rfc, salary, hire_date, schedule))
                print("Administrador agregado con exito")
            else:
                print("No fue posible agregar el empleado")
        else:
            print("La fecha no es valida, no se pudo realizar el registro")

    def __register_date(self):
        print("Dia (1-31): ")
        day = int(input())
        print("Mes(1-12): ")
        month = int(input())
        print("Año(AAAA): ")
        year = int(input())
        if self.__validate_date(day, month, year):
            return date(year, month, day)
        return None

    @staticmethod
    def __validate_date(day, month, year):
        if day < 1 or day > 31:
            return False
        if month < 1 or month > 12:
            return False
        if year < 1900 or year > 2024:
            return False
        return True
    
    def show_guides(self):
        if len(self.__guides)==0:
            print("No hay guias registrados")
        else:
            i = 1
        for guide in self.__guides:
            print(f"{i}) {guide.show_guide()}")
            i += 1
    def show_vets(self):
        if len(self.__vets)==0:
            print("No hay veterinarios registrados")
        else:
            i = 1
        for vet in self.__vets:
            print(f"{i}) {vet.show_vet()}")
            i += 1
    def show_managements(self):
        if len(self.__managements)==0:
            print("No hay empleados de mantenimiento registrados")
        else:
            i = 1
        for management in self.__managements:
            print(f"{i}) {management.show_management()}")
            i += 1
    def show_maintenances(self):
        if len(self.__maintenances)==0:
            print("No hay veterinarios registrados")
        else:
            i = 1
        for maintenance in self.__maintenances:
            print(f"{i}) {maintenance.show_maitenance()}")
            i += 1
    def show_animals(self):
        if len(self.__vets)==0:
            print("No hay animales registrados")
        else:
            i = 1
        for animal in self.__animals:
            print(f"{i}) {animal.show_animal()}")
            i += 1
            
    def show_visitors(self):
        if len(self.__visitors)==0:
            print("No hay visitantes registrados")
        else:
            i = 1
        for visitor in self.__visitors:
            print(f"{i}) {visitor.show_visitor()}")
            i += 1
            
    def show_vets(self):
        if len(self.__vets)==0:
            print("No hay veterinarios registrados")
        else:
            i = 1
        for vet in self.__vets:
            print(f"{i}) {vet.show_vet()}")
            i += 1
            
    def show_employees(self):
        print("Guias:\n")
        self.show_guides()
        print("Veterinarios:\n")
        self.show_vets()
        print("Mantenimiento:\n")
        self.show_maintenances()
        print("Administradores:\n")
        self.show_managements()
        
    def add_visitors(self):
        # nombre completo
        name = input("Ingrese el nombre: ")
        last_name = input("Ingrese el apellido: ")
        if not name or not last_name:
            print("Debe llenar el nombre completo correctamente")
            return
        # Registro de fecha de nacimiento
        print("Registro de fecha de nacimiento")
        birth_date = self.__register_date()
        if birth_date==None:
            print("Fecha de nacimiento no válida")
            return

        # Ingrese la CURP
        curp = input("Ingrese la CURP: ")  # ¿Deberíamos hacer un método para validar la CURP?
        # Fecha de registro del visitante
        print("Fecha de registro del visitante: ")
        register_date = self.register_date()
        if register_date is None:
            print("Fecha de registro no válida")
            return

        # Crear el visitante
        new_visitor = Visitor(name, last_name, birth_date, curp, register_date)
        # Agregarlo a la lista
        self.visitors.append(new_visitor)
        print("Visitante creado con éxito")     
        
        
        
        