import smtplib

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('example@gmail.com', password)
