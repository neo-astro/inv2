from helpers import *
from entidadesUnemi import *
from componentes import *
from crudArchivos import *

def validar_el_id(nombre_de_entidad,arc,col,fil):
    lista,entidad=[],None
    while not lista:

        gotoxy(col,fil);id = input()
        archivo = Archivo(arc,";")
        lista = archivo.buscar(id)
        if lista:
            entidad = Carrera(lista[0],lista[1])
            gotoxy(col+5,fil);print(entidad.descripcion)
        else:
            gotoxy(col+5,fil);print(Fore.RED + f"No existe {nombre_de_entidad} con ese codigo[{id}]:")
            time.sleep(1);gotoxy(col,fil);print(" "*45)
    return entidad