from datetime import *
from email import message
import time
import schedule
from sys import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def Mail_Sender(dir=argv[1]):
    listToAddr=list()
    fromaddr = "pm300500166@gmail.com"
    listToAddr = ['prasadbade1066@gmail.com','jadhavabhishek164@gmail.com','nikitabade555@gmail.com','abhishek.v.dahihale@gmail.com','abhi.v.dahiphale@gmail.com','chawarayasumit4545@gmail.com','abhidahiphale3774@gmail.com','abhidahiphale3373@gmail.com','krutikadalvi23@gmail.com'] 
    #listToAddr = ['prasadbade1066@gmail.com','abhi.v.dahiphale@gmail.com','abhidahiphale3774@gmail.com','abhidahiphale3373@gmail.com'] 
    msg = MIMEMultipart()
    for toaddr in listToAddr:
        msg['From'] = fromaddr
        msg['To'] = toaddr

        msg['Subject'] = "Mail send using automation"

        body = """Hi 
            I am abhishke Dahiphale 
                Very Good Morning
                                
                                     yours
                                        %s"""%fromaddr

        msg.attach(MIMEText(body,'plain'))

        attach = open(dir,'rb')

        p = MIMEBase('application','octet-stream')
        p.set_payload((attach).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % dir)                 
        msg.attach(p)
    
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login("pm300500166@gmail.com","Python166")
        text = msg.as_string()
        s.sendmail(fromaddr,toaddr,text)
        s.quit()


def main():
    print("---- Abhishek Dahiphale-----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (len(argv)==2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("usage : ApplicationName Directory_name Email_address_want_to_send")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : This Script is used to send the mail attach with log file")
            exit()

    if (len(argv)==2):
        try:
            
            schedule.every(1).minute.do(Mail_Sender)
            while True:
                schedule.run_pending()
                time.sleep(1)
        except ValueError:
            print("Value Error")

        except Exception as e: 
            print("Error : ",e)
if __name__ == "__main__":
    main()               