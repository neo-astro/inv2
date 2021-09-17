from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArchivos import *
from entidadesUnemi import *
from datetime import date
import time
from colorama import Fore

#----------------Procesos de las Opciones del Menu Mantenimiento------------
def carreras():
    validar = Valida
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE CARRERAS")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion Carrera: ")
    gotoxy(25,4);validar.solo_numeros(None, "Debes escribir solo numeros!",25,4)
    gotoxy(36,5);descarrera = validar.no_vacio(None, "Completa el campo!,solo letras",36,5)
    archiCarrera = Archivo("./archivos/carrera.txt",";")
    carreras = archiCarrera.leer()
    if carreras : idSig = int(carreras[-1][0])+1
    else: idSig=1
    carrera = Carrera(idSig,descarrera)
    datos = carrera.getCarrera()
    datos = ';'.join(datos)
    archiCarrera.escribir([datos],"a")
    gotoxy(15,7);print(Fore.GREEN + f"Se agrego la carrera {descarrera}")
    time.sleep(1.5)

#----------------COPIA DE PERIODO-------------------------------------
def materias():
    validar_materia = Valida
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE MATERIAS")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion Carrera: ")
    gotoxy(25,4);validar_materia.solo_numeros(None, "Debes escribir solo numeros!",25,4)
    gotoxy(36,5);descarrera = validar_materia.no_vacio(None, "Completa el campo!,solo letras",36,5)
    archiCarrera = Archivo("./archivos/carrera.txt",";")
    carreras = archiCarrera.leer()
    if carreras : idSig = int(carreras[-1][0])+1
    else: idSig=1
    carrera = Carrera(idSig,descarrera)
    datos = carrera.getCarrera()
    datos = ';'.join(datos)
    archiCarrera.escribir([datos],"a")
    gotoxy(15,6);print(Fore.GREEN + f"Se agrego la carrera {descarrera}")
    time.sleep(1.5)
#-----------------------------------------------------
def periodos():
    validar_periodo = Valida
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE PERIODOS")
    gotoxy(15,4);print("Año del periodo: ")
    gotoxy(15,5);print("Mes del periodo: ")
    gotoxy(15,6);print("Descripcion del periodo: ")
    
    #inputs

    gotoxy(36,4);año = validar_periodo.solo_numeros(None, "Debes escribir solo numeros!",36,4)
    gotoxy(36,5);mes = validar_periodo.solo_numeros(None, "Debes escribir solo numeros!",36,5)
    gotoxy(52,6);descarrera = validar_periodo.no_vacio(None, "Completa el campo!,solo letras",52,6)
    archivo_periodos = Archivo("./archivos/periodos.txt")
    periodo = str(año) + str(mes)
    ent_periodo = Periodo(periodo,descarrera)
    datos = ent_periodo.getPeriodo()
    datos = ';'.join(datos)
    archivo_periodos.escribir([datos],"a")
    gotoxy(15,8); print(Fore.GREEN + "Se agrego el periodo")
    time.sleep(1.5)
    #periodo = Periodo(año,mes,descarrera)



#-----------------------------------------------------

def profesores():

   borrarPantalla()
   validar_pro = Valida()
   gotoxy(20,2);print("INGRESO DE PROFESORES")
   gotoxy(15,4);print("Nombre : ")
   gotoxy(15,5);print("Cedula : ")
   gotoxy(15,6);print("Titulo : ")
   gotoxy(15,7);print("Telefono : ")
   gotoxy(15,8);print("Carrera ID[    ]: ")
   gotoxy(25,4);nombre = validar_pro.no_vacio("Completa el campo!. Solo letras",25,4)
   gotoxy(25,5);cedula = validar_pro.solo_numeros("Error: Solo numeros",25,5)
   gotoxy(25,6);titulo_docente = validar_pro.no_vacio("Completa el campo!,solo letras",25,6)
   telefono=validar_pro.solo_numeros("Error: Solo numeros",25,7)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,8);id = input()
      archiCarrera = Archivo("./archivos/carrera.txt",";")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1])
          gotoxy(33,8);print(entCarrera.descripcion)
      else:
         gotoxy(33,8);print(Fore.RED + "No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)

   gotoxy(15,10);print(Fore.GREEN + "Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()

   if grabar == "s":
        archiProfesor = Archivo("./archivos/profesor.txt")
        lisProfesores = archiProfesor.leer()
        if lisProfesores : idSig = int(lisProfesores[-1][0])+1
        else: idSig=1
        entProfesor = Profesor(idSig,nombre,cedula,entCarrera,titulo_docente,telefono)
        datos = entProfesor.getProfesor()
        datos = ';'.join(datos)
        archiProfesor.escribir([datos],"a")
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
        gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")     

def estudiantes():
    borrarPantalla()
    validar_estudiantes = Valida()
    gotoxy(20,2);print("INGRESO DE ESTUDIANTES")
    gotoxy(15,4);print("Nombre : ")
    gotoxy(15,5);print("Cedula : ")
    gotoxy(15,6);print("Direccion : ")
    gotoxy(15,7);print("Telefono : ")
    #inputs

    gotoxy(25,4);nombre = validar_estudiantes.no_vacio("Completa el campo!. Solo letras",25,4)
    gotoxy(25,5);cedula = validar_estudiantes.solo_numeros("Error: Solo numeros",25,5)
    gotoxy(25,6);direccion = validar_estudiantes.no_vacio("Completa el campo!,solo letras",25,6)
    gotoxy(25,7);telefono = validar_estudiantes.solo_numeros("Error: Solo numeros",25,7)


    gotoxy(15,8);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,8);grabar = input().lower()

    lis_estudiantes,entidad_estudiantes = [],None

    if grabar == "s":
            archivo_estudiantes = Archivo("./archivos/estudiantes.txt")
            lis_estudiantes = archivo_estudiantes.leer()
            if lis_estudiantes : idSig = int(lis_estudiantes[-1][0])+1
            else: idSig=1
            entidad_estudiantes = Estudiante(idSig,nombre,cedula,telefono,direccion)
            datos = entidad_estudiantes.getEstudiante()
            datos = ';'.join(datos)
            archivo_estudiantes.escribir([datos],"a")
            gotoxy(15,11);input(Fore.GREEN + "Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(15,11);input(Fore.RED + "Registro No fue Grabado\n presione una tecla para continuar...")

