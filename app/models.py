from . import db
from datetime import datetime

class LoginAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    user_agent = db.Column(db.String(300))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    flagged = db.Column(db.String(100), default="Normal")
    timestamp = db.Column(db.DateTime,default=datetime.utcnow)