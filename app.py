from flask import Flask, render_template, url_for, flash, request, redirect
from flask_wtf import FlaskForm
from forms import ContactForm
from flask_mail import Message, Mail
import os
import creds

# mail 

mail = Mail()

# app

app = Flask(__name__)

app.config['SECRET_KEY'] = creds.secret_key

# mail

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587 # 465
app.config["MAIL_SUPPRESS_SEND"] = False
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = creds.username
app.config["MAIL_PASSWORD"] = creds.password

mail.init_app(app)

# handle forms

@app.route('/contacts', methods=('GET', 'POST'))
def contacts():
	form = ContactForm()

	if request.method == 'POST':
		if form.validate() == False:
			flash('Моля, попълнете всички полета.')
			return render_template('contacts.html', form=form)
		else:
			msg = Message(form.subject.data, sender=creds.username, recipients=['receiving_email@example.com'])
			msg.body = """
			От: %s \nE-mail: %s\nСъобщение: %s
			""" % (form.name.data, form.email.data, form.message.data)
			mail.send(msg)
			
			return render_template("message_sent.html") 
	
	elif request.method == 'GET':
		return render_template('contacts.html', form=form)

@app.route("/report_a_problem", methods=('GET', 'POST'))
def report_a_problem():
	form = ContactForm()

	if request.method == 'POST':
		if form.validate() == False:
			flash('Моля, попълнете всички полета.')
			return render_template('report_a_problem.html', form=form)
		else:
			msg = Message(form.subject.data, sender=creds.username, recipients=['receiving_email@example.com'])
			msg.body = """
			От: %s \nE-mail: %s\nСъобщение: %s
			""" % (form.name.data, form.email.data, form.message.data)
			mail.send(msg)
			
			return render_template("message_sent.html") 
	
	elif request.method == 'GET':
		return render_template('report_a_problem.html', form=form)

# handle 404 error

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# handle app routes/pages

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/history")
def history():
	return render_template("history.html")

@app.route("/career")
def career():
	return render_template("career.html")

@app.route("/interfaces")
def interfaces():
	return render_template("interfaces.html")

@app.route("/lan_access")
def lan_access():
	return render_template("lan_access.html")

@app.route("/optical_connectivity")
def optical_connectivity():
	return render_template("optical_connectivity.html")

@app.route("/wireless_connectivity")
def wireless_connectivity():
	return render_template("wireless_connectivity.html")
	
@app.route("/television")
def television():
	return render_template("television.html")

@app.route("/cabling")
def cabling():
	return render_template("cabling.html")

@app.route("/software_support")
def software_support():
	return render_template("software_support.html")

@app.route("/web_design")
def web_design():
	return render_template("web_design.html")

@app.route("/hosting")
def hosting():
	return render_template("hosting.html")

@app.route("/cctv")
def cctv():
	return render_template("cctv.html")

@app.route("/prices_internet")
def prices_internet():
	return render_template("prices_internet.html")

@app.route("/prices_telephony")
def prices_telephony():
	return render_template("prices_telephony.html")

@app.route("/prices_trio_package")
def prices_trio_package():
	return render_template("prices_trio_package.html")

@app.route("/subscription_check")
def subscription_check():
	return render_template("subscription_check.html")

@app.route("/promotions_bonus_points")
def promotions_bonus_points():
	return render_template("promotions_bonus_points.html")

@app.route("/terms_and_conditions")
def terms_and_conditions():
	return render_template("terms_and_conditions.html")

#

if __name__=='__main__':
	app.run(ssl_context='adhoc')