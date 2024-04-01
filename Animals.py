from Date import Date

class Animals:
    cant_animal = 0

    def _init_(self, type, arrival_date, diet, birth_date, weight, feeding_frequency, is_vaccinated):
        Animals.cant_animal += 1
        self.id = Animals.cant_animal
        self.type = type
        self.arrival_date = arrival_date
        self.diet = diet
        self.birth_date = birth_date
        self.weight = weight
        self.feeding_frequency = feeding_frequency
        self.is_vaccinated = is_vaccinated
        self.list_diseases = []

    def add_disease(self, new_disease):
        self.list_diseases.append(new_disease)

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_arrival_date(self):
        return self.arrival_date

    def get_list_diseases(self):
        return self.list_diseases

    def get_diet(self):
        return self.diet

    def get_birth_date(self):
        return self.birth_date

    def get_weight(self):
        return self.weight

    def get_feeding_frequency(self):
        return self.feeding_frequency

    def is_vaccinated(self):
        return self.is_vaccinated

    def set_diet(self, diet):
        self.diet = diet

    def set_weight(self, weight):
        self.weight = weight

    def set_feeding_frequency(self, feeding_frequency):
        self.feeding_frequency = feeding_frequency

    def set_vaccinated(self, vaccinated):
        self.is_vaccinated = vaccinated

    def show_animal(self):
        aDate = f"{self.arrival_date.day}/{self.arrival_date.month}/{self.arrival_date.year}"
        bDate = f"{self.birth_date.day}/{self.birth_date.month}/{self.birth_date.year}"
        return f"ID: {self.id} || type: {self.type} || Fecha de llegada: {aDate} || diet: {self.diet} || Fecha nacimiento: {bDate} || Peso: {self.weight} || Frecuencia de alimentacion: {self.feeding_frequency} || Esta vacunado: {self.is_vaccinated}"