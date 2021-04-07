import os, platform, sys,subprocess


"""
Ejercicio 8. Realizar un script que genere el alta de cuatro usuarios en el sistema, dichos
usuarios deberán pertenecer al grupo Alumnos, para ello se tendrán que realizar una serie de
etapas:
– Necesarias :
Editar el fichero /etc/passwd para definir la nueva cuenta de usuario.
Introducir una contraseña inicial (comando passwd).
Crear el directorio propio (HOME) del usuario.
– Conveniente para el usuario :
Copiar los ficheros de arranque por defecto al directorio del usuario.
Crear el directorio de correo del usuario y definir alias del correo.
Realizar las tareas de configuración especificas a algunas aplicaciones.
Informar al usuario cuando la apertura haya sido realizada.
– Conveniente para el administrador :
Añadir el usuario al fichero /etc/group.
Registrar información contable.
Introducir al usuario en la base de datos de usuarios de la entidad.
Configurar las cuotas de disco.
Verificar que la cuenta ha sido creada correctamente.
"""


"""
Usage: Defining a method that create a user into a Unix system
Name of method: createUser
Date of creation: 20/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 20/03/2021
Parameters:
    Entry:
        - nameUser: String which contains user's name
        - group: String which contains group name for new user
    Out: None
"""
def createUser(nameUser, group):
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
Usage: Defining a method that configure start files for new user, files copied
are:
    - ~/.bashrc
    - ~/.home
    - ~/.bash_logout
Name of method: copyStartFiles
Date of creation: 20/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 20/03/2021
Parameters:
    Entry: None
    Out: None
Documentation: https://www.sever-world.info/en/note?os=Ubuntu_18.04&p=mail&f=3
"""
def copyStartFiles():
    #Start files are copied to new user directory
    os.system("sudo cp ~/.bashrc /home/" + nameUser)
    os.system("sudo chown " +  nameUser + " /home/" + nameUser + "/.bashrc" )

    os.system("sudo cp ~/.profile /home/" + nameUser)
    os.system("sudo chown " +  nameUser + " /home/" + nameUser + "/.profile" )

    os.system("sudo cp ~/.bash_logout /home/" + nameUser)
    os.system("sudo chown " +  nameUser + " /home/" + nameUser + "/.bash_logout")





"""
Usage: Defining a main method
Name of method: main
Date of creation: 20/03/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 20/03/2021
Parameters:
    Entry: None
    Out: None
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
