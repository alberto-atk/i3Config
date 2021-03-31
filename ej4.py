import imaplib, pyzmail, platform, sys, datetime, locale

"""
Ejercicio 4. Desarrollar un script en Python que elimine de una cuenta de correo de Gmail los
emails no leídos en un intervalo de fechas previamente preestablecido.
Nota: paquetes necesarios para el uso de las acciones requeridas (imapclient,pyzmail) 
"""

"""
Definition of the main method of the program
Name of method: main
Date of creation: 27/02/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification:
    - 3/03/2021 If a date is wrong, exit from the program
    - 5/03/2021 Calling deleteMails for delete all incorrect mails
Parameters:  None, parameters are read by console
"""
def main():

    if  platform.system() != 'Linux':
        #Check if is a UNIX machine
        print("Error, the OS is not a UNIX machine. Getting out...")
        exit(1)
    if len(sys.argv) == 1:
        #Gets the initial date and check if its correct
        startDate = input("Put the start date: (dd-mm-yyyy): ")
        startDateAux = checkDate(startDate)
        if(not(startDateAux)):
            print("Getting out...")
            exit()

        #Gets the initial date and check if its correct
        finalDate = input("Put the final date: (dd-mm-yyyy): ")
        finalDateAux = checkDate(finalDate)
        if(not(finalDateAux)):
            print("Getting out...")
            exit()

        #Check if the range has sense
        if(finalDateAux < startDateAux):
            print("Error, start date is bigger than final date")
            print("Getting out...")
            exit()

        #Making login in the mail
        server = imaplib.IMAP4_SSL('imap.gmail.com')
        server.login('roberatecaads2@gmail.com', 'administracion2')
        select_info = server.select("INBOX")

        #Deleting all mails
        deleteMails(server, startDateAux, finalDateAux)

    else:
        #Case when parameters are passed to the script
        print("Error, the parameters are not necessary")


"""
Checks if the date passed got by console is correct
Name of method: checkDate
Date of creation: 28/02/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification: 
    - 3/03/2021. Checks the format of the date
    - 5/03/2021. Checks if the date is correct
Parameters:  
    Entry:
        - date: String of the date provided by the user
    Out: 
        - datetime, the date in datetime format 
"""
def checkDate(date):
    try:
        dateAux = str(date).split("-")
        return datetime.datetime(int(dateAux[2]),int(dateAux[1]),int(dateAux[0]))
    except ValueError:
        print("Error, date doesn't exists")
        return None
    except IndexError:
        print("Error, incorrect date format")
        return None



"""
Delete all mails in a date range
Name of method: main
Date of creation: 27/02/2021
Members: Roberto Jiménez y Alberto Pérez
Last modification:
    - 27/02/2021 Delete all mails without date range
    - 28/02/2021 Using the since sentence for delete the mails in the date range
Parameters:  
    Entry:
        - server: Connection with the mail provider
        - startDate: Initial date provided by the user
        - finalDate: Final date provided by the user
    Out:
"""
def deleteMails(server,startDate,finalDate):
    query = ("UNSEEN SINCE " + startDate.strftime("%d-%b-%Y") + " BEFORE "
            + finalDate.strftime("%d-%b-%Y"))
    estado, messages = server.search(None,query)
    messages = messages[0].split()

    for mail in messages:
        server.store(mail, '+FLAGS', '\\Deleted')
    print(str(len(messages)) + " mail deleted")
    server.expunge()


if __name__ == "__main__":
    """
    In that case, we check that the program starts in the right function, in our
    case, main()
    """
    main()
