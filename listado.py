import os, sys

"""
Ejercicio 1a. Desarrollar un script donde se muestren los ficheros pasados por parametro,
asi como los permisos asociados a cada uno de ellos.
Sintaxis: listado.py [Dir]
Dir sera opcional de forma que si el usuario no lo inserta el script buscara
en el directorio actual
El script debera capturar todas las posibles excepciones como pueden ser:
a. Debe permitir el paso de parámetros con una sintaxis correcta
b. Si se produce alguna excepción grave a la hora de la búsqueda en sí, el script debera
comunicarlo.
"""

#poner como variables globales los comandos, para si se cambia de SO

"""
Definicion del metodo main del programa
Nombre: main
Fecha de creacion: 18/02/2021

"""
def comprobarPermisosPorFichero():
    contadorParametros = 0
    while contadorParametros < len(sys.argv):
        comandoEjecutar = "ls -l " + sys.argv[contadorParametros]
        #print(comandoEjecutar)
        os.system(comandoEjecutar)
        contadorParametros += 1
        
        
def main():
    print(len(sys.argv))
    if len(sys.argv) == 1:
        os.system("ls -l")
    else:
        contadorParametros = 0
        while contadorParametros < len(sys.argv):
            comandoEjecutar = "ls -l " + sys.argv[contadorParametros]
            #print(comandoEjecutar)
            os.system(comandoEjecutar)
            contadorParametros += 1

    

if __name__ == "__main__":
    """
    De esta forma, se comprueba en python para que al ejecutarse el script
    vaya a la función indicada en este caso main.
    """
    main()