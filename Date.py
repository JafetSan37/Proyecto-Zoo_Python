class Date:
    
    def __init__(self,day_of_month,month,year):
        self.day_of_month = day_of_month
        self.month = month
        self.year = year
    
    #Getters y Setters
    def get_day_of_month(self):
        return self.day_of_month
    def set_dat_of_month(self,day_of_month):
        self.day_of_month = int(day_of_month)
    def get_month(self):
        return self.month
    def set_month(self,month):
        self.month = int(month)
    def get_year(self):
        return self.year
    def set_year(self,year):
        self.year = int(year)
    
    #Modifica la fecha actual y valida datos
    def modify_date(self):
        print("\nIngrese la fecha de Nacimiento")
        new_year = int(input("\nAño: "))
        if(new_year>1900 and new_year<2024):
            self.year = new_year
        elif(new_year>=2024):
            print("Año no válido")
        new_month = int(input("\nMes: "))
        if(new_month<13 and new_month>0):
            self.month = new_month
        elif(new_month>=13 or new_month<=0):
            print("Mes no válido")
        new_day_of_month = int(input("\nDía: "))
        if(new_day_of_month>0 and new_day_of_month<32):
            self.day_of_month = new_day_of_month
        elif(new_day_of_month>=32 or new_day_of_month<=0):
            print("Día no válido")
    #Método para mostrar la fecha como cadena
    def show_date(self):
        return f"{self.day_of_month}/{self.month}/{self.year}"