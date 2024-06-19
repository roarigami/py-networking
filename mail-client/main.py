import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('example@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'User'
msg['To'] = 'text@gmail.com'
msg['Subject'] = 'Submit your packets at once.. Just kidding this is a test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

msgImage = 'img/network.jpg'
attachment = open(msgImage, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; msgImage={msgImage}')
msg.attach(p)

text = msg.as_string()
server.sendmail('example@gmail.com', 'test@gmail.com', text)
