import re
import dns.resolver
import socket
import smtplib


class Email_verify():    

    def verify_email(self,email):
        fromadress='abc@gmail.com'
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

        if match == None:
                return -1

        splitAddress=email.split('@')
        domain=str(splitAddress[1])
        print('Domain: ',domain)

        records = dns.resolver.query(domain, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)

        # Get local server hostname
        #host = socket.gethostname()

        # SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP()
        server.set_debuglevel(0)

        # SMTP Conversation
        server.connect(mxRecord)
        server.helo(server.local_hostname)
        server.mail(fromadress)
        code, message = server.rcpt(str(email))
        server.quit()

        # Assume 250 as Success
        if code == 250:
                return 1
        else:
                return 0
