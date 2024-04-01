from Date import Date
class Person:
    def __init__(self,name,last_name,birth_date,curp):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.curp = curp
    
    #Métodos de la clase
    def set_name(self,name):
        self.name = name
    def set_last_name(self,last_name):
        self.last_name = last_name
    def set_birth_date(self, birth_date):
        self.birth_date = birth_date
    def get_name(self):
        return self.name
    def get_birth_date(self):
        return self.birth_date
    def set_curp(self,curp):
        self.curp = curp
    #Método para mostrar la información
    def show_info(self):
        #Se llama al método show_date de la clase Date para el atributo birth_date
        return f"Nombre completo: {self.name}, Fecha de nacimiento: {self.birth_date.show_date()}, CURP: {self.curp}"