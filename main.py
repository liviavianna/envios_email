from email.message import EmailMessage
import ssl
import smtplib

meu_email = "livia.vianna8@gmail.com"
senha_gerada = "" #sua senha
destinatario_email = "" #email destinatario
assunto = "Testando Python"
body = """
Teste
"""
em = EmailMessage()

em['From'] = meu_email
em['To'] = destinatario_email
em['subject'] = assunto
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(meu_email, senha_gerada)
    smtp.sendmail(meu_email, destinatario_email, em.as_string())