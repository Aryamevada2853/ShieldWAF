import logging
import itertools
from flask import Flask, request, render_template, redirect, url_for, jsonify
import re
import requests
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
app = Flask(__name__)



LOG_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "app.log"
)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# Simulated database of malicious IP addresses
malicious_ips = set()

# Read malicious payloads from file
malicious_payloads = []
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "malicious_payload.txt"), "r", encoding="utf-8") as f:
    for line in f:
        malicious_payloads.append(re.escape(line.strip()))

# Generate all combinations of lowercase and uppercase letters for payloads
malicious_pattern = re.compile(r'\b(?:' + '|'.join(malicious_payloads) + r')\b', re.IGNORECASE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form.get('username', '')
        password = request.form.get('password', '')

        ip_address = request.remote_addr
        user_agent = request.headers.get('User-Agent', '')

        # Do not include passwords in request_data
        request_data = f"Username: {username}"

        if is_request_malicious(ip_address, user_agent, request_data):
            log_malicious_request(
                ip_address,
                user_agent,
                request_data
            )
            return render_template("403.html"), 403

        if username == "admin" and password == "admin123":
            return redirect(url_for('index'))

        return "Invalid credentials", 401

    return render_template("login.html")

@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact_form():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        ip_address = request.remote_addr
        user_agent = request.headers.get('User-Agent', '')
        request_data = name + email + message

        if is_request_malicious(ip_address, user_agent, request_data):
            log_malicious_request(ip_address, user_agent, request_data)
            return render_template("403.html")

        log_valid_request(ip_address, user_agent, request_data)
        return jsonify(message='Your request has been received successfully.')
    
    return render_template("contact.html")
@app.route('/team')
@app.route('/team.html')
def team():
    return render_template('team.html')


@app.route('/service')
@app.route('/service.html')
def service():
    return render_template('service.html')


@app.route('/why')
@app.route('/why.html')
def why():
    return render_template('why.html')
def is_request_malicious(ip_address, user_agent, request_data):
    # Check if the IP address or user agent matches any known malicious patterns
    if ip_address in malicious_ips:
        return True

    # Check for malicious payloads in the request data
    if malicious_pattern.search(request_data):
        print(request_data)
        print(malicious_pattern)
        return True

    return False

def log_malicious_request(ip_address, user_agent, request_data):
    # Log that malicious request
    logging.warning(f'Malicious request from IP: {ip_address}, User-Agent: {user_agent}')
    alert_message = f"Malicious request from IP: {ip_address}, User-Agent: {user_agent}, Data: {request_data}"
    send_telegram_message(alert_message)
    logging.warning(f'Request Data: {request_data}')

def log_valid_request(ip_address, user_agent, request_data):
    logging.info(f'Valid request from IP: {ip_address}, User-Agent: {user_agent}')
    logging.info(f'Request Data: {request_data}')

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True,port=5555)
