import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient email address

print("Спуфер электронной почты!")
print("Вы можете конвертировать ваше почтовое сообщение на этой странице 'http://www.unit-conversion.info/texttools/text-to-html/'")
print("Просто скопируйте ваше сообщение и конвертируйте его в html!")
print("Потом вставьте выходные данные в текстовой файл(Пример:html.html)")
print("Или используйте свой html код!")
Name = input("Введите имя с которого будет отправлено сообщение!:")
Subject = input("Введите тему которую вы хотили!:")
#Message = input("Enter Message what you want!:")
VictimMail = input("Введите почту жертвы!:")
namemail = (Name) + (" <testx9287@gmail.com>")
you = (VictimMail)
me = (namemail)
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = ""
path = input("Введите путь к вашему текстовому файлу(Example: /home/html.html)!:")
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