from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArchivos import *
from entidadesUnemi import *
from datetime import date
import time
from colorama import Fore
from validar_id import *
#----------------Procesos de las Opciones del Menu Mantenimiento------------
def carreras():
    validar_carreras = Valida
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE CARRERAS")
    gotoxy(15,3);print("Generar carrera, codigo automatico ")
    gotoxy(15,4);print("Descripcion Carrera: ")
    gotoxy(36,4);descarrera = validar_carreras.no_vacio(None, "Completa el campo!,solo letras",36,4)
    archivo_carreras = Archivo("./archivos/carrera.txt",";")
    carrera = archivo_carreras.leer()
    if carrera : idSig = int(carrera[-1][0])+1
    else: idSig=1
    entidad_carrera = Carrera(idSig,descarrera)
    datos = entidad_carrera.getCarrera()
    datos = ';'.join(datos)
    archivo_carreras.escribir([datos],"a")
    gotoxy(15,7);print(Fore.GREEN + f"Se agrego la carrera {descarrera}")
    time.sleep(1.5)

#----------------COPIA DE PERIODO-------------------------------------
def materias():
    validar_materia = Valida
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE MATERIAS")
    #este codigo es con el que busco en archivo.buscar
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion Carrera: ")
    gotoxy(25,4);codigo = validar_materia.solo_numeros(None, "Debes escribir solo numeros!",25,4)
    gotoxy(36,5);descarrera = validar_materia.no_vacio(None, "Completa el campo!,solo letras",36,5)
    archiCarrera = Archivo("./archivos/materias.txt",";")
    #carreras = archiCarrera.leer()
    #if carreras : idSig = int(carreras[-1][0])+1
    #else: idSig=1
    #Le mando el codigo ingresado--------------------------------------
    carrera = Carrera(int(codigo),descarrera)
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
    gotoxy(45,6);descarrera = validar_periodo.no_vacio(None, "Completa el campo!,solo letras",45,6)
    archivo_periodos = Archivo("./archivos/periodos.txt")
    periodo = str(año) + str(mes)
    ent_periodo = Periodo(periodo,descarrera)
    datos = ent_periodo.getPeriodo()
    datos = ';'.join(datos)
    archivo_periodos.escribir([datos],"a")
    gotoxy(15,8); print(Fore.GREEN + "Se agrego el periodo")
    time.sleep(1.5)



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
   gotoxy(25,5);cedula = validar_pro.solo_numeros("Solo numeros,no se admite 0 como primer valor",25,5)
   gotoxy(25,6);titulo_docente = validar_pro.no_vacio("Completa el campo!,solo letras",25,6)
   telefono=validar_pro.solo_numeros("Solo numeros,no se admite 0 como primer valor",25,7)

   entidad_carrera = validar_id_ca_pe_ma(Carrera,'Carrera',"./archivos/carrera.txt",27,8)
   gotoxy(15,10);print(Fore.GREEN + "Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()

   if grabar == "s":
        archiProfesor = Archivo("./archivos/profesor.txt")
        lisProfesores = archiProfesor.leer()
        if lisProfesores : idSig = int(lisProfesores[-1][0])+1
        else: idSig=1
        entProfesor = Profesor(idSig,nombre,cedula,entidad_carrera,titulo_docente,telefono)
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
    gotoxy(27,6);direccion = validar_estudiantes.solo_letras("Completa el campo!,solo letras",27,6)
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
#------------------------------------------------------------------------------
def matriculacion():
    borrarPantalla()
    validar_matriculacion = Valida()
    gotoxy(20,2);print("INGRESO DE MATRICULACION")
    gotoxy(15,4);print("Estudiante ID:[]")
    gotoxy(15,5);print("Periodo ID:[]")
    gotoxy(15,6);print("Carrera ID:[]")
    gotoxy(15,7);print("Valor de la inscripcion: ")
    #inputs

    entidad_estudiante = validar_id_estudiante(Estudiante,'estudiante',"./archivos/estudiantes.txt",30,4)
    entidad_periodo = validar_id_ca_pe_ma(Periodo,"periodo","./archivos/periodos.txt",27,5)
    entidad_carrera = validar_id_ca_pe_ma(Carrera,"carrera","./archivos/carrera.txt",27,6)
    gotoxy(40,7);valor_de_matricula = validar_matriculacion.solo_numeros("Error: Solo numeros",40,7)

    gotoxy(15,10);print(Fore.GREEN + "Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,10);grabar = input().lower()

    if grabar == "s":
            archivo_matriculacion = Archivo("./archivos/matriculacion.txt")
            lis_matriculacion = archivo_matriculacion.leer()
            if lis_matriculacion : idSig = int(lis_matriculacion[-1][0])+1
            else: idSig = 1
            entidad_matriculacion = Matricula(idSig,entidad_estudiante,entidad_carrera,entidad_periodo,valor_de_matricula)
            datos = entidad_matriculacion.getMatricula()#retorna una lista
            datos = ";".join(datos)#convierte a cadena
            archivo_matriculacion.escribir([datos],"a+")
            gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
            gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")

#----------------------------------------------------------------
def notas():
    borrarPantalla()
    validar_notas = Valida()
    gotoxy(20,2);print("INGRESO DE NOTAS")
    gotoxy(15,4);print("Periodo ID:[]")
    gotoxy(15,5);print("Estudiante ID:[]")
    gotoxy(15,6);print("Materia ID:[]")
    gotoxy(15,7);print("Profesor ID:[]")
    gotoxy(15,8);print("Nota 1:")
    gotoxy(15,9);print("Nota 2:")
    #inputs
    #estas var entidades almacenan el codigo de dicha entidad
    entidad_periodo = validar_id_ca_pe_ma(Periodo,"periodo","./archivos/periodos.txt",27,4)
    entidad_estudiante = validar_id_estudiante(Estudiante,'estudiante',"./archivos/estudiantes.txt",30,5)
    entidad_materia = validar_id_ca_pe_ma(Carrera,"materia","./archivos/materias.txt",27,6)
    entidad_profesor = validar_id_ca_pe_ma(Carrera,"profesor","./archivos/profesor.txt",27,7)
    gotoxy(22,7);nota1 = validar_notas.solo_numeros("Error: Solo numeros",40,8)
    gotoxy(22,8);nota2 = validar_notas.solo_numeros("Error: Solo numeros",40,9)

    gotoxy(15,10);print(Fore.GREEN + "Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,10);grabar = input().lower()

    if grabar == "s":
            archivo_notas= Archivo("./archivos/notas.txt")
            lis_notas = archivo_notas.leer()
            if lis_notas: idSig = int(lis_notas[-1][0])+1
            else: idSig = 1
            entidad_notas = Matricula(idSig,entidad_periodo,entidad_estudiante,entidad_materia,entidad_profesor,nota1,nota2)
            datos = entidad_notas.getMatricula()#retorna una lista
            datos = ";".join(datos)#convierte a cadena
            archivo_notas.escribir([datos],"a+")
            gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
            gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")