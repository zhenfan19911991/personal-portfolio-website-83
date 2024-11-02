from flask import Flask, render_template, request
import os
import smtplib

MY_EMAIL = os.getenv('MY_EMAIL')
MY_PASSWORD = os.getenv('GMAIL_PASS')

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        contents = (f"Name: {request.form['name']}\nEmail: {request.form['email']}\nSubject: {request.form['subject']}\n"
                    f"Message: {request.form['message']}")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:New Message\n\n{contents}"
            )
        return render_template('Thanks.html')
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5002)



