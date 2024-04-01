from Guide import Guide
"""from Visitor import visitor"""

class Visit:
    def __init__(self, guide, visit_date):
        self.guide = guide
        self.visitors = []
        self.total_cost = self.cost()
        self.kids_quantity = self.kids_quantity()
        self.adults_quantity = self.adults_quantity()
        self.visit_date = visit_date

    def get_total_cost(self):
        return self.total_cost

    def get_kids_quantity(self):
        return self.kids_quantity

    def get_adults_quantity(self):
        return self.adults_quantity

    def get_guide(self):
        return self.guide

    def get_visit_date(self):
        return self.visit_date

    def add_visitor(self, visitor):
        if visitor in self.visitors:
            print("Este visitante ya fue registrado")
        else:
            visitor.set_total_visits(visitor.get_total_visits() + 1)
            self.visitors.append(visitor)

    def delete_visitor(self, visitor):
        self.visitors.remove(visitor)

    # Calcula el costo total de la visita
    def cost(self):
        cost = 0
        for visitor in self.visitors:
            cost += visitor.calculate_ticket_cost()
        return cost

    # Calcula el total de niños
    def kids_quantity(self):
        quantity = 0
        for visitor in self.visitors:
            if not visitor.is_an_adult():
                quantity += 1
        return quantity

    # Calcula el total de adultos
    def adults_quantity(self):
        quantity = 0
        for visitor in self.visitors:
            if visitor.is_an_adult():
                quantity += 1
        return quantity