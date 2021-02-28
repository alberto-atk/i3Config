import os, platform, sys,subprocess
"""
Definición del metodo principal del programa
Nombre: main
Fecha de creacion: 28/02/2021
Miembros: Roberto Jiménez y Alberto Pérez
Última modificación: 28/02/2021
Parámetros: Ninguno, los parámetros son los que se pasan como argumento a la
llamada
"""
def main():

    if  platform.system() != 'Linux':
        #Check if is a UNIX machine
        print("Error, the OS is not a UNIX machine. Getting out...")
        exit(1)
    if len(sys.argv) == 1:

        vectorPID = subprocess.getoutput("ps -l | awk '$8 <= 0 && $4 {print $4}'")
        #print(vectorPID)

        lista = vectorPID.split()
        vectorNI=subprocess.getoutput("ps -l| awk '$8>=0 && $4 {print $8}'")
        lista2 = vectorNI.split()
        lista2.remove("NI")
        print(lista2)

        counter = 0
        for pid in lista:
            if int(lista2[counter]) >= 0:

                query = "sudo renice -n " + str(int(lista2[counter]) - 5) + " -p " + pid
                print(query)
                os.system(query)
                print("El proceso " + pid + " se ha modificado")
            else:
                print("No hay valores con prioridad mayor de 10")
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
