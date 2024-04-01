class Care:
    def _init_(self, employee_in_charge, process_realized, id, process_date, observations):
        self.employee_in_charge = employee_in_charge
        self.process_realized = process_realized
        self.id = id
        self.process_date = process_date
        self.observations = observations

    def get_employee_in_charge(self):
        return self.employee_in_charge

    def get_process_realized(self):
        return self.process_realized

    def get_id(self):
        return self.id

    def get_process_date(self):
        return self.process_date

    def get_observations(self):
        return self.observations

    def show_care(self):
        print("Empleado a cargo: " + self.get_employee_in_charge().show_employee() +
              "\nProceso: " + self.process_realized + "\n" +
              "ID Animal: " + str(self.get_id()) +
              "\nFecha Proceso: " + self.get_process_date().show_date() +
              "\nObservaciones: " + self.get_observations())
        print("......................................")