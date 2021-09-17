from helpers import borrarPantalla, gotoxy
import time
from colorama import Fore

class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil

    def menu(self):
        gotoxy(self.col,self.fil);print(Fore.GREEN + self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones))) 
        return opc

class Valida:
    #input vacio
    def no_vacio(self,mensajeError,col,fil):
        while True:
            gotoxy(col,fil)
            valor = input()
            valor = valor.split(" ")
            lista_comprobar = list(x.isalpha() for x in valor)
            try:
                if all(lista_comprobar):
                    valor = " ".join(valor)
                    break
                elif len(valor) == 0 :
                    raise ValueError
                else : raise ValueError

            except ValueError:
                gotoxy(col,fil);print(Fore.RED + mensajeError), print(Fore.WHITE + "")
                time.sleep(1.5)
                gotoxy(col,fil);print(" "*40)
        return valor


        # while True:
        #     gotoxy(col,fil)
        #     valor = input()

        #     try:
        #         valor = valor.split(" ")
        #         for ele in valor:
        #             assert ele.isalpha()
        #         valor =  " ".join(valor)


        #     except AssertionError or ValueError:
        #         gotoxy(col,fil);print(Fore.RED + mensajeError), print(Fore.WHITE + "")
        #         time.sleep(1.5)
        #         gotoxy(col,fil);print(" "*30)
                
        #     return valor



    def solo_numeros(self, mensajeError,col,fil):
        while True:
            gotoxy(col,fil)
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(Fore.RED + mensajeError),print(Fore.WHITE + "")
                time.sleep(1.5)
                gotoxy(col,fil);print(" "*30)
                
        return valor

    def solo_letras(self,mensaje,mensajeError):
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print("          ------><  | {} ".format(mensajeError))
        return valor

    def solo_decimales(self,mensaje,mensajeError):
        while True:
            valor = str(input("          ------>   | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor
    
    def cedula():
        pass
    
