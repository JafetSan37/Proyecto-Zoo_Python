from Person import Person
from Date import Date
class Visitor(Person):
    
    def __init__(self, name, last_name, birth_date, curp,register_date):
        super().__init__(name, last_name, birth_date, curp)
        self.__register_date = register_date
        self.__total_visits = 0
        
    #Métodos de la clase
    def get_total_visits(self):
        return self.__total_visits
    def get_register_date(self):
        return self.__register_date
    def set_total_visits(self,total_visits):
        self.__total_visits = total_visits
    def add_visit(self):
        self.__total_visits+=1
        
    def show_visitor(self):
        return self.show_info() + f"Total visits: {self.__total_visits} Register date: {self.__register_date.show_date()}"
    def modify_visitor(self):
        print("\n¿Qué aspecto desea modificar?\n1) Nombre\n2) Apellido\n3) Fecha de Nacimiento\n4) CURP")
        selection = int(input("\n"))
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
        else:
            print("\nOpción no válida")
        print(f"\nInformación guardada: {self.show_visitor()}")
    def calculate_ticket_cost(self):
        if(self.is_an_adult()):
            if(self.__total_visits%5==0):
                return 100*.08
            else: return 100
        else:
            if(self.__total_visits%5==0):
                return 50*0.8
            else: return 50
    def is_an_adult(self):
        actual_year = 2024
        person_year = self.get_birth_date().get_year()
        visitors_age = actual_year - person_year
        return (visitors_age >= 18)