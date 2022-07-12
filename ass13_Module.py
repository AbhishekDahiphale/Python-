import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email import message
import psutil
import time
from sys import*
import os
import hashlib

def Mail_Sender(log_file,toaddr=argv[3]):
    fromaddr = "pm300500166@gmail.com"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr

    msg['Subject'] = "Mail send using automation"

    body = """Hi 
    I am abhishke Dahiphale 
                     yours
                     %s"""%fromaddr

    msg.attach(MIMEText(body,'plain'))

    attach = open(log_file,'rb')

    p = MIMEBase('application','octet-stream')
    p.set_payload((attach).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % log_file)                 
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("pm300500166@gmail.com","Python166")
    text = msg.as_string()
    s.sendmail(fromaddr,toaddr,text)
    s.quit()


def Write_log(List):
    dirName = "Marvellous"
    if not os.path.isdir(dirName):
        os.mkdir(dirName)
    else:
        pass

    Log_file = "%s.log"%time.time() 
    Logfile_path = os.path.join(dirName,Log_file)
    design = "*"*80
    start_data = "Scrpt information : %s"%time.ctime()
    fd = open(Logfile_path,'a')
    fd.write(design+"\n")
    fd.write("\n"+start_data+"\n\n")
    fd.write(design+"\n\n")
    for file in List:
        print()
        data = file + "\n"
        fd.write(data)
    fd.close()
    Mail_Sender(Logfile_path,argv[3])

def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DublicateFileRemoval(dir=argv[1]):
    diction = dict()
    removal_list = list()
    if not os.path.isabs(dir):
        dir = os.path.abspath(dir)

    exists = os.path.isdir(dir)
    if exists:
        for foldername,subfolder,filename in os.walk (dir):
            for filen in filename:
                Mk_path = os.path.join(foldername,filen)
                unique = hashfile(Mk_path)
                flag = False
                for key in diction:
                    if diction[key] == unique:
                        removal_list.append(filen)          
                        flag = True
                        os.remove(Mk_path)
                if flag == False:
                    diction.update({filen : unique})
        Write_log(removal_list)  
    else:
        print("Invalide Path")    