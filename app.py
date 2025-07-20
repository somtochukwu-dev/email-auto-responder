from flask import Flask, request, render_template_string
import smtplib
from email.message import EmailMessage
import os  # Added to use environment variables

app = Flask(__name__)

# Replace these with environment variables for safety
EMAIL_ADDRESS = os.getenv('EMAIL_USER')  # Set your email in environment variable
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')  # Set your app password in environment variable

form_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact GoStreamlined</title>
    <style>
        body { background-color: #f0f2f5; font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .form-container { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); width: 90%; max-width: 400px; text-align: center; }
        .form-container h1 { color: #0044cc; margin-bottom: 20px; }
        .form-group { text-align: left; margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 8px; font-weight: bold; }
        .form-group input { width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; font-size: 1em; }
        .form-group input:focus { border-color: #0044cc; outline: none; }
        .submit-btn { background-color: #0044cc; color: white; padding: 15px; border: none; border-radius: 8px; width: 100%; font-size: 1em; cursor: pointer; transition: background-color 0.3s ease; }
        .submit-btn:hover { background-color: #003399; }
    </style>
</head>
<body>
<div class="form-container">
    <h1>Contact Us</h1>
    <form method="POST" action="/">
        <div class="form-group">
            <label>Name</label>
            <input type="text" name="name" required>
        </div>
        <div class="form-group">
            <label>Email</label>
            <input type="email" name="email" required>
        </div>
        <button type="submit" class="submit-btn">Send Message</button>
    </form>
</div>
</body>
</html>
'''

success_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Thank You</title>
</head>
<body style="display:flex;justify-content:center;align-items:center;height:100vh;background:#f0f2f5;font-family:Arial;">
  <div style="text-align:center;">
    <h1 style="color:#0044cc;">Thanks for contacting us!</h1>
    <p>We'll respond to your message shortly.</p>
  </div>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        user_name = request.form["name"]
        user_email = request.form["email"]
        send_auto_response(user_email, user_name)
        return render_template_string(success_html)
    return render_template_string(form_html)

def send_auto_response(user_email, user_name):
    msg = EmailMessage()
    msg['Subject'] = 'Thanks for contacting GoStreamlined!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = user_email
    msg.set_content(f'''
    Hi {user_name},

    Thanks for reaching out to GoStreamlined! Your message has been received and we will respond shortly.

    Best,
    The GoStreamlined Team
    ''')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    app.run(debug=True)
