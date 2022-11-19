########################################################################################
# Send mail from your Gmail account using Python
# https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python
########################################################################################

# The 3 steps:
# 1. import smtplib, ssl
# 2. from getpass import getpass
# 3. from email.message import EmailMessage

################################
#   libraries to be imported   #
################################

from email.message import EmailMessage
import os
import ssl
import smtplib

################################
#     Email parameters         #
################################


smtp_server = 'smtp.gmail.com'
port = 465                           # 465

# print(os.environ.get("EMAIL_PASSWORD"))

email_sender = 'oscar.centeno.mora@gmail.com'
# email_password = os.environ.get("EMAIL_PASSWORD")
# print(email_password)

email_password = 'XXXXXXXXXXukdxmgz'

# Or with Take a tempory mail with https://temp-mail.org/

email_receiver = 'oscarcenteno86@gmail.com'    

subject = "Email with python without attachment"

body = """

The song of the moment by Spotify: https://www.youtube.com/watch?v=Tq0DA9J5-oM&list=RDTq0DA9J5-oM&start_radio=1&ab_channel=WanoKuni
"""

################################
#     EMail specifications     #
################################

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

#####################################
#        SMTP especifcation         #
#####################################

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server,port, context=context) as mail: 
    mail.login(email_sender,email_password)
    mail.sendmail(email_sender,email_receiver, em.as_string())
    print("Sent...")