import smtplib
from string import Template
from time import sleep

# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Get the smtp credentials
settings = {}

with open("./cred.txt", mode="r") as cred:
    for x in cred:
        parts = x.split("=")
        settings[parts[0]] = parts[1].strip()



def contacts():
    email_list = []
    with open("./emails.txt", mode="r", encoding="UTF-8") as fp:
        for email in fp:
            email_list.append(email.strip())

    return email_list

def read_message():
    with open("./message.txt", mode="r") as fp:
        message = fp.read()
        
    return message


if __name__ == "__main__":
    print(settings)
    # Create the smtp client
    smtp = smtplib.SMTP(settings["HOST"], int(settings["PORT"]))
    # smtp.starttls()
    smtp.login(settings["USERNAME"], settings["PASSWORD"])

    emails = contacts()
    message_text = read_message()
    print(message_text)
    for email in emails:
        msg = MIMEMultipart() # Create the email message

        msg['From']=settings["FROM"]
        msg['To']=email
        msg['Subject']="PREPAID METER REQUEST REMINDER"

        msg.attach(MIMEText(message_text, "plain"))
        smtp.send_message(msg)
        sleep(3)
        del msg

    smtp.quit()