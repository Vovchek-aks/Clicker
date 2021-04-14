import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from_email = 'code_sender@mail.ru'
password = ']=[-p0o9'
to_email = 'profitcamp@mail.ru'
message = 'Программа отработала. Необходимо проверить.'

msg = MIMEMultipart()
msg.attach(MIMEText(message, 'plain')) 
server = smtplib.SMTP('smtp.mail.ru: 25')
server.starttls()
server.login(from_email, password)
server.sendmail(from_email, to_email, msg.as_string())
server.quit()

