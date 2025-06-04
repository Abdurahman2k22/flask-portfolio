from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flashing success messages

# Route for each page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route to handle form submission
@app.route('/send', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Compose the message
    subject = f'Portfolio Contact from {name}'
    body = f"From: {name} <{email}>\n\n{message}"
    
    # Email credentials (use environment variables in real deployment)
    sender_email = 'abdulrahmanama007@gmail.com'
    sender_password = 'jgerfkixaivofcje'
    receiver_email = 'abdulrahmanama007@gmail.com'

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{body}")
        flash("Message sent successfully!", "success")
    except Exception as e:
        print("Error:", e)
        flash("Failed to send message. Please try again.", "danger")

    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)