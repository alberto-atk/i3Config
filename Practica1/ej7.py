import os, platform, sys,subprocess, copy, filecmp, time

"""
Ejercicio 7. Desarrollar un script que detecte ficheros duplicados en un directorio (por ejemplo
el dicrectorio /tmp) y automáticamente los elimine de dicho directorio
"""

"""
Definition of the main method of the program
Nombre: main
Fecha de creacion: 11/03/2021
Miembros: Roberto Jiménez y Alberto Pérez
Última modificación: 11/03/2021
Parámetros: Parameters are passed in the calling process
"""
def main():
    if  platform.system() != 'Linux':
        #Check if is a UNIX machineputt
        print("Error, the OS is not a UNIX machine. Getting out...")
        exit(1)
    if len(sys.argv) == 1:
        #Case when parameters are not passed to the script
        directory = input("Your current directory is: " + os.getcwd() + " please insert another"+
                " directory to compare: " + '\n' )
        if(os.path.isdir(directory)):
            deleteDuplicateFiles(os.getcwd(), directory)
        else:
            print("Error, the passed directory does not exist")
    elif  len(sys.argv) == 2:
        #Case when a parameter is passed to the script
        directory = input("Directory passed:" + sys.argv[1] + " please insert another"+
                " directory to compare: " + '\n' )
        if(os.path.isdir(directory)):
            deleteDuplicateFiles(sys.argv[1], directory)
        else:
            print("Error, one of the directories does not exist")
    elif len(sys.argv) == 3:
        #Case when 2 parameters are passed to the script

        if(os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2])):
            deleteDuplicateFiles(sys.argv[1], sys.argv[2])
        else:
            print("Error, one of the directories does not exist")

    else:
        print("Error, the parameters are not necessary")




"""
Deletes the duplicate files
Nombre: deleteDuplicateFiles
Fecha de creacion: 11/03/2021
Miembros: Roberto Jiménez y Alberto Pérez
Última modificación: 11/03/2021
Parámetros: 
    Entry:
        - dir1: First directory for getting the files
        - dir2: Second directory for getting the files
    Out:
"""
def deleteDuplicateFiles(dir1, dir2):
    filesDir1 = subprocess.getoutput("ls " + dir1).split() #Get a list of files from directory1
    filesDir2 = subprocess.getoutput("ls " + dir2).split() #Get a list of files from directory2


    for file1 in filesDir1:
        for file2 in filesDir2:
            #Compares if the name of two files is the same
            if file1 == file2:
                pathFile1 = dir1 + "/" + file1
                pathFile2 = dir2 + "/" + file2

                #Compares if the content of two files is the same
                if filecmp.cmp(pathFile1, pathFile2, shallow=False):
                    dateTimeFile1 = (time.ctime(os.path.getctime(pathFile1)), pathFile1)
                    dateTimeFile2 = (time.ctime(os.path.getctime(pathFile2)), pathFile2)
                    borrar = max(dateTimeFile1[0], dateTimeFile2[0])
                    #Deletes the newest file
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
