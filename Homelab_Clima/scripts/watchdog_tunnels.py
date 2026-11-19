import subprocess
import time
import re
import smtplib
from email.mime.text import MIMEText

SEU_EMAIL = "*********@gmail.com"
SENHA_APP = "*************"
DESTINATARIO = "*************@gmail.com"

def extrair_link(arquivo_log):
    try:
        with open(arquivo_log, "r") as f:
            conteudo = f.read()
        match = re.search(r"https://[-0-9a-z]+\.trycloudflare\.com", conteudo)
        return match.group(0) if match else "Erro ao gerar link"
    except Exception:
        return "Log não encontrado"

def enviar_email(link_gotty, link_fb):
    corpo = f"""Seu servidor no Termux iniciou ou reiniciou os túneis Cloudflare!

💻 GoTTY (Terminal - Porta 8080):
{link_gotty}

📁 File Browser (Arquivos - Porta 8081):
{link_fb}
"""
    msg = MIMEText(corpo)
    msg["Subject"] = "🔗 Novos Links do Servidor Termux"
    msg["From"] = SEU_EMAIL
    msg["To"] = DESTINATARIO

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SEU_EMAIL, SENHA_APP)
        server.sendmail(SEU_EMAIL, DESTINATARIO, msg.as_string())

while True:

    subprocess.run(["pkill", "-f", "cloudflared tunnel"], stderr=subprocess.DEVNULL)
    time.sleep(2)

    log_gotty = open("/data/data/com.termux/files/home/cf_gotty.log", "w")
    log_fb = open("/data/data/com.termux/files/home/cf_fb.log", "w")

    proc_gotty = subprocess.Popen(["cloudflared", "tunnel", "--url", "http://localhost:8080"], stdout=log_gotty, stderr=subprocess.STDOUT)
    proc_fb = subprocess.Popen(["cloudflared", "tunnel", "--url", "http://localhost:8081"], stdout=log_fb, stderr=subprocess.STDOUT)

    time.sleep(10)

    url_gotty = extrair_link("/data/data/com.termux/files/home/cf_gotty.log")
    url_fb = extrair_link("/data/data/com.termux/files/home/cf_fb.log")

    try:
        enviar_email(url_gotty, url_fb)
    except Exception as e:
        print(f"Falha ao enviar e-mail: {e}")

    while proc_gotty.poll() is None and proc_fb.poll() is None:
        time.sleep(30)

    time.sleep(5)
