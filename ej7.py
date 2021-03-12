import os, platform, sys,subprocess, copy, filecmp, time
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
    # comando de llamada prueba
    #python3 ej7.py /home/alumno/Escritorio/PractiasAS2/Practica1/practicasAS2/p1 /home/alumno/Escritorio/PractiasAS2/Practica1/practicasAS2/p2

    if  platform.system() != 'Linux':
        #Check if is a UNIX machineputt
        print("Error, the OS is not a UNIX machine. Getting out...")
        exit(1)
    if len(sys.argv) == 1:
        #Case when parameters are not passed to the script
        directory = input("Your current directory is: " + os.getcwd() + " please insert another"+
                " directory to compare: " + '\n' )
        if(os.path.isdir(directory)):
            eliminarFicherosDuplicados(os.getcwd(), directory)
        else:
            print("Error, the passed directory does not exist")
    elif  len(sys.argv) == 2:
        #Case when a parameter is passed to the script
        directory = input("Directory passed:" + sys.argv[1] + " please insert another"+
                " directory to compare: " + '\n' )
        if(os.path.isdir(directory)):
            eliminarFicherosDuplicados(sys.argv[1], directory)
        else:
            print("Error, one of the directories does not exist")
    elif len(sys.argv) == 3:
        #Case when 2 parameters are passed to the script

        if(os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2])):
            eliminarFicherosDuplicados(sys.argv[1], sys.argv[2])
        else:
            print("Error, one of the directories does not exist")

    else:
        print("Error, the parameters are not necessary")



def eliminarFicherosDuplicados(dir1, dir2):
    filesDir1 = subprocess.getoutput("ls " + dir1).split() #Get a list of files
    filesDir2 = subprocess.getoutput("ls " + dir2).split() #Get a list of files


    for file1 in filesDir1:
        for file2 in filesDir2:
            if file1 == file2:
                pathFile1 = dir1 + "/" + file1
                pathFile2 = dir2 + "/" + file2
                #TODO falta borrar el mas nuevo

                if filecmp.cmp(pathFile1, pathFile2, shallow=False):
                    dateTimeFile1 = (time.ctime(os.path.getctime(pathFile1)), pathFile1)
                    dateTimeFile2 = (time.ctime(os.path.getctime(pathFile2)), pathFile2)
                    borrar = max(dateTimeFile1[0], dateTimeFile2[0])
                    if(borrar == dateTimeFile1[0]):
                        os.system("rm " + dateTimeFile1[1])
                        print("File: " + dateTimeFile1[1] + " deleted")
                    elif(borrar == dateTimeFile2[0]):
                        os.system("rm " + dateTimeFile2[1])
                        print("File: " + dateTimeFile2[1] + " deleted")


if __name__ == "__main__":
    """
    De esta forma, se comprueba en python para que al ejecutarse el script
    vaya a la función indicada en este caso main.
    """
    main()
