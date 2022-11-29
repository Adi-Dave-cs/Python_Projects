# The client sends this command to the SMTP server to identify itself and initiate the SMTP conversation. using helo
# ehlo is same as helo but it tells the server that it will be using the extended smtp 
# https://www.samlogic.net/articles/smtp-commands-reference.htm
# https://www.youtube.com/watch?v=JRCJ6RtE3xU

import smtplib
import datetime as dt
import random

my_email = "technicolorconnectedhomes123@gmail.com"
my_password = "***********"

now = dt.datetime.now()
weekday = now.weekday()

if(weekday == 2):
    with open("D:\ADITYA IMPORTANT PDF\Codes\python\SMTP_Mail_sending\quotes.txt") as data:
        quotes = data.readlines()
        quote = random.choice(quotes)
    print(quote)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject : Motivation \n\n {quote}")