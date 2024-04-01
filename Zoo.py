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
        if name==None or last_name==None:
            print("Debe llenar el nombre completo correctamente")
            return
        # Registro de fecha de nacimiento
        print("Registro de fecha de nacimiento")
        birth_date = self.__register_date()
        if birth_date is None:
            print("Fecha de nacimiento no válida")
            return

        # Ingrese la CURP
        curp = input("Ingrese la CURP: ")  # ¿Deberíamos hacer un método para validar la CURP?
        # Fecha de registro del visitante
        print("Fecha de registro del visitante: ")
        register_date = self.__register_date()
        if register_date is None:
            print("Fecha de registro no válida")
            return

        # Crear el visitante
        new_visitor = Visitor(name, last_name, birth_date, curp, register_date)
        # Agregarlo a la lista
        self.__visitors.append(new_visitor)
        print("Visitante creado con éxito")     
        
        
    #Métodos Jaf
    
    def show_visits(self):
        if(len(self.__visits)==0):
            print("\nNo hay visitas para mostrar")
        else:
            for i, visit in enumerate(self.__visits, 1):
                print(f"Visita: {i} {visit.show_visit()}")
                print(".....................................")

    def show_care_list(self):
        if(len(self.__cares)==0):
            print("\nNo hay registros")
        else:
            print(">>> Lista de Cuidados <<<")
            for i, care in enumerate(self.__cares, 1):
                print(f"{i}) {care.show_care}")
    
    def tester(self):
        birth_date_alex = Date(4, 2, 2003)
        birth_date_atziri = Date(5, 6, 1996)
        birth_date_jafet = Date(30, 1, 1997)
        birth_date_alan = Date(5, 6, 1996)
        register_date_alan = Date(31, 3, 2024)
        birth_date_pao = Date(23, 4, 1997)
        register_date_pao = Date(30, 3, 2024)
        birth_date_marcos = Date(15, 1, 1990)
        birth_date_fany = Date(7, 6, 2003)
        birth_date_rubi = Date(10, 2, 1996)
        birth_date_more = Date(25, 8, 2003)
        birth_date_ed = Date(23, 1, 2000)
        register_date_marcos = Date(25, 2, 2014)
        register_date_fany = Date(12, 4, 2005)
        register_date_rubi = Date(25, 8, 2019)
        register_date_more = Date(26, 8, 2008)
        register_date_ed = Date(20, 9, 2019)
        visit_date = Date(31, 3, 2024)
        hire_date_general = Date(2, 1, 2005)
        guide_schedule = "Mie-Dom 9-17"

        guide1 = Guide("Alejandro", "Montejano", birth_date_alex, "MODA030204LMN01", "MODA83726", 2000, hire_date_general, guide_schedule)
        guide2 = Guide("Jafet", "Santoyo", birth_date_jafet, "SABE970130LJBSA01", "SABJ87657", 2000, hire_date_general, guide_schedule)
        guide3 = Guide("Atziri", "Mancilla", birth_date_atziri, "MACA05061997LMN12", "MACA0506199710", 2001, hire_date_general, guide_schedule)
        self.__guides.append(guide1)
        self.__guides.append(guide2)
        self.__guides.append(guide3)
        visitor1 = Visitor("Alan", "Lopez", birth_date_alan, "LOMA220522HHNOSE", register_date_alan)
        visitor2 = Visitor("Paola Itzel", "Cobián", birth_date_pao, "NECO970423HLOUWU", register_date_pao)
        visitor3 = Visitor("Marcos", "Sánchez", birth_date_marcos, "SAHM9862543HOLI", register_date_marcos)
        visitor4 = Visitor("Estefanía", "López", birth_date_fany, "ESLO982345JAHSBR", register_date_fany)
        visitor5 = Visitor("Rubi", "Martinez", birth_date_rubi, "RUBA986543JSHLKL", register_date_rubi)
        visitor6 = Visitor("Morelia", "Durán", birth_date_more, "MODU030825JSHDGET", register_date_more)
        self.__visitors.append(visitor1)
        self.__visitors.append(visitor2)
        self.__visitors.append(visitor3)
        self.__visitors.append(visitor4)
        self.__visitors.append(visitor5)
        self.__visitors.append(visitor6)
        visit1 = Visit(guide3, visit_date)
        visit1.add_visitor(visitor1)
        visit1.add_visitor(visitor2)
        visit1.add_visitor(visitor3)
        visit2 = Visit(guide1, visit_date)
        visit2.add_visitor(visitor4)
        visit2.add_visitor(visitor5)
        visit2.add_visitor(visitor6)
        self.__visits.append(visit1)
        self.__visits.append(visit2)
        hire_date = Date(2, 2, 2020)
        
        vet1 = Vet("Eduardo", "Martinez", birth_date_ed, "MARE8976625LKJ", "JDHSGHKL1625", 2000, hire_date, "L-V 8-4")
        self.__vets.append(vet1)
        manager = Management("Dr professor", "Alejandro", birth_date_alex, "MODA030204JSHDG", "KDJDHSKL", 3000, hire_date, "L-V 8-4")
        self.__managements.append(manager)
        maintenance1 = Maintenance("Juan", "Pérez", birth_date_marcos, "JDHHG09876123", "HDGHAJK1278", 2000, hire_date_general, "L-V 8-4")
        maintenance2 = Maintenance("Diana", "Garnica", birth_date_fany, "JHGJKLLJJK", "JDHSKLN", 2000, hire_date_general, "M-D 12-8")
        self.__maintenances.append(maintenance1)
        self.__maintenances.append(maintenance2)

        arrival_date = Date(2, 6, 2000)
        animal_birth_date = Date(23, 3, 1990)
        animal1 = Animals("Dolphin", arrival_date, "piscivorous", animal_birth_date, 100.5, 7, True)
        animal2 = Animals("Capybara", arrival_date, "grasses, berries, seeds", animal_birth_date, 35, 14, True)
        animal3 = Animals("Penguin", arrival_date, "piscivorous", animal_birth_date, 30, 14, True)
        animal4 = Animals("Flamingo", arrival_date, "crustaceans", animal_birth_date, 3, 7, True)
        animal5 = Animals("Elephant", arrival_date, "grasses, fruit, tree bark, roots", animal_birth_date, 5000, 21, True)
        animal6 = Animals("Panda", arrival_date, "Bambu", animal_birth_date, 80, 14, True)
        animal7 = Animals("Red panda", arrival_date, "Fruits, roots, bambu", animal_birth_date, 14, 4, True)
        animal8 = Animals("Rattlesnake", arrival_date, "rats", animal_birth_date, 4, 1, True)
        animal9 = Animals("Galapagos giant tortoise", arrival_date, "fruit, leaves, vegetables", animal_birth_date, 40, 5, True)
        animal10 = Animals("White tiger", arrival_date, "carnivorous", animal_birth_date, 1000, 3, True)
        self.__animals.append(animal1)
        self.__animals.append(animal2)
        self.__animals.append(animal3)
        self.__animals.append(animal4)
        self.__animals.append(animal5)
        self.__animals.append(animal6)
        self.__animals.append(animal7)
        self.__animals.append(animal8)
        self.__animals.append(animal9)
        self.__animals.append(animal10)

        process_date = Date(31, 3, 2024)
        care1 = Care(maintenance1, "Alimentar", 0, process_date, "comió poquito :(")
        care2 = Care(maintenance2, "Curacion", 4, process_date, "Mejora significativa en sus heridas")
        self.__cares.append(care1)
        self.__cares.append(care2)

    def modify_employee(self):
        print("\nSeleccione el tipo de empleado:\n1. Guía\n2. Veterinario\n3. Mantenimiento\n4. Administración")
        opcion = int(input("\n"))
        if(opcion==1):
            print("\nSeleccione el número")
            self.show_guides()
            opcion = int(input("\n"))
            self.__guides.get(opcion-1).modify()
        elif(opcion==2):
            print("\nSeleccione el número")
            self.show_vets()
            opcion = int(input("\n"))
            self.__vets.get(opcion-1).modify()
        elif(opcion==3):
            print("\nSeleccione el número")
            self.show_maintenances()
            opcion = int(input("\n"))
            self.__maintenances.get(opcion-1).modify()
        elif(opcion==4):
            print("\nSeleccione el número")
            self.show_managements()
            opcion = int(input("\n"))
            self.__managements.get(opcion-1).modify()
        else: print("\nOpción no válida")
    def modify_visitor(self):
        self.show_visitors()
        opcion = int(input("\nIngrese el número de visitante: "))
        self.__visitors.get(opcion-1).modify()