import imaplib, pyzmail, platform, sys, datetime, locale


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
        startDate = input("Put the start date: (dd-mm-yyyy): ")
        startDateAux = checkDate(startDate)
        if(not(startDateAux)):
            print("Getting out...")
            exit()

        finalDate = input("Put the final date: (dd-mm-yyyy): ")
        finalDateAux = checkDate(finalDate)
        if(not(finalDateAux)):
            print("Getting out...")
            exit()

        if(finalDateAux < startDateAux):
            print("Error, start date is bigger than final date")
            print("Getting out...")
            exit()

        server = imaplib.IMAP4_SSL('imap.gmail.com')
        server.login('roberatecaads2@gmail.com', 'administracion2')
        select_info = server.select("INBOX")

        deleteMails(server, startDateAux, finalDateAux)

    else:
        #Case when parameters are passed to the script
        print("Error, the parameters are not necessary")



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
