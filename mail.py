from os import environ
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage


def SendMail(to, subject, body):
    sender = "meji.hello@gmail.com"
    password = environ.get("MAIL_PASSWORD")

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    msg.attach(MIMEText(body, "html"))

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender, password)
    server.sendmail(sender, to, msg.as_string())
    server.quit()

    result = "Mail Sent"
    print(result)
    return result


def SendMail2(to, subject, body):
    email = "meji.hello@gmail.com"
    password = environ.get("MAIL_PASSWORD")

    msg = EmailMessage()
    msg['to'] = to
    msg['subject'] = subject
    msg.set_content(body)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    # server.sendmail(email, to, msg.as_string())
    server.quit()

    # result = "Mail Sent"
    # print(result)
    # return result


SendMail2("theophilus.ogbolu@gmail.com", "hello", "hello")
