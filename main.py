from componentes import Menu,Valida
from colorama import Fore as color
from helpers import borrarPantalla,gotoxy
from crudArchivos import *
from entidadesUnemi import *
from datetime import date
import time
from estudiantes import *
import time

# Menu Principal
def main():
    salir = True
    while salir:
        borrarPantalla()
        menu = Menu("Menu Principal",["1) Mantenimiento","2) Matriculacion","3) Notas","4) Salir"],20,10)
        opc = menu.menu()
        if opc == "1":
            opc1 = ''
            while opc1 !='6':
                borrarPantalla()
                menu1 = Menu("Menu Mantenimiento",["1) Carrera","2) Materias","3) Periodos","4) Profesores","5) Estudiantes","6) Salir"],20,10)
                opc1 = menu1.menu()
                if opc1 == "1":
                    carreras()
                elif opc1 == "2":
                    materias()
                elif opc1 == "3":
                    periodos()
                elif opc1 == "4":
                    profesores()
                elif opc1 == "5":
                    estudiantes()
                elif opc1 == "6":
                    pass
                else:
                    gotoxy(40,18);print(color.RED + "Opcion no valida"), time.sleep(1.5),print(color.WHITE + ""),gotoxy(40,18);print(""*30)



        elif opc == "2":
                borrarPantalla()
                menu2 = Menu("Menu Matriculacion",["1) Matricula","2) Salir"],20,10)
                opc2 = menu2.menu()
                if opc2 == "1":
                    matriculacion()
                elif opc2 == "2":
                    pass
        elif opc == "3":
                borrarPantalla()
                menu3 = Menu("Menu Notas",["1) Notas","2) Salir"],20,10)
                opc3 = menu3.menu()
                if opc3 == "1":
                    pass

        elif opc == "4":
                print(color.GREEN + "Gracias por su visita..."), time.sleep(1.5), exit()

        else:
            print(color.RED + "Opcion no valida"), time.sleep(1.5),print(color.WHITE + ""),main()


if __name__ == "__main__":
    main()