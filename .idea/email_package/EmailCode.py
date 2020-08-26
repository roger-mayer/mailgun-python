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
TO_EMAILS = EmailCreds.TO_EMAILS
print(EMAIL_ADD)

for ToEmail in TO_EMAILS:
    msg = EmailMessage()
    msg['Subject'] = 'Interview Followup'
    msg['From'] = EMAIL_ADD
    msg['To'] = ToEmail
    msg.set_content('Hi! How are you!')

    files = ['RMayerResumeMG.jpeg',
            'RogerImg.jpeg',
             'GeekdomSticker.jpeg',
             ]

    # for html
    msg.add_alternative("""\
    <!DOCTYPE HTML>
    <head>
    <link href="css/bootstrap.min.css" rel="stylesheet">
        <style>
            .container {
            padding: 1em;
            justify-content: center;
            background: skyblue;
            }
            h2 {
            color:Red;
            border-bottom: 1px solid black;
            text-align: center;
            }
        </style>
    </head>
        <html>
            <body>
                <div class="container">
                    <div>
                    <h2>Hey Josh! This email was made using Python and simple HTML.</h2>
                    <h4>Below are several links including to the projects I would love to talk about with the Devs!</h4> 
                    <h4>(I've also attached my resume and several random photos which are part of my code demonstration)</h4>
                    <h4>-Roger </h4>
                    </div>
                    <div class="card">
                    <h4><a href="https://github.com/roger-mayer?tab=projects" target="_blank">Mailgun Projects</a></h4>
                    <h4><a href="https://github.com/roger-mayer" target="_blank">GitHub</a></h4>
                    <h4><a href="https://www.linkedin.com/in/roger-mayer/" target="_blank">LinkedIn</a></h4>
                    <h4><a href="mailto: rmayer1984@gmail.com" target="_blank">Send Me An Email!</a></h4>
                    </div>
                </div>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
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
