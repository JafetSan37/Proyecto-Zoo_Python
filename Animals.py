from Date import Date

from Date import Date

class Animals:
    __cant_animal = 0

    def __init__(self, type, arrival_date, diet, birth_date, weight, feeding_frequency, is_vaccinated):
        Animals.__cant_animal += 1
        self.__id = self.__cant_animal
        self.__type = type
        self.__arrival_date = arrival_date
        self.__diet = diet
        self.__birth_date = birth_date
        self.__weight = weight
        self.__feeding_frequency = feeding_frequency
        self.__is_vaccinated = is_vaccinated
        self.__list_diseases = []


    def add_disease(self, new_disease):
        self.__list_diseases.append(new_disease)

    def get_id(self):
        return self.__id

    def get_type(self):
        return self.__type

    def get_arrival_date(self):
        return self.__arrival_date

    def get_list_diseases(self):
        return self.__list_diseases

    def get_diet(self):
        return self.__diet

    def get_birth_date(self):
        return self.__birth_date

    def get_weight(self):
        return self.__weight

    def get_feeding_frequency(self):
        return self.__feeding_frequency

    def is_vaccinated(self):
        return self.__is_vaccinated

    def set_diet(self, diet):
        self.__diet = diet

    def set_weight(self, weight):
        self.__weight = weight

    def set_feeding_frequency(self, feeding_frequency):
        self.__dietfeeding_frequency = feeding_frequency

    def set_vaccinated(self, vaccinated):
        self.__is_vaccinated = vaccinated

    def show_animal(self):
        aDate = f"{self.__arrival_date.get_day_of_month()}/{self.__arrival_date.get_month()}/{self.__arrival_date.get_year()}"
        bDate = f"{self.__birth_date.get_day_of_month()}/{self.__birth_date.get_month()}/{self.__birth_date.get_year()}"
        return f"ID: {self.__id}\n   type: {self.__type}\n   Fecha de llegada: {aDate}\n   Diet: {self.__diet}\n   Fecha nacimiento: {bDate}\n   Peso: {self.__weight}\n   Frecuencia de alimentacion: {self.__feeding_frequency}\n   Esta vacunado: {self.__is_vaccinated}\n"