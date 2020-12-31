import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('email.html').read_text())
email = EmailMessage()
email['from'] = 'Dazz Kaminski'
email['to'] = 'kaminski.darek@icloud.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute(name='10000'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('kodilla.dazz4@gmail.com', 'kodilla_password')
    smtp.send_message(email)
    print('msg sent')

