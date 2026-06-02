import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'ficek.risa@gmail.com'
PASSWORD = 'igxx vwyp voru uzsi'




def sentEmail(email: str, subject: str):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = email

    msg.set_content("""Ahoj,
    tohle je správně a bezpečně odeslaný e-mail z Pythonu za pomoci STARTTLS.

    Měj se fajn,
    Tvůj skript""")

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade spojení na šifrované
            
            server.login(SENDER_EMAIL, PASSWORD)
            
            server.send_message(msg)
            
        return True, 'Email sent successfully'

    except Exception as e:
        return False, str(e)        


# sentEmail('ficek.risa@gmail.com', 'Test Subject')