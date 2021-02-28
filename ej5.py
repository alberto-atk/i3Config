import os, sys, platform



"""
Definition of the main method of the program
Name of method: main
Date of creation: 28/02/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 28/02/2021 //rellenar lo demas solo esta bien fecha
Parameters:  None, parameters are read by console
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
