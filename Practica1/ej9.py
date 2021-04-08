import os, sys, random

"""
Ejercicio 9. Realizar un script que nos genere password cifrados de 10 caracteres aleatorios,
siendo dichos caracteres los que a continuación se describen dentro de un vector:
VECTOR="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwx
yz"
Posteriormente realizar la compresión de un fichero de texto:
casa bbb zzzzz ff  casa 3b 5z ff (2f)
Y a continuación realizar un cifrado simple de cada uno de los caracteres:
Carácter cifrado = (Código ASCII(carácter) + número constante) Módulo 256
¿Cómo se podría desencriptar?
Nota: se puede usar el valor devuelto por la variable RANDOM 
"""


"""
Usage: Defining a main method that generate a ciffer key using ASCII code and
module operation
Name of method: main
Date of creation: 24/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 24/03/2021
Parameters:
    Entry: None, Parameters are requested by console
    Out: None, key is shown by console
"""
def main():
    #Declare a variable  which contains characters permitted
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
