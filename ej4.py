import os, pyzmail, imapclient, platform, sys



"""
Definition of the main method of the program
Name of method: main
Date of creation: 28/02/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 28/02/2021
Parameters:  None, parameters are read by console
"""
def main():

    if  platform.system() != 'Linux':
        #Check if is a UNIX machine
        print("Error, the OS is not a UNIX machine. Getting out...")
        exit(1)
    if len(sys.argv) == 1:
        print("Robertito")

    else:
        #Case when parameters are passed to the script
        print("Error, the parameters are not necessary")







if __name__ == "__main__":
    """
    In that case, we check that the program starts in the right function, in our
    case, main()
    """
    main()
