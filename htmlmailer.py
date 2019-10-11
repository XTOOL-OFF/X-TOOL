import smtplib
import time, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient email address

print("Fake Mailer!")
print("You can convert your mail messages to html on this webpage 'http://www.unit-conversion.info/texttools/text-to-html/'")
print("Easily Copy your message and convert it html!")
print("After paste this in some text file(Example:html.html)")
print("Or use your html code!")
Name = input("Enter from what name, message will be sended!:")
Subject = input("Enter Subject what you want!:")
#Message = input("Enter Message what you want!:")
VictimMail = input("Enter Victim Mail address!:")
namemail = (Name) + (" <testx9287@gmail.com>")
you = (VictimMail)
me = (namemail)
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = (Subject)
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = ""
os.system("cd")
print("Put your html file in X-TOOL Directory")
path = input("Enter html filename(html.html)!:")
text2 = open(path, "r").read()

html = text2


# Record the MIME types of both parts - text/plain and text/html.
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

mail.login("testx9287@gmail.com", 'Fedya13032018')
mail.sendmail(me, you, msg.as_string())
mail.quit()
