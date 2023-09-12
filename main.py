import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


# Email configuration
smtp_server = 'smtp.wp.pl'
smtp_port = 465  # or the appropriate port for your SMTP server
sender_email = 'XYZ@gmail.com'
sender_password = 'qwerty'
subject = 'Oferta firmy ***'

with open('index.html', 'r', encoding='utf-8') as file:
    html_message = file.read()

with open('adresmaila.txt', 'r') as file:
    lines = file.readlines()


# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)  # Use SMTP_SSL for SSL connection
    server.login(sender_email, sender_password)
    for line in lines:
        receiver_email = line.strip()
        # Create the email message
        msg = MIMEMultipart('alternative')
        # Attach the HTML message
        msg.attach(MIMEText(html_message, 'html'))
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent successfully!')
    server.quit()
except Exception as e:
    print('Error sending email:', str(e))

time.sleep(10)
