from helpers import *
from entidadesUnemi import *
from componentes import *
#import emoji 
from crudArchivos import *

def validar_id_ca_pe_ma(nom_enti,nombre_de_entidad,arc,col,fil):
    lista,entidad=[],None
    while not lista:
        validar = Valida
        gotoxy(col,fil);valor = validar.solo_numeros(None,"Solo numeros,no se admite 0 como primer valor",col,fil)
        valor = str(valor)
        archivo = Archivo(arc,";")
        #lista me sirve para saber si existen datos, si es asi busca el valor y lo muestra
        lista = archivo.buscar(valor)
        if lista:
            entidad = nom_enti(lista[0],lista[1])
            gotoxy(col+7,fil);print(Fore.GREEN + lista[1])
        else:
            gotoxy(col+5,fil);print(Fore.RED + f"No existe {nombre_de_entidad} con ese codigo[{valor}]:")
            time.sleep(1.5);gotoxy(col,fil);print(" "*50)

    return entidad

def validar_id_estudiante(nom_enti,nombre_de_entidad,arc,col,fil):
    lista,entidad=[],None
    while not lista:
        validar = Valida
        gotoxy(col,fil);valor = validar.solo_numeros(None,"Solo numeros,no se admite 0 como primer valor",col,fil)
        valor = str(valor)
        archivo = Archivo(arc,";")
        #lista me sirve para saber si existen datos, si es asi busca el valor y lo muestra
        lista = archivo.buscar(valor)
        if lista:
            entidad = nom_enti(lista[0],lista[1],lista[2],lista[3],lista[4])
            gotoxy(col+5,fil);print(Fore.GREEN + lista[1])
        else:
            gotoxy(col+5,fil);print(Fore.RED + f"No existe {nombre_de_entidad} con ese codigo[{valor}]:")
            time.sleep(1.5);gotoxy(col,fil);print(" "*60)

    return entidad

def validar_id_profesor(nom_enti,nombre_de_entidad,arc,col,fil):
    lista,entidad=[],None
    while not lista:
        validar = Valida
        gotoxy(col,fil);valor = validar.solo_numeros(None,"Solo numeros,no se admite 0 como primer valor",col,fil)
        valor = str(valor)
        archivo = Archivo(arc,";")
        #lista me sirve para saber si existen datos, si es asi busca el valor y lo muestra
        lista = archivo.buscar(valor)
        if lista:
            entidad = nom_enti(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5])
            gotoxy(col+5,fil);print(Fore.GREEN + lista[1])
        else:
            gotoxy(col+5,fil);print(Fore.RED + f"No existe {nombre_de_entidad} con ese codigo[{valor}]:")
            time.sleep(1.5);gotoxy(col,fil);print(" "*60)

    return entidad


