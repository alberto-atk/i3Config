import os, sys, subprocess
import platform
import os.path, stat

from os import listdir


"""
Ejercicio 2a. Modificar el anterior script para que se le pida al usuario por
consola el directorio donde tendrá que buscar y deberá mostrar todos
los ficheros del directorio, así como de los posibles subdirectorios.
Sintaxis: listado.py
El script deberá capturar todas las posibles excepciones como pueden ser:

a. Si el directorio que el usuario introduce no existe o no es un directorio,
deberá dar un error.
b. Si el usuario que lo invoca no tiene permisos de lectura del directorio,
el script deberá gestionar dicha excepción.
"""

#/home/alumno/Escritorio/PracticasSI2
"""
Usage: Defining a method that lists the files in a directory
Name of method: recursivelyList
Date of creation: 20/02/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 20/02/2021
Parameters:
    Entry:
     path: Directory from which the list of files or directories
           that exist is obtained
    Out: List with files and directories

"""
def listDirectory(path):
    if os.access(path, os.R_OK):
        return os.listdir(path)
    return ["Error, directory has not reading permissions"]


"""
Usage: Definition of a recursive method that goes through all the directories and
subdirectories based on the directory passed by parameter
Name of method: recursivelyList
Date of creation: 20/02/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 20/02/2021
Parameters:
    Entry:
     directory: Directory which is going to be listed
    Out: None

"""
def recursivelyList(directory):
    auxDirectories = []
    files = listDirectory(directory)
    print("\x1b[1;34m" + directory + ":")
    for file in files:
        path = directory + "/" + file
        if(os.path.isdir(path)):
            print("\x1b[1;36m" + file + " ", end="")
            auxDirectories.append(path)
        else:
            print("\x1b[1;37m" + file + " ", end="")

    print("\x1b[1;37m \n")
    #
    for directory in auxDirectories:
        recursivelyList(directory)


"""
Definition of the main method of the program
Name of method: main
Date of creation: 20/02/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 20/02/2021
Parameters:  None, parameters are read by console
"""
def main():

    if  platform.system() != 'Linux':
        #Check if is a UNIX machine
        print("Error, the OS is not a UNIX machine. Getting out...")
        exit(1)
    if len(sys.argv) == 1:
        #We chek that no parameters are passed
        path = input('Write the path of the directory ')

        if os.path.isdir(path):
            print("")
            recursivelyList(path)
            #if os.chmod(path, )
            #subprocess.run(['ls', '-l', '-R', path])

    else:
        #Case when parameters are passed to the script
        print("Error, the parameters are not necessary")



if __name__ == "__main__":
    """
    In that case, we check that the program starts in the right function, in our
    case, main()
    """
    main()
