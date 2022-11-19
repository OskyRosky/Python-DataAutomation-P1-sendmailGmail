########################################################################################
# Send mail from your Gmail account using Python with an attachment 
# https://www.youtube.com/watch?v=aSPN4wQa_Go&ab_channel=TheOdinProject
########################################################################################

# Python code to illustrate Sending mail with attachments
# from your Gmail account 
  
############################
#   Stablish a directory   #
############################
import os

# Get the current working directory  : os.getcwd()
cwd = os.getcwd()
cwd

# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Let's set the directory 

path = 'C:\\Users\\oscar\\Desktop\\GitHub\\Python\\Projetcs\\P1'


# Change the current working directory
os.chdir(path)

# Let's check the new directory 

print("Current working directory: {0}".format(os.getcwd()))
  
  
################################
#   libraries to be imported   #
################################
  
import smtplib
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from pathlib import Path

################################
#    Email especification      #
################################


smtp_server = 'smtp.gmail.com'
port = 587                           # 465

# print(os.environ.get("EMAIL_PASSWORD"))

email_sender = 'oscar.centeno.mora@gmail.com'

# email_password = os.environ.get("EMAIL_PASSWORD")
# print(email_password)

email_password = 'XXXXXXXXXXukdxmgz'


#####################################
#     Create a MIMEMultipart()      #
#####################################

message = MIMEMultipart()
message["from"] = "Osky"
message["to"] = email_sender
message["subject"] = "Email with python with attachment."
message.attach(MIMEText("Stay connect always with data :=) "))
message.attach(MIMEImage(Path("data_mail.png").read_bytes()))

#####################################
#        SMTP especifcation         #
#####################################

with smtplib.SMTP(host = smtp_server,port = port) as smtp: 
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_sender,email_password)
  #  mail.sendmail(email_sender,email_receiver, em.as_string())
    smtp.send_message(message)
    print("Sent...")