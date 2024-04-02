from Date import Date
class Person:
    def __init__(self,name,last_name,birth_date,curp):
        self.__name = name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__curp = curp
    
    #Métodos de la clase
    def set_name(self,name):
        self.__name = name
    def set_last_name(self,last_name):
        self.__last_name = last_name
    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date
    def get_name(self):
        return self.__name
    def get_birth_date(self):
        return self.__birth_date
    def set_curp(self,curp):
        self.__curp = curp
    #Método para mostrar la información
    def show_info(self):
        #Se llama al método show_date de la clase Date para el atributo birth_date
        return f"Nombre completo: {self.__name} {self.__last_name}\n   Fecha de nacimiento: {self.__birth_date.show_date()}\n   CURP: {self.__curp}"