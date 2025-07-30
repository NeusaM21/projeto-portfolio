import pandas as pd
import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do .env
load_dotenv()
EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA_DO_APP = os.getenv("SENHA_DO_APP")

# Carregar planilha de doadores
planilha = pd.read_excel("doadores.xlsx")
planilha.columns = planilha.columns.str.strip()  # Remove espaços das colunas

# Criar mensagem personalizada
def criar_mensagem(nome_completo):
    primeiro_nome = nome_completo.split()[0]
    return f"""
Olá {primeiro_nome},

Primeiramente gostaríamos de agradecer toda a sua solidariedade.

A Nossa Instituição enfrenta uma crise grave e estamos desesperados. Estamos sem comida e, mais preocupante, sem os medicamentos de alto custo indispensáveis para nossas crianças. Elas não podem ficar sem esses remédios, especialmente as que lutam contra o câncer. A rede pública não tem fornecido os medicamentos necessários. Por favor, ajude-nos a salvar essas vidas preciosas.

👶 As nossas crianças podem contar com a sua ajuda para o auxílio.

Segue abaixo o Pix do Instituto para a transferência 👇

👉 Doe agora: iaesperancaevida@gmail.com

Muito obrigada, fique com Deus 🙏

Com gratidão,  
Equipe Instituto Esperança e Vida
"""

# Função para enviar e-mail
def enviar_email(destinatario, assunto, corpo):
    mensagem = EmailMessage()
    mensagem["Subject"] = assunto
    mensagem["From"] = EMAIL_REMETENTE
    mensagem["To"] = destinatario
    mensagem["Bcc"] = EMAIL_REMETENTE  # Envia cópia oculta para você
    mensagem.set_content(corpo)

    contexto = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as servidor:
        servidor.login(EMAIL_REMETENTE, SENHA_DO_APP)
        servidor.send_message(mensagem)

# Enviar e-mails para todos da planilha
for index, linha in planilha.iterrows():
    try:
        nome = linha["Nome Completo"]
        email = linha["Email"]
        corpo = criar_mensagem(nome)
        enviar_email(email, "Ajude o Instituto Esperança e Vida 💖", corpo)
        print(f"✅ E-mail enviado com sucesso para {nome} - {email}")
    except Exception as e:
        print(f"❌ Erro ao enviar para {email}: {e}")
