import smtplib
from email.message import EmailMessage
import os

    
def sendEmail(subject, receiver_email ,attachment_file_path ,emailBody,sender_email = "abc@example.com"):
        
    try:
        email_password = os.environ['email_password']
    except KeyError:
        print("environment variable not found.")

    msg = EmailMessage()
    msg.set_content(emailBody)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with open(attachment_file_path, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='text', subtype='plain', filename=file_name)
    print(emailBody)
    print('Email sent successfully!')

    # try:
    #     with smtplib.SMTP(smtp_server="smtp.gmail.com", smtp_port=587) as smtp:
    #         smtp.starttls()
    #         smtp.login(sender_email, email_password)
    #         smtp.send_message(msg)
    #         print('Email sent successfully!')
    # except Exception as e:
    #     print(f'Failed to send email: {e}')
