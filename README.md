📌 Web Honeypot System
A lightweight Flask-based web honeypot designed to detect and log malicious login attempts in real time. The system monitors suspicious activity such as brute-force attempts and sends instant Telegram alerts.
🚀 Features
Fake login interface to attract attackers
Brute-force detection logic
IP address logging
Username & password attempt capture
User-Agent tracking
Telegram real-time alerts
Alert cooldown protection
SQLite database logging
Environment variable based secret management
🛠 Tech Stack
Python
Flask
SQLAlchemy
SQLite
Requests
python-dotenv
Telegram Bot API
📂 Project Structure
Copy code

web-honeypot-system/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── detection.py
│
├── static/
├── templates/
│
├── config.py
├── run.py
├── requirements.txt
└── .gitignore
⚙️ Installation & Setup
1️⃣ Clone the Repository
Copy code

git clone https://github.com/your-username/web-honeypot-system.git
cd web-honeypot-system
2️⃣ Create Virtual Environment
Copy code

python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
Copy code

pip install -r requirements.txt
4️⃣ Setup Environment Variables
Create a .env file in the root directory:
Copy code

BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
⚠ Never upload .env to GitHub.
5️⃣ Run the Application
Copy code

python run.py
Server will start on:
Copy code

http://127.0.0.1:5000
🔐 Detection Logic
The system detects suspicious activity such as:
Multiple login attempts in short time
Repeated username attempts
Brute-force behavior
When detected:
Attempt is stored in database
Telegram alert is sent
Cooldown prevents spam alerts
📊 Logged Data
Each attempt stores:
IP Address
Username entered
Password entered
User-Agent
Timestamp
Detection Flag
📡 Telegram Alert Format
Copy code

🚨 Honeypot Alert 🚨
IP: 192.168.1.10
Username: admin
Status: BRUTE_FORCE
🧠 Why This Project Matters
This project demonstrates:
Backend security logic implementation
Attack detection strategy
Secure secret handling
Real-time monitoring system
Defensive cybersecurity concepts
⚠ Disclaimer
This project is for educational and research purposes only.
Do not deploy publicly without proper security hardening.


## ▶ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/web-honeypot-system.git
cd web-honeypot-system
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / Mac**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory and add:

```
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
```

⚠ Do NOT commit this file to GitHub.

### 5️⃣ Run the Application
```bash
python run.py
```

The server will start at:
```
http://127.0.0.1:5000
```

Open this URL in your browser to access the honeypot login page.

---

## 🧪 Testing the Honeypot

Enter random credentials multiple times.
If brute-force behavior is detected:
- Attempt will be stored in database
- Telegram alert will be triggered
- Cooldown will prevent spam alerts




👨‍💻 Author
Sudhansu Kumar Sahoo
Cybersecurity Enthusiast
