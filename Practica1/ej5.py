import os, sys, platform

"""
Ejercicio 5. Desarrollar un script que nos muestre por consola información relevante del
identificador de proceso que el usuario inserte por consola.
Sintaxis: proceso.py
El script deberá mostrar la siguiente información del proceso: identificador UID, propietario
PID, PPID, Prioridad absoluta ”C”, Prioridad Relativa “PRI” y la Dirección en memoria o en
disco del proceso “ADDR”
"""

"""
Definition of the main method of the program
Name of method: main
Date of creation: 7/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 7/03/2021
Parameters:  None, parameters are passed 
"""
def main():
    if  platform.system() != 'Linux':
        #Check if is a UNIX machine
        print("Error, the OS is not a UNIX machine. Getting out...")
        exit(1)

    if len(sys.argv) == 1:
        #Case when parameters are not passed to the script
        print("Error, a process id is necessary")
    elif len(sys.argv) == 2:
        query = "ps -o uid,pid,ppid,c,pri,addr " + sys.argv[1]
        os.system(query)
    else:
        #Case when parameters are passed to the script
        print("Error, more parameters than necessaries")


if __name__ == "__main__":
    """
    In that case, we check that the program starts in the right function, in our
    case, main()
    """
    main()
