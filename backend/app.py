from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import os
import base64
from flask_mail import Mail, Message
from io import BytesIO
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import random
import string

app = Flask(__name__)
app.secret_key = os.urandom(24)
s = URLSafeTimedSerializer(app.secret_key) 

db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="",  
    database="CodeCrypt" 
)
cursor = db.cursor()

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		identifier = request.form['identifier']
		password = request.form['password']

		cursor.execute("SELECT * FROM users WHERE email = %s OR username = %s", (identifier, identifier))
		user = cursor.fetchone()

		if user:
			stored_hashed_password = user[4]
			if check_password_hash(stored_hashed_password, password):
				session['user_id'] = user[0]  
				session['username'] = user[3]  
                
				return redirect(url_for('homepage'))
			else:
				flash('Invalid email/username or password', 'danger')
		else:
			flash('Invalid email/username or password', 'danger')

	return render_template('login.html')