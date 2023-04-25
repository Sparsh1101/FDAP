import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr
import datetime


def sendEmail(receiver):
    # All basic configurations
    host = "smtp.gmail.com"
    port = 25
    sender_email = "hardikriyasparsh@gmail.com"
    sender_password = "gcrqndtkbqhotlxf"

    # Setting up mime (This is where all the email related headers, body etc is set up)
    mime = MIMEMultipart("alternative")
    mime["From"] = formataddr(
        ("Code Runner", "hardikriyasparsh@gmail.com")
    )  # The senders details
    mime["Reply-To"] = formataddr(
        ("Code Runner", "hardikriyasparsh@gmail.com")
    )  # If the receiver clicks on reply this is the email id to which the mail will be sent
    mime["To"] = receiver.get("To", "")  # The receivers email ids
    mime["Cc"] = receiver.get("Cc", "")  # The Cc receivers email ids
    # This are all the recipients who will receive the mail (Note: Bcc is not a parameter that mime takes so all the email ids that are not under "To" and "Cc" by default become "Bcc")
    all_recipients = (
        receiver.get("To", "").split(",")
        + receiver.get("Cc", "").split(",")
        + receiver.get("Bcc", "").split(",")
    )

    mime["Subject"] = "DBScan Parameter Tuning"  # Subject of the mail
    # The body of the mail
    
    text = str(sys.argv[0])
    body_text = MIMEText(text, 'plain')  # 
    mime.attach(body_text)  # attaching the text body into msg

    ## Attachments in general
    ## Replace filename to your attachments. Tested and works for png, jpeg, txt, pptx, csv
    # filename = "" # TODO: replace your attachment filepath/name
    # with open(filename, 'rb') as fp:
    #     attachment = MIMEApplication(fp.read())
    #     attachment.add_header('Content-Disposition', 'attachment', filename=filename)
    #     mime.attach(attachment)

    # Actually sending the mail after completing all the configurations above
    try:
        print("Sending mail to:", receiver)
        connection = smtplib.SMTP(host, port)
        connection.starttls()
        connection.login(sender_email, sender_password)
        connection.sendmail(mime["From"], all_recipients, mime.as_string())
        connection.quit()
        print("Mail sent successfully! Sent at:", datetime.datetime.now())
    except Exception as e:
        print(
            "Error sending the mail!\nFor debugging purposes, the error is as follows:"
        )
        print(e)

test_run = {"To": "sparshtgupta@gmail.com", "Cc": "devansh.ts@somaiya.edu, hardikriyasparsh@gmail.com,  hardik.kj@somaiya.edu, riya.rege@somaiya.edu", "Bcc": ""}

sendEmail(test_run)