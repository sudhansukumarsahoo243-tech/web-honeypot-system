from datetime import datetime, timedelta
from .models import LoginAttempt
def detect_attack(ip, username, user_agent):
    now = datetime.utcnow()

    # Rule 1
    recent_time = now - timedelta(seconds=30)

    rapid_attempts = LoginAttempt.query.filter(
        LoginAttempt.ip_address == ip,
        LoginAttempt.timestamp >= recent_time
    ).count()

    if rapid_attempts >= 5:
        return "Brute Force (Rapid Attempts)"

    # Rule 2
    recent_time = now - timedelta(seconds=60)

    username_count = LoginAttempt.query.filter(
        LoginAttempt.ip_address == ip,
        LoginAttempt.timestamp >= recent_time
    ).distinct(LoginAttempt.username).count()

    if username_count >= 5:
        return "Credential Stuffing"

    # Rule 3
    suspicious_agents = ["curl", "bot", "python", "wget"]

    for agent in suspicious_agents:
        if agent in user_agent.lower():
            return "Suspicious Bot Activity"

    return "Normal"