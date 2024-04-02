from Zoo import Zoo
class MainMenu:
    password = "uwu"
    print(">>> Bienvenido al zoológico <<<")
    user_input = input("\nIngrese contraseña: ")

    if (user_input != password):
        print("\nContraseña inválida, intente más tarde")
    else:
        zoo = Zoo()
        flag = True
        zoo.tester()
        while flag:
            print("\n>>> Bienvenido al sistema <<<")
            print("\n¿Qué acción desea realizar?\n"
                  "\n1) Registrar empleado\n"
                  "2) Registrar visitante\n"
                  "3) Registrar visita\n"
                  "4) Registrar animal\n"
                  "5) Registrar mantenimiento\n"
                  "6) Modificar empleado\n"
                  "7) Modificar registro de animal\n"
                  "8) Modificar visitante\n"
                  "9) Eliminar empleado\n"
                  "10) Eliminar Animal\n"
                  "11) Eliminar visitante\n"
                  "12) Consultar empleados\n"
                  "13) Consultar animales\n"
                  "14) Consultar visitantes\n"
                  "15) Consultar visitas\n"
                  "16) Consultar mantenimientos\n"
                  "0) Salir")
            option = int(input("\nIngrese una opcion: "))
            if(option == 1):
                zoo.add_employee()
            elif(option == 2):
                zoo.add_visitors()
            elif(option == 3):
                zoo.add_visit()
            elif(option == 4):
                zoo.add_animal()
            elif(option == 5):
                zoo.add_care()
            elif(option == 6):
                zoo.modify_employee()
            elif(option == 7):
                zoo.modify_animal_register()
            elif(option == 8):
                zoo.modify_visitor()
            elif(option == 9):
                zoo.delete_employee()
            elif(option == 10):
                zoo.delete_animal()
            elif(option == 11):
                zoo.delete_visitor()
            elif(option == 12):
                zoo.show_employees()
            elif(option == 13):
                zoo.show_animals()
            elif(option == 14):
                zoo.show_visitors()
            elif(option == 15):
                zoo.show_visits()
            elif(option == 16):
                zoo.show_care_list()
            elif(option == 0):
                flag = False
                print("\nGracias por usar el zoologico")

    