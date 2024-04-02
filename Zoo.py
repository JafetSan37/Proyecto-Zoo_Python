from Guide import Guide
from Maintenance import Maintenance
from Management import Management
from Vet import Vet
from Visit import Visit
from Visitor import Visitor
from Animals import Animals
from Care import Care
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
        name = input("\nIngrese el nombre: ")
        lastName = input("\nIngrese el apellido: ")
        # Seleccionar fechas
        print("\nFecha de Nacimiento")
        date_of_birth = self.__register_date()
        print("\nFecha de contratación")
        hire_date = self.__register_date()
        if date_of_birth!=None and hire_date!=None:
            curp = input("\nIngrese la curp: ")
            rfc = input("\nIngrese el RFC: ")
            salary = float(input("\nIngrese el salario: "))
            schedule = input("\nIngrese el horario: ")
            print("\nSeleccione el tipo de empleado: \n1. Guia\n2. Veterinario\n3. Mantenimiento\n4. Administracion")
            opcion = int(input())
            if opcion == 1:
                self.__guides.append(Guide(name, lastName, date_of_birth, curp, rfc, salary, hire_date, schedule))
                print("\nGuia agregado con exito")
            elif opcion == 2:
                self.__vets.append(Vet(name, lastName, date_of_birth, curp, rfc, salary, hire_date, schedule))
                print("\nVeterinario agregado con exito")
            elif opcion == 3:
                self.__maintenances.append(Maintenance(name, lastName, date_of_birth, curp, rfc, salary, hire_date, schedule))
                print("\nEmpleado de mantenimiento agregado con exito")
            elif opcion == 4:
                self.__managements.append(Management(name, lastName, date_of_birth, curp, rfc, salary, hire_date, schedule))
                print("\nAdministrador agregado con exito")
            else:
                print("\nNo fue posible agregar el empleado")
        else:
            print("\nLa fecha no es valida, no se pudo realizar el registro")

    def __register_date(self):
        print("\nDia (1-31): ")
        day = int(input())
        print("\nMes(1-12): ")
        month = int(input())
        print("\nAño(AAAA): ")
        year = int(input())
        if self.__validate_date(day, month, year):
            return Date(year, month, day)
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
            print("\nNo hay guias registrados")
        else:
            i = 1
        for guide in self.__guides:
            print(f"{i}) {guide.show_guide()}")
            i += 1
    def show_vets(self):
        if len(self.__vets)==0:
            print("\nNo hay veterinarios registrados")
        else:
            i = 1
        for vet in self.__vets:
            print(f"{i}) {vet.show_vet()}")
            i += 1
    def show_managements(self):
        if len(self.__managements)==0:
            print("\nNo hay empleados de mantenimiento registrados")
        else:
            i = 1
        for management in self.__managements:
            print(f"{i}) {management.show_management()}")
            i += 1
    def show_maintenances(self):
        if len(self.__maintenances)==0:
            print("\nNo hay veterinarios registrados")
        else:
            i = 1
        for maintenance in self.__maintenances:
            print(f"{i}) {maintenance.show_maintenance()}")
            i += 1
    def show_animals(self):
        if len(self.__vets)==0:
            print("\nNo hay animales registrados")
        else:
            i = 1
        for animal in self.__animals:
            print(f"{i}) {animal.show_animal()}")
            i += 1
            
    def show_visitors(self):
        if len(self.__visitors)==0:
            print("\nNo hay visitantes registrados")
        else:
            i = 1
        for visitor in self.__visitors:
            print(f"{i}) {visitor.show_visitor()}")
            i += 1
            
    def show_employees(self):
        print("\nGuias:\n")
        self.show_guides()
        print("\nVeterinarios:\n")
        self.show_vets()
        print("\nMantenimiento:\n")
        self.show_maintenances()
        print("\nAdministradores:\n")
        self.show_managements()
        
    def add_visitors(self):
        # nombre completo
        name = input("\nIngrese el nombre: ")
        last_name = input("\nIngrese el apellido: ")
        if name==None or last_name==None:
            print("\nDebe llenar el nombre completo correctamente")
            return
        # Registro de fecha de nacimiento
        print("\nRegistro de fecha de nacimiento")
        birth_date = self.__register_date()
        if birth_date is None:
            print("\nFecha de nacimiento no válida")
            return

        # Ingrese la CURP
        curp = input("\nIngrese la CURP: ")  # ¿Deberíamos hacer un método para validar la CURP?
        # Fecha de registro del visitante
        print("\nFecha de registro del visitante: ")
        register_date = self.__register_date()
        if register_date is None:
            print("\nFecha de registro no válida")
            return

        # Crear el visitante
        new_visitor = Visitor(name, last_name, birth_date, curp, register_date)
        # Agregarlo a la lista
        self.__visitors.append(new_visitor)
        print("\nVisitante creado con éxito")     
    
    def add_visit(self):
        print("\nGuías")
        self.show_guides()
        opcion = int(input("\nIngrese el número de guía: "))
        guide = self.__guides[opcion-1]
        print("\nIngresa la fecha de visita")
        date = self.__register_date()
        if(date==None):
            print("\nError. La fecha ingresada no es válida\n")
        else:
            band = True
            visit = Visit(guide,date)
            self.__visits.append(visit)
            while(band):
                print("\nSi desea ingresar un visitante ingrese el número, ingrese 0 para salir\n")
                self.show_visitors()
                opcion = int(input("\n"))
                if(opcion==0):
                    band = False
                if(opcion>len(self.__visitors)):
                    print("\nIngrese un número de visitante válido\n")
                if(opcion>0 & opcion<=len(self.__visitors)):
                    if(self.validate_visitors(visit,self.__visitors[opcion-1])):
                        visit.add_visitor(self.__visitors[opcion-1])
                        print("\nUsuario agregado")
                    else:
                        print("\nEl usuario ya está en esta visita\n")
            print("\nVisita creada con éxito\n")
    
    def validate_visitors(self, visit, visitor):
        band = True
        if visitor in visit.get_visitors():
            band = False
        return band

        
    def add_animal(self):
        type_animal = input("\nIngrese tipo de animal: ")
        print("\nFecha de llegada")
        arrival_date = self.__register_date()
        if arrival_date is None:
            print("\nFecha no válida")
            return
        diet = input("\nIngrese tipo de dieta: ")
        print("\nFecha Nacimiento")
        birth_date = self.__register_date()
        if birth_date is None:
            print("\nFecha no válida")
            return
        
        weight = float(input("\nIngrese peso (kg): "))
        feeding_frequency = int(input("\nVeces que se alimenta por semana: "))
        vaccinated = int(input("\n¿Tiene sus vacunas?\n 1) Si 2) No\n"))
        if vaccinated == 1:
            is_vaccinated = True
        elif vaccinated == 2:
            is_vaccinated = False
        else:
            print("\nNo es una entrada válida")
            return
        # Crear objeto y añadirlo a la lista
        new_animal = Animals(type_animal, arrival_date, diet, birth_date, weight, feeding_frequency, is_vaccinated)
        self.__animals.append(new_animal)
        print("\nAnimal registrado en sistema")
    
    def add_care(self):
        print("\nSeleccionaste añadir cuidado/mantenimiento")
        print("\nSelecciona el número de empleado a cargo")
        self.show_maintenances()
        employee_selected = int(input()) - 1
        staff = self.__maintenances[employee_selected]

        process_realized = input("\nIngrese proceso realizado: ")
        print("\nSelecciona el número de animal al que realizarás cuidado")
        self.show_animals()
        animal_selected = int(input()) - 1
        selected_animal = self.__animals[animal_selected]
        print("\nSeleccionaste " + selected_animal.show_animal())
        id_animal = selected_animal.get_id()

        print("\nFecha del proceso: ")
        process_date = self.__register_date()
        if process_date is None:
            print("\nFecha no válida")
            return

        observations = input("\nObservaciones (opcional): ")

        # Crear objeto
        new_care = Care(staff, process_realized, id_animal, process_date, observations)
        print("\nCuidado registrado, gracias por cuidar tqm")
        
    def modify_animal_register(self):
        print("\nElija el animal al que desea actualizar su registro")
        self.show_animals()
        opcion = int(input())
        print("\nHas seleccionado: " + self.__animals[opcion - 1].show_animal())
        print("\n¿Qué cambio desea realizar?\n1) Registrar Enfermedad\n2) Actualizar peso\n" +
          "3) Cambiar tipo de alimentación\n4) Cambiar frecuencia de alimentación\n5) Registrar vacunación\n0) Atrás")
        option = int(input())
        animal = self.__animals[opcion - 1]

        if option == 1:
            new_disease = input("\nIngrese enfermedad: ")
            animal.add_disease(new_disease)
            print("\nEnfermedad agregada")
        elif option == 2:
            new_weight = float(input("\nIngrese nuevo peso (Kg): "))
            animal.set_weight(new_weight)
            print("\nEl nuevo peso de " + animal.get_type() + " ||ID: " + str(animal.get_id()) + " es: " + str(animal.get_weight()) + "Kg")
        elif option == 3:
            new_diet = input("\nIngrese nueva dieta: ")
            animal.set_diet(new_diet)
            print("\nDieta actualizada")
        elif option == 4:
            print("\nElegiste cambiar frecuencia de alimentación")
            new_frequency = int(input("\nIngrese número de veces por semana: "))
            animal.set_feeding_frequency(new_frequency)
            print("\nFrecuencia actualizada")
        elif option == 5:
            print("\nElegiste actualizar vacunación")
            decision = int(input("\n¿Tiene todas sus vacunas?\n 1)Si 2) No\n"))
            if decision == 1:
                animal.set_vaccinated(True)
                print("\nAhora " + animal.get_type() + " ||ID: " + str(animal.get_id()) + " está vacunado")
            elif decision == 2:
                animal.set_vaccinated(False)
                print("\nSe ha actualizado que " + animal.get_type() + " ||ID: " + str(animal.get_id()) + " requiere vacunas")
            else:
                print("\nEntrada no válida")
        elif option == 0:
            pass
        else:
            print("\nEntrada no válida")
            
    def delete_employee(self):
        print("\n¿Qué tipo de empleado desea eliminar? \n1. Guia\n2. Veterinario\n3. Mantenimiento\n4. Administracion\n0. Salir\n")
        selection = int(input())

        if selection == 1:
            # Mostrar guías
            self.show_guides()
            guide_to_delete = int(input("\nSelecciona el empleado que desea eliminar: ")) - 1
            self.__guides.pop(guide_to_delete)
            print("\nEmpleado eliminado")

        elif selection == 2:
            # Mostrar veterinarios
            self.show_vets()
            vet_to_delete = int(input("\nSelecciona el empleado que desea eliminar: ")) - 1
            self.__vets.pop(vet_to_delete)
            print("\nEmpleado eliminado")

        elif selection == 3:
            # Mostrar personal de mantenimiento
            self.show_maintenances()
            staff_to_delete = int(input("\nSelecciona el empleado que desea eliminar: ")) - 1
            self.__maintenances.pop(staff_to_delete)
            print("\nEmpleado eliminado")

        elif selection == 4:
            # Mostrar personal de administración
            self.show_managements()
            manager_to_delete = int(input("Selecciona el empleado que desea eliminar")) - 1
            self.__managements.pop(manager_to_delete)
            print("\nEmpleado eliminado")

        elif selection == 0:
            pass

        else:
            print("\nEntrada no válida")
    
    def delete_animal(self):
        i = 1
        print("\nSelecciona el animal a eliminar:")
        for index, animal in enumerate(self.animals):
            print(f"{i}) {animal.show_animal()}")
            i += 1
        selection = int(input()) - 1
        print("\nSeleccionaste: " + self.__animals[selection].show_animal())
        confirmation = int(input("\n¿Estás seguro de que lo quieres eliminar?\n 1) Si 2) Cancelar\n"))
        if confirmation == 1:
            del self.__animals[selection]
            print("\nAnimal eliminado de la base de datos.")
        else:
            print("\nSe canceló su eliminación")
            
    def delete_visitor(self):
        print("\nSeleccione el visitante que desea eliminar: ")
        self.show_visitors()
        visitor_to_delete = int(input()) - 1

        self.__visitors.pop(visitor_to_delete)
        #Métodos Jaf
    
    def show_visits(self):
        if(len(self.__visits)==0):
            print("\nNo hay visitas para mostrar")
        else:
            for i in range(0,len(self.__visits)):
                print(f"Visit {i+1}\n")
                self.__visits[i].show_visit()
                print(".....................................")

    def show_care_list(self):
        if(len(self.__cares)==0):
            print("\nNo hay registros")
        else:
            print("\n>>> Lista de Cuidados <<<")
            for i in range(0,len(self.__cares)):
                print(f"Care {i+1}\n")
                self.__cares[i].show_care()
           
    
    def tester(self):
        birth_date_alex = Date(4, 2, 2003)
        birth_date_atziri = Date(5, 6, 1996)
        birth_date_jafet = Date(30, 1, 1997)
        birth_date_alan = Date(5, 6, 1996)
        register_date_alan = Date(22, 5, 2020)
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
        visit2.add_visitor(visitor1)
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
        care1 = Care(maintenance1, "Alimentar", 1, process_date, "Comió poquito :(")
        care2 = Care(maintenance2, "Curacion", 4, process_date, "Mejora significativa en sus heridas")
        self.__cares.append(care1)
        self.__cares.append(care2)

    def modify_employee(self):
        print("\nSeleccione el tipo de empleado:\n1. Guía\n2. Veterinario\n3. Mantenimiento\n4. Administración")
        opcion = int(input("\n"))
        if(opcion==1):
            print("\nSeleccione el número")
            self.show_guides()
            opcion = int(input())
            self.__guides[opcion-1].modify_employee()
        elif(opcion==2):
            print("\nSeleccione el número")
            self.show_vets()
            opcion = int(input())
            self.__vets[opcion-1].modify_employee()
        elif(opcion==3):
            print("\nSeleccione el número")
            self.show_maintenances()
            opcion = int(input())
            self.__maintenances[opcion-1].modify_employee()
        elif(opcion==4):
            print("\nSeleccione el número")
            self.show_managements()
            opcion = int(input())
            self.__managements[opcion-1].modify_employee()
        else: print("\nOpción no válida")
    def modify_visitor(self):
        self.show_visitors()
        opcion = int(input("\nIngrese el número de visitante: "))
        self.__visitors[opcion-1].modify_visitor()