# https://docs.python.org/3/library/smtplib.html
import smtplib

my_email = "technicolorconnectedhomes123@gmail.com"
my_password = "***********"
connection = smtplib.SMTP("smtp.gmail.com")
# gmail = smtp.gmail.com
# live = smtp.live.com
# yahoo = smtp.mail.yahoo.com

connection.starttls()
# Puts the connection to the SMTP server into TLS mode.
# If there has been no previous EHLO or HELO command this session, this method tries ESMTP EHLO first.
# If the server supports TLS, this will encrypt the rest of the SMTP session. If you provide the keyfile 
# and certfile parameters, the identity of the SMTP server and client can be checked. 
# This, however, depends on whether the socket module really checks the certificates.
# This method may raise the following exceptions:
#  SMTPHeloError The server didn't reply properly to the helo greeting.

connection.login(user=my_email,password=my_password)
# Log in on an SMTP server that requires authentication.

# The arguments are:

# user: The user name to authenticate with.
# password: The password for the authentication.

connection.sendmail(from_addr=my_email,to_addrs="adisnowball99@gmail.com",msg="Subject:Hello\n\n This is the body of the demo mail")
connection.close()

