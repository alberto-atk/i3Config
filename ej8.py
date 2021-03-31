import os, sys

"""
Ejercicio 8. Generar un script que nos permita generar ficheros tar, inicialmente el script nos
mostrará un menú con las siguientes opciones:
a. Generacion fichero tar
b. Extracción fichero tar
c. Visualización de la información del fichero tar (nombre del fichero, propietario, y
tamaño)
d. Listado de todos los archivos incluidos en el fichero tar
e. Validación de que el fichero tar se ha generado correctamente, para ello el menú deberá
solicitar previamente el fichero tar a validar.
Sintaxis: generatar.py
"""


"""
Usage: Defining a method that create a Tar file from an input wrote by user
Name of method: optionA
Date of creation: 16/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 16/03/2021
Parameters:
    Entry: None
    Out: None, output it's tar file
"""
def optionA():
    print("Name of new tar file: ")
    fileTarName = input()
    next = "y"
    while next == "y":
        print("File name to introduce into a tar file: ")
        fileName = input()
        query = "tar -rvf " + fileTarName + " " + fileName
        os.system(query)
        print("Do you want add more files (y/n)?")
        next = input()


"""
Usage: Defining a method that extracts files from a Tar file
Name of method: optionB
Date of creation: 16/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 16/03/2021
Parameters:
    Entry: None
    Out: None, output is the files extracted
"""
def optionB():
    print("Name of the .tar file")
    fileTarName = input()
    os.system(("tar -xvf" + fileTarName))

"""
Usage: Defining a method that lists info from a Tar file
Name of method: optionC
Date of creation: 16/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 16/03/2021
Parameters:
    Entry: None
    Out: None, output only is showed by terminal
"""
def optionC():
    print("Name of .tar file")
    fileTarName = input()
    os.system(("ls -l " + fileTarName))


"""
Usage: Defining a method that lists the files in a Tar file
Name of method: optionD
Date of creation: 16/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 16/03/2021
Parameters:
    Entry: None
    Out: None, output only is showed by terminal
"""
def optionD():
    print("Name of .tar file: ")
    fileTarName = input()
    os.system(("tar -tf " + fileTarName))


"""
Usage: Defining a main method of program, which is able to work with Tar files,
differents options are splitted in some methods (OptionA, B, C and D).
Here user select from a menu differents options
Name of method: main
Date of creation: 14/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 16/03/2021
Parameters:
    Entry: None
    Out: None, info is requested by console
"""
main():
    continuar="y"
    while continuar == "y":
        print("-------------------------------------------------------------- \n"+
                "a) Generate tar file \n" +
                "b) Extract tar file \n" +
                "c) View info about tar file \n" +
                "d) List all files from a tar file\n" +
                "e) Exit \n" +
                "--------------------------------------------------------------")
        print("$ ", end ="")
        option = input()
        if option == "a":
            optionA()
        elif option == "b":
            optionB()
        elif option == "c":
            optionC()
        elif option == "d":
            optionD()
        elif option == "e":
            exit(0)
        else:
            print("Incorrect option")


        print("Do you want to do another operation (y/n)")
        continuar = input()


if __name__ == "__main__":
    """
    De esta forma, se comprueba en python para que al ejecutarse el script
    vaya a la función indicada en este caso main.
    """
    main()
