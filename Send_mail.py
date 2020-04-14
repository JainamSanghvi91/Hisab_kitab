import smtplib
from email.message import EmailMessage

class Send_Email():
    def __init__(self):
        self.sender = 'hisabkitab1224@gmail.com'
        self.passwd = "Bh@gw@n1010"

    def send_mail(self, receivers,username,message):
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.sender, self.passwd)
        msq=EmailMessage()
        msq['From']=self.sender
        msq['To']=receivers
        msq['Subject']="Pay to "+username
        msq.set_content(message)
        server.send_message(msq)
        server.quit()

