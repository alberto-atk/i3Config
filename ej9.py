import os, sys, random




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
def main():
    array="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    randomNumber = random.randrange(3000)

    key=""
    cifferValue =""


    for i in range (10):
        char = random.randrange(len(array)) + 1
        key += array[(char - 1):char:1]
        cifferValue += str((ord(key[i:i + 1: 1]) + randomNumber) % 256) + " "

    print("The key is: " + key)
    print("The ciffer key is:" + cifferValue)
    print("The random number is: " + str(randomNumber))




if __name__ == "__main__":
    """
    De esta forma, se comprueba en python para que al ejecutarse el script
    vaya a la función indicada en este caso main.
    """
    main()
