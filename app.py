import os
import sys
import webbrowser
import threading
import time
from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    city = data.get('city')
    services = ', '.join(data.get('services', []))  # Converte lista de serviços em string

    # Enviar notificação por e-mail
    send_email(name, email, message, city, services)

    return jsonify({'status': 'Message received'})

def load_config_from_file(file_name='config.txt'):
    # Determine the base directory where the executable is running
    if hasattr(sys, '_MEIPASS'):
        # Running in a PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running in a normal Python environment
        base_path = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(base_path, file_name)

    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config[key] = value
    return config

# Carregar configurações do arquivo
config = load_config_from_file()
EMAIL_USER = config.get('EMAIL_USER')
EMAIL_PASS = config.get('EMAIL_PASS')

def send_email(name, email, message, city, services):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = 'testedeautomacao4@gmail.com'
    msg['Subject'] = 'Novo Contato Recebido'

    email_body = (f'Novo contato recebido:\n\n'
                  f'Nome: {name}\n'
                  f'E-mail: {email}\n'
                  f'Mensagem: {message}\n'
                  f'Cidade: {city}\n'
                  f'Serviços de Interesse: {services}')
    
    msg.attach(MIMEText(email_body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
    except Exception as e:
        print(f'Error sending email: {e}')

def run_flask_app():
    print("Starting Flask app...")
    app.run(port=5000)

if __name__ == '__main__':
    # Start Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    # Allow the server to start up
    time.sleep(5)  # Increase sleep time to ensure the server has started

    # Open the default web browser to the Flask app URL in a new window
    print("Opening browser...")
    webbrowser.open('http://127.0.0.1:5000', new=1)
