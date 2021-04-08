import os, platform, sys,subprocess

"""
Ejercicio 6. Desarrollar un script para que busque a aquellos procesos con una prioridad relativa
superior a 11 y les decremente su prioridad en 5 unidades; posteriormente deberá mostrar que
procesos han sido susceptibles de modificación junto con la nueva prioridad asignada. 
"""

"""
Definition of the main method of the program
Nombre: main
Fecha de creacion: 8/03/2021
Miembros: Roberto Jiménez y Alberto Pérez
Última modificación: 8/03/2021
Parámetros: Parameters are passed
"""
def main():

    if  platform.system() != 'Linux':
        #Check if is a UNIX machine
        print("Error, the OS is not a UNIX machine. Getting out...")
        exit(1)
    if len(sys.argv) == 1:

        #Getting the PID list of processes
        vectorPID = subprocess.getoutput("ps -l | awk '$8 <= 0 && $4 {print $4}'")
        lista = vectorPID.split()
        vectorNI=subprocess.getoutput("ps -l| awk '$8>=0 && $4 {print $8}'")
        lista2 = vectorNI.split()
        lista2.remove("NI")

        #Updates the proccesses priority
        counter = 0
        for pid in lista:
            if int(lista2[counter]) >= 0:
                query = "sudo renice -n " + str(int(lista2[counter]) - 5) + " -p " + pid
                os.system(query)
                print("The process " + pid + " has been modified")
            else:
                print("No process with priority bigger than ten")
            counter += 1
    else:
        #Case when parameters are passed to the script
        print("Error, the parameters are not necessary")



if __name__ == "__main__":
    """
    De esta forma, se comprueba en python para que al ejecutarse el script
    vaya a la función indicada en este caso main.
    """
    main()
