import csv

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
from email.mime.image import MIMEImage

def send_email():
    para_envio = []
    with open("emails.csv", "r") as f:
        arquivo = csv.reader(f, delimiter=",")
        for item in arquivo:
            email = item[0]
            para_envio.append(email)

    botao = '<a href="https://business.google.com"><button style="background: #00DC6A; border-radius: 6px; padding: 15px; cursor: pointer; color: #fff; border: none; font-size: 16px;"><b>Perfil da empresa</button</b></a>'
    botao2 = '<a href="https://appgoogle.nappsolutions.com/"><button style="background: #00DC6A; border-radius: 6px; padding: 15px; cursor: pointer; color: #fff; border: none; font-size: 16px;"><b>Plataforma O2O</b></button></a>'

    for envio in para_envio:
        print(f'enviando email para {envio}')
        remetente = "email remetente"
        destino = [envio]

        print('carregando corpo do email')
        msg = MIMEMultipart() 
        msg['From'] = remetente 
        msg['To'] = ', '.join(destino)
        msg['Subject'] = "Olá, temos uma boa notícia para você!"
        body = f'<br><img src="cid:image1"><br><p><hr><b>Acesse Agora:</b></p>{botao}<p>{botao2}</p>'
        msg.attach(MIMEText(body, 'html'))  

        print('carregando imagem')
        imagem = open('diretorio da imagem', 'rb')
        msgImage = MIMEImage(imagem.read())
        imagem.close()

        msgImage.add_header('Content-ID', '<image1>')
        msg.attach(msgImage)

        send = smtplib.SMTP('smtp.gmail.com: 587')
        send.starttls() 
        send.login(remetente, "senha do email")
        text = msg.as_string().encode('utf-8')
        send.sendmail(remetente, destino, text) 
        send.quit() 

        print('Email enviado!')

send_email()
