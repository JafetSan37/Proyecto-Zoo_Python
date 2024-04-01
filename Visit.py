from Guide import Guide
from Visitor import Visitor

class Visit:
    def __init__(self, guide, visit_date):
        self.__guide = guide
        self.__visitors = []
        self.__total_cost = self.__cost()
        self.__kids_quanty = self.__kids_quanty()
        self.__adults_quanty = self.__adults_quanty()
        self.__visit_date = visit_date

    def get_total_cost(self):
        return self.__total_cost

    def get_kids_quantity(self):
        return self.__kids_quanty

    def get_adults_quantity(self):
        return self.__adults_quanty

    def get_guide(self):
        return self.__guide

    def get_visit_date(self):
        return self.__visit_date

    def add_visitor(self, visitor):
        if visitor in self.__visitors:
            print("Este visitante ya fue registrado")
        else:
            visitor.set_total_visits(visitor.get_total_visits() + 1)
            self.__visitors.append(visitor)

    def delete_visitor(self, visitor):
        self.__visitors.remove(visitor)

    # Calcula el costo total de la visita
    def __cost(self):
        cost = 0
        for visitor in self.__visitors:
            cost += visitor.calculate_ticket_cost()
        return cost

    # Calcula el total de niños
    def __kids_quanty(self):
        quantity = 0
<<<<<<< HEAD
        for visitor in self.visitors():
=======
        for visitor in self.__visitors:
>>>>>>> 93b3952f2e2a27f8a5219e62948171862f82e5c2
            if not visitor.is_an_adult():
                quantity += 1
        return quantity

    # Calcula el total de adultos
    def __adults_quanty(self):
        quantity = 0
        for visitor in self.__visitors:
            if visitor.is_an_adult():
                quantity += 1
        return quantity