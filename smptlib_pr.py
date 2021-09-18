import smtplib, ssl
from info import Info

port = Info.port #указываем порт 587
smtp_server = Info.smtp_server
sender_email = Info.sender_email #отправитель
receiver_email = Info.receiver_email #получатель
password = input("Type your password and press enter:") #пароль от почты
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
