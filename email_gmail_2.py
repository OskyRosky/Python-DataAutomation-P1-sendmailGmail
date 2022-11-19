########################################################################################
# Send mail from your Gmail account using Python
# https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/
########################################################################################

#  A fast code

################################
#   libraries to be imported   #
################################

import smtplib
 
################################
#   creates SMTP session      #
################################ 

s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()

################################
#     EMail specifications     #
################################
 
 email_sender = 'oscar.centeno.mora@gmail.com'
# email_password = os.environ.get("EMAIL_PASSWORD")
# print(email_password)

email_password = 'XXXXXXXXXXukdxmgz'

email_receiver = 'oscarcenteno86@gmail.com'     
 
# Authentication
s.login(email_sender, email_password)
 
# message to be sent
message = "Message_you_need_to_send"


#####################################
#        SMTP especifcation         #
#####################################

 
# sending the mail
s.sendmail(email_sender, email_receiver, message)
 
# terminating the session
s.quit()