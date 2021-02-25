import os, sys, platform
import psutil, time, smtplib, signal
from email.mime.text import MIMEText



"""
Ejercicio 3. Desarrollar un script que nos muestre por consola el consumo de CPU
y calcule internamente si dicho consumo supera el 70% 4 veces consecutivas,
en un periodo de tiempo preestablecido por el administrador.
En caso de producirse dicho evento, el script deberá enviar un mail al correo
del administrador
"""

"""
Usage: Defining a method that lists the files in a directory
Name of method: recursivelyList
Date of creation: 20/02/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 25/02/2021 //rellenar lo demas solo bien fechas
Parameters:
    Entry:
     path: Directory from which the list of files or directories
           that exist is obtained
    Out: List with files and directories
"""

def create_sesion(emisor, passwd):
    #https://docs.python.org/3/library/smtplib.html
    # Nos conectamos al servidor SMTP de Gmail
    serverSMTP = smtplib.SMTP('smtp.gmail.com',587)
    serverSMTP.starttls()

    # Iniciamos sesión
    serverSMTP.login(emisor, passwd)
    return serverSMTP


"""
Definition of the main method of the program
Name of method: main
Date of creation: 20/02/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 25/02/2021
Parameters:  None, parameters are read by console
"""
def generateMail(mailFrom,to,subject, content):
    message = MIMEText(content, "plain")
    message["From"] = mailFrom
    message["To"] = to
    message["Subject"] = subject
    return message

"""
Definition of the main method of the program
Name of method: main
Date of creation: 20/02/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 25/02/2021 //rellenar lo demas solo esta bien fecha
Parameters:  None, parameters are read by console
"""
def main():
    if  platform.system() != 'Linux':
        #Check if is a UNIX machine
        print("Error, the OS is not a UNIX machine. Getting out...")
        exit(1)
    if len(sys.argv) == 1:
        mailFrom = "roberatecaads2@gmail.com"
        passwd='administracion2'

        mailTo = "rooobertrl@gmail.com"

        content = "Last 60 seconds, CPU has reached 4 times more than 70%"
        subject = "High CPU!"

        signal.alarm(60)
        reachedTimes = 0
        while(True):
            CPUpercent = psutil.cpu_percent(interval=3)
            if CPUpercent >= 70:
                reachedTimes += 1
            else:
                reachedTimes = 0
            if reachedTimes == 4:
                try:
                    smtp = create_sesion(mailFrom,passwd)
                    email = generateMail(mailFrom, mailTo, subject,content )
                    smtp.sendmail(mailFrom, mailTo, email.as_string())
                    smtp.quit()
                except Exception as e:
                    print("Excepcion: ", e)
                break

    else:
        #Case when parameters are passed to the script
        print("Error, the parameters are not necessary")









if __name__ == "__main__":
    """
    In that case, we check that the program starts in the right function, in our
    case, main()
    """
    main()
