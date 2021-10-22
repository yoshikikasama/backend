# from email import message
from email.mime import multipart
from email.mime import text
import smtplib

smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'hoge@gmail.com'
to_email = 'hoge@gmail.com'
username = 'hoge@gmail.com'
password = 'hoge'

# msg = message.EmailMessage()
msg = multipart.MIMEMultipart()
# msg.set_content('Test email')
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email
msg.attach(text.MIMEText('Test email', 'plain'))

with open('email_lesson.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment',
        filename='email_lesson.txt'
    )
    msg.attach(attachment)

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()
