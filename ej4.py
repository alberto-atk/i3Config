import os, pyzmail, platform, sys
from imapclient import IMAPClient



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
        #startDate = input("Put the start date: (xx-xx-xxxx)")

        #finalDate = input("Put the final date: (xx-xx-xxxx)")

         server = IMAPClient('smtp.gmail.com', use_uid=True)
         server.login('roberatecaads2@gmail.com', 'administracion2')
         select_info = server.select_folder('INBOX')

         messages = server.search(None, 'UNSEEN')


         for msgid, data in server.fetch(messages, ['ENVELOPE']).items():
             envelope = data[b'ENVELOPE']
             print('ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))


    else:
        #Case when parameters are passed to the script
        print("Error, the parameters are not necessary")







if __name__ == "__main__":
    """
    In that case, we check that the program starts in the right function, in our
    case, main()
    """
    main()
