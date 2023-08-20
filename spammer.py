import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Email configuration
sender_email = 'your_email@gmail.com'
sender_password = 'your_email_password'
receiver_email = 'recipient@example.com'
subject = 'Demo Email'

# Create the email content
def create_demo_content():
    return "This is a demo email sent for demonstration purposes."

# Send the email
def send_demo_email():
    demo_content = create_demo_content()

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(demo_content, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

    print("Demo email sent successfully")

# Send a demo email every 1 second
while True:
    send_demo_email()
    time.sleep(1)
