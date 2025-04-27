import os
from flask import Flask, render_template, request,redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Configurações do remetente
email_remetente = os.getenv('EMAIL_REMENTENTE')
senha = os.getenv('EMAIL_SENHA')

app = Flask(__name__)

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/submit_consultoria', methods=['POST'])
def submit_consultoria():
    name = request.form['name']
    email = request.form['email']
    personal_phone = request.form['personal_phone']
    company = request.form['company']
    segmento = request.form['cf_qual_o_segmento_da_sua_empresa']
    cargo = request.form['cf_qual_e_o_seu_cargo_na_empresa']
    faturamento = request.form['cf_faturamento_mensal_da_empresa']
    
    # Configurações do destinatário
    email_destinatario = [email,
                          'samuelsoares177778@gmail.com']
    assunto = 'Novo lEAD do SITE'
    mensagem = f'''Olá! Um lead acabou de entrar em contato 😎
    nome : {name}
    email : {email}
    personal_phone : {personal_phone}
    segmento : {segmento}
    cargo : {cargo}
    faturamento : {faturamento}
    '''
    
    print(mensagem)
    # Montar o e-mail
    msg = MIMEMultipart()
    msg['From'] = email_remetente
    msg['To'] = ", ".join(email_destinatario)
    msg['Subject'] = assunto
    
    msg.attach(MIMEText(mensagem, 'plain'))
    
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(email_remetente, senha)
        texto = msg.as_string()
        servidor.sendmail(email_remetente, email_destinatario, texto)
        servidor.quit()
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')
    
    return  redirect(url_for('index'))

@app.route('/social_media')
def social_media():
    return  render_template('social_media.html')

@app.route('/branding')
def branding():
    return  render_template('branding.html')

@app.route('/web_services')
def web_services():
    return  render_template('branding.html')

@app.route('/design_grafico')
def design_grafico():
    return  render_template('web_services.html')

@app.route('/gestaodeanuncios')
def gestaodeanuncios():
    return  render_template('web_services.html')\
        
if __name__ == '__main__':
    app.run(debug=True, port=8080)