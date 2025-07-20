# 📧 Email Auto-Responder

A lightweight Python Flask app that serves a contact form and automatically sends a personalised email response to users who submit their details.

Built for **GoStreamlined**, this project demonstrates how to integrate HTML forms with Python backend logic and secure email automation using SMTP.

---

## 🚀 Features

- 📄 Clean, responsive HTML contact form
- 📧 Automatic email replies using Gmail SMTP
- 🔒 Secure credentials via environment variables
- 🛠 Modular structure for easy customisation

---

## 🗂 Project Structure

email-auto-responder/
├── app.py              # Main Flask application
├── form.html           # Frontend contact form
├── send_email.py       # Email sending logic
└── README.md           # Project documentation

---

## ⚙️ Setup Instructions

1. **Clone the repository**
git clone https://github.com/yourusername/email-auto-responder.git
cd email-auto-responder

markdown
Copy code

2. **Install dependencies**
pip install flask

markdown
Copy code

3. **Set environment variables**
- Linux/Mac:
export EMAIL_USER="your_email@example.com"
export EMAIL_PASS="your_app_password"

diff
Copy code
- Windows:
set EMAIL_USER=your_email@example.com
set EMAIL_PASS=your_app_password

markdown
Copy code

4. **Run the app**
python app.py

yaml
Copy code
Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the contact form.

---

## 📧 Email Configuration

This app uses Gmail’s SMTP server:  
- Server: `smtp.gmail.com`  
- Port: `465` (SSL)  

For Gmail, use an App Password instead of your main password.

---

## 🔒 Security Note

✅ Do not hardcode credentials in Python files.  
✅ Always use environment variables or a `.env` file for sensitive data.

---

## ✨ Customisation

- Edit `form.html` to change the form’s design.  
- Adjust `send_email.py` to modify email content.  

---

## 👨‍💻 Author

Developed by Somtochukwu O 
