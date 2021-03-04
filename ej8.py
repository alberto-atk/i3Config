import os, sys

"""
Usage: Defining a method that lists the files in a directory
Name of method: recursivelyList
Date of creation: 04/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 04/03/2021
Parameters:
    Entry: cipote
     path: Directory from which the list of files or directories
           that exist is obtained
    Out: List with files and directories
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
Usage: Defining a method that lists the files in a directory
Name of method: recursivelyList
Date of creation: 04/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 04/03/2021
Parameters:
    Entry:
     path: Directory from which the list of files or directories
           that exist is obtained
    Out: List with files and directories
"""
def optionB():
    print("Name of the .tar file")
    fileTarName = input()
    os.system(("tar -xvf" + fileTarName))

"""
Usage: Defining a method that lists the files in a directory
Name of method: recursivelyList
Date of creation: 04/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 04/03/2021
Parameters:
    Entry:
     path: Directory from which the list of files or directories
           that exist is obtained
    Out: List with files and directories
"""
def optionC():
    print("Name of .tar file")
    fileTarName = input()
    os.system(("ls -l " + fileTarName))

"""
Usage: Defining a method that lists the files in a directory
Name of method: recursivelyList
Date of creation: 04/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 04/03/2021
Parameters:
    Entry:
     path: Directory from which the list of files or directories
           that exist is obtained
    Out: List with files and directories
"""
def optionD():
    print("Name of .tar file: ")
    fileTarName = input()
    os.system(("tar -tf " + fileTarName))


"""
Usage: Defining a method that lists the files in a directory
Name of method: recursivelyList
Date of creation: 04/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 04/03/2021
Parameters:
    Entry:
     path: Directory from which the list of files or directories
           that exist is obtained
    Out: List with files and directories
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
