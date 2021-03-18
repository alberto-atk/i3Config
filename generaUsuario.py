import os, platform, sys,subprocess
"""
Definición del metodo principal del programa
Nombre: main
Fecha de creacion: 28/02/2021
Miembros: Roberto Jiménez y Alberto Pérez
Última modificación: 28/02/2021
Parámetros: Ninguno, los parámetros son los que se pasan como argumento a la
llamada
"""

def createUser(nameUser, group):
    os.system("sudo groupadd" + group)
    os.system("sudo useradd -g" + group + " "+  nameUser)
    os.system("passwd " + nameUser)
    os.system("sudo mkdir /home/" + nameUser)
    os.system("sudo chown " + nameUser + ":" + group + " -R /home/" + nameUser)
    os.system("sudo usermod -s /bin/bash " + nameUser)
def main():

    if  platform.system() != 'Linux':
        #Check if is a UNIX machine
        print("Error, the OS is not a UNIX machine. Getting out...")
        exit(1)
    if len(sys.argv) == 1:
        for i in range(4):
            user = input("Introduce username for new user")
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





























condicionUsuario='^[a-z]{3,8}$'
condicionNombre='^[a-z|A-Z|áéíóúñ| ]*$'
condicion='^[a-zA-Z|áéíóú| |\.|\,|\;|\_|\-]*$'
condicion2='/[\:]/'


 if [ $# -eq 3 ]
 then

   if [[ $1 =~ $condicionUsuario ]]
   then
    usuario=$1

   else
    echo "Login incorrecto, el login "$1" debe tener entre 3 y 8 carácteres en minúsculas "
    exit
   fi

   if [[ $2 =~ $condicion2 ]]
   then
     echo "Nombre correcto"
     nombre=$2
    else
     echo "El nombre real no puede contener el caracter :"
     exit
   fi

   if [[ $3 =~ $condicionGrupo ]]
   then
    echo "Grupo correcto"
    grupo=$3
   else
    echo "El grupo tiene que ser contabilidad, finanzas ó estadistica"
    exit
   fi

  sudo groupadd -fK GID_MIN=100 -K GID_MAX=999 $grupo

   if [ $? -ne 0 ]
   then
    echo "Ha habido problemas"
    exit
   else
    echo "El grupo $grupo ha ido bien"
   fi
   sudo useradd -g $grupo  $usuario

    if [ $? -ne 0 ]
    then
     echo "Error creando el usuario"
     exit
    else
      echo "Usuario $usuario creado"

    fi
   sudo mkdir /home/$usuario
   sudo chown $usuario:$grupo -R /home/$usuario
   #sudo usermod -d /home/$usuario $usuario
   sudo usermod -s /bin/bash $usuario

   if [ $? -ne 0 ]
   then
    echo "Ha habido problemas cambiando la consola"
    exit
   else
    echo "Se ha cambiado la terminal a /bin/bash"
   fi
   echo "Introduce la contraseña del usuario"
   sudo passwd $usuario
   sudo userdel -r $usuario
   #sudo mail -u $usuario




 else
  echo "No has introducido 3 argumentos"
  exit
fi
