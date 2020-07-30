# Atlantis NET website
Web application for Atlantis NET built with Bootstrap 4, HTML 5 and Flask 1.1.2


# How to build and run (for Windows), assuming you have Python installed?

1. In the project's folder open PowerShell (shift + right mouse button) and execute the following commands:

* py -3 -m venv venv
* venv\Scripts\activate
* pip install -r requirements.txt
* set FLASK_APP=app.py
* flask run

2. The app should be running on localhost - 127.0.0.1:5000

# /contacts and /report_a problem aren't working?

That's because you need to change a few things.

1. In creds.py use a real email account and a password (those will be our sender credentials). # example: email:peter.1999@gmail.com, password:peter1999

2. In app.py change this email (receiving_email@example.com) in "recipients=['receiving_email@example.com'])" to whatever email address you want the messages to arrive at. # example: email:joe.2001@gmail.com
