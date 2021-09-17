from helpers import *
from entidadesUnemi import *
from componentes import *
from crudArchivos import *

def validar_el_id(nombre_de_entidad,lis_var,arc,col,fil):
    while not lis_var:

        gotoxy(col,fil);id = input()
        archivo = Archivo(arc,";")
        lis_var = archivo.buscar(id)
        if lis_var:
            entidad = Carrera(entidad[0],entidad[1])
            gotoxy(col+5,fil + 20);print(entidad.descripcion)
        else:
            gotoxy(col+5,fil + 20);print(Fore.RED + f"No existe {nombre_de_entidad} con ese codigo[{id}]:")
            time.sleep(1);gotoxy(col,fil);print(" "*40)