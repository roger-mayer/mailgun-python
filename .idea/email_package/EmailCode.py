# import OS for private info in my mac
import os

# import smtp library module
import smtplib
import EmailCreds
import imghdr
from email.message import EmailMessage

# TO GET FROM OS
# EMAIL_ADD = os.environ.get('EMAIL_ADDRESS')
# EMAIL_PASS = os.environ.get('EMAIL_PASSWORD')

# OR RUN IN TERMINAL FOR LOCAL DEBUGGING
# python3 -m smtpd -c DebuggingServer -n localhost:1025

# USED .gitignore TO HIDE PW EmailCreds
EMAIL_ADD = EmailCreds.EMAIL_ADD
EMAIL_PASS = EmailCreds.EMAIL_PASS
print(EMAIL_ADD)


msg = EmailMessage()
msg['Subject'] = 'I sent this with python'
msg['From'] = EMAIL_ADD
msg['To'] = 'roger@geekdom.com'
msg.set_content('Hi! How are you!')

files = ['RogerImg.jpeg', 'GeekdomSticker.jpeg']

# for html
msg.add_alternative("""\
<!DOCTYPE HTML>
    <html>
        <body>
            <h2 style="color:Red;"> HTML Rulez DOOd</h2>
        </body>
    </html>
""", subtype='html')

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADD, EMAIL_PASS)
    smtp.send_message(msg)

