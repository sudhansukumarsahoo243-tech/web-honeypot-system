import os
token=os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")
import requests
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import time
last_alert_time=0
COOLDOWN=60
from .models import LoginAttempt
from .detection import detect_attack
from . import db
def send_telegram_alert(message):
    global last_alert_time

    current_time = time.time()

    if current_time - last_alert_time < COOLDOWN:
        print("Cooldown active. Alert skipped.")
        return

    token = "8653606042:AAHztP3P7sZSDEBlm_I94pKsTRbxOvV74NU"
    chat_id = "5523320415"

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Telegram alert sent")
        last_alert_time = current_time
    else:
        print("Failed to send alert")

main = Blueprint('main', __name__)


@main.route('/')
def login():
    return render_template('login.html')


@main.route('/login', methods=['POST'])
def handle_login():
    ip = request.remote_addr
    username = request.form.get('username')
    password = request.form.get('password')
    user_agent = request.headers.get('User-Agent')

    flag = detect_attack(ip,username,user_agent)   # test ke liye hardcode

    if flag != "Normal":
        message = f"""
🚨 Honeypot Alert 🚨
IP: {ip}
Username: {username}
Status: {flag}
"""
        send_telegram_alert(message)

    attempt = LoginAttempt(
        ip_address=ip,
        username=username,
        password=password,
        user_agent=user_agent,
        flagged=flag
    )

    db.session.add(attempt)
    db.session.commit()

    print("SAVED:", ip, username)

    return redirect(url_for('main.login'))


@main.route('/dashboard')
def dashboard():
    attempts = LoginAttempt.query.all()

    total_attempts = len(attempts)
    unique_ips = len(set([a.ip_address for a in attempts]))
    brute_force_count = len([a for a in attempts if a.flagged != "Normal"])

    # Threat Logic
    if brute_force_count > 10:
        threat_level = "CRITICAL"
    elif brute_force_count > 5:
        threat_level = "HIGH"
    elif brute_force_count > 2:
        threat_level = "MEDIUM"
    else:
        threat_level = "LOW"

    return render_template(
        'dashboard.html',
        attempts=attempts,
        total_attempts=total_attempts,
        unique_ips=unique_ips,
        brute_force_count=brute_force_count,
        threat_level=threat_level
    )

@main.route('/api/metrics')
def api_metrics():
    attempts = LoginAttempt.query.all()

    total_attempts = len(attempts)
    unique_ips = len(set([a.ip_address for a in attempts]))
    suspicious = len([a for a in attempts if a.flagged != "Normal"])

    return jsonify({
        "total_attempts": total_attempts,
        "unique_ips": unique_ips,
        "suspicious": suspicious
    })