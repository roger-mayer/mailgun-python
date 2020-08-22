# import OS for private info in my mac
import os

# import smtp library module
import smtplib
import imghdr

# from email.message import EmailMessage

EMAIL_ADD = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASS = os.environ.get('EMAIL_PASSWORD')



with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    # identify as encripted connection
    smtp.ehlo()
    # encript traffic
    smtp.starttls()
    # reidentify self as encripted package
    smtp.ehlo()

    smtp.login(EMAIL_ADD, EMAIL_PASS)

    subject = 'I sent this with python'
    body = 'This is a plain text email'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADD, 'rmayer1984@gmail.com', msg)
#
# contacts = ['rmayer1984@gmail.com', 'rmayer1984@gmail.com']
#
# msg = EmailMessage()
# msg['Subject'] = 'I sent this with python'
# msg['From'] = EMAIL_ADDRESS
# msg['To'] = 'YourAddress@gmail.com'
#
# msg.set_content('This is a plain text email')
#
# msg.add_alternative("""\
# <!DOCTYPE html>
# <html>
#     <body>
#         <h1 style="color:SlateGray;">This is an HTML Email!</h1>
#     </body>
# </html>
# """, subtype='html')
#
#
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     smtp.send_message(msg)