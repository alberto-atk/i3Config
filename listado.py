import os, sys, subprocess
import platform
import os.path

"""
Ejercicio 1a. Desarrollar un script donde se muestren los ficheros pasados por
parametro, asi como los permisos asociados a cada uno de ellos.
Sintaxis: listado.py [Dir]
Dir sera opcional de forma que si el usuario no lo inserta el script buscara
en el directorio actual
El script debera capturar todas las posibles excepciones como pueden ser:
a. Debe permitir el paso de parámetros con una sintaxis correcta
b. Si se produce alguna excepción grave a la hora de la búsqueda en sí, el
script debera comunicarlo.
"""

"""
Usage: Defining a method which obtains permissions of the files passed by
parameter
Name of method: checkFilePermissions
Date of creation: 18/02/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 20/02/2021
Parameters:
    Entry:  None
    Out: None
Documentation:  https://docs.python.org/3/library/subprocess.html
"""

def checkFilePermissions():

    contadorParametros = 1
    while contadorParametros < len(sys.argv):
        try:
            if (not os.path.isdir(sys.argv[contadorParametros])  and
               not os.path.isfile(sys.argv[contadorParametros])):
               #Comprobación de si el path es erróneo (siendo este fichero o directorio)
               print("Error in path: " + sys.argv[contadorParametros])
            else:
               subprocess.run(['ls', '-l', sys.argv[contadorParametros]], check = True)
        except subprocess.CalledProcessError as err:
            print('Error in processor call:', err)
        except Exception as e:
            print('Error detected: ', e)
        contadorParametros += 1


"""
Usage: Defining main method of program
Name of method: main
Date of creation: 18/02/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 20/02/2021
Parameters:
    Entry:  None

Documentation:  https://docs.python.org/3/library/subprocess.html
"""
def main():

    if  platform.system() != 'Linux':
        #Check OS System

        print("Error, the OS is not a UNIX machine. Getting out...")
        exit(1)
    if len(sys.argv) == 1:
        """
        Este caso se ejecuta cuando no se pasa ningún parámetro al script
        y se muestran los permisos de los ficheros del directorio actual
        """
        os.system("ls -l")
    else:
        checkFilePermissions()



if __name__ == "__main__":
    """
    De esta forma, se comprueba en python para que al ejecutarse el script
    vaya a la función indicada en este caso main.
    """
    main()
