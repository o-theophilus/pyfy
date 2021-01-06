import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def SendMail(to, subject, body):


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
