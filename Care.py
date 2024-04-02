class Care:
    def __init__(self, employee_in_charge, process_realized, id, process_date, observations):
        self.__employee_in_charge = employee_in_charge
        self.__process_realized = process_realized
        self.__id = id
        self.__process_date = process_date
        self.__observations = observations

    def get_employee_in_charge(self):
        return self.__employee_in_charge

    def get_process_realized(self):
        return self.__process_realized

    def get_id(self):
        return self.__id

    def get_process_date(self):
        return self.__process_date

    def get_observations(self):
        return self.__observations

    def show_care(self):
        print("Empleado a cargo: " + self.__employee_in_charge.show_employee() +
              "\nProceso: " + self.__process_realized + "\n" +
              "ID Animal: " + str(self.__id) +
              "\nFecha Proceso: " + self.__process_date.show_date() +
              "\nObservaciones: " + self.__observations)
        print("......................................")