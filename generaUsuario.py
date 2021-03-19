import os, platform, sys,subprocess

"""
Definición del metodo principal del programa
Nombre: createUser
Fecha de creacion: 19/03/2021
Miembros: Roberto Jiménez y Alberto Pérez
Última modificación: 19/03/2021
Parámetros: Ninguno, los parámetros son los que se pasan como argumento a la
llamada
"""
def createUser(nameUser, group):
    #os.system("sudo groupadd " + )
    userExists = os.system("sudo useradd -g " + group + " "+  nameUser)
    if(userExists != 0):
        return
    os.system("sudo passwd " + nameUser)
    os.system("sudo mkdir /home/" + nameUser)
    os.system("sudo chown " + nameUser + ":" + group + " -R /home/" + nameUser)
    os.system("sudo usermod -s /bin/bash " + nameUser)
    copyStartFiles()
    print("User has been created correctly")


"""
Definición del metodo principal del programa
Nombre: copyStartFiles
Fecha de creacion: 19/03/2021
Miembros: Roberto Jiménez y Alberto Pérez
Última modificación: 19/03/2021
Parámetros: Ninguno, los parámetros son los que se pasan como argumento a la
llamada
"""
def copyStartFiles():
    #Start files are copied to new user directory
    os.system("sudo cp ~/.bashrc /home/" + nameUser)
    os.system("sudo chown " +  nameUser + " /home/" + nameUser + "/.bashrc" )

    os.system("sudo cp ~/.profile /home/" + nameUser)
    os.system("sudo chown " +  nameUser + " /home/" + nameUser + "/.profile" )

    os.system("sudo cp ~/.bash_logout /home/" + nameUser)
    os.system("sudo chown " +  nameUser + " /home/" + nameUser + "/.bash_logout")
    #https://www.sever-world.info/en/note?os=Ubuntu_18.04&p=mail&f=3




"""
Definición del metodo principal del programa
Nombre: main
Fecha de creacion: 19/03/2021
Miembros: Roberto Jiménez y Alberto Pérez
Última modificación: 19/03/2021
Parámetros: Ninguno, los parámetros son los que se pasan como argumento a la
llamada
"""
def main():

    if  platform.system() != 'Linux':
        #Check if is a UNIX machine
        print("Error, the OS is not a UNIX machine. Getting out...")
        exit(1)
    if len(sys.argv) == 1:
        for i in range(4):
            user = input("Introduce username for new user ")
            createUser(user, "Alumnos")

    else:
        #Case when parameters are passed to the script
        print("Error, the parameters are not necessary")



if __name__ == "__main__":
    """
    De esta forma, se comprueba en python para que al ejecutarse el script
    vaya a la función indicada en este caso main.
    """
    main()
