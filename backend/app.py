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
    database="seekreto" 
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test-db')
def test_db():
    try:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return jsonify(rows)
    except Exception as e:
        return f"Database error: {e}"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        email_exists = cursor.fetchone()

        if email_exists:
            flash('Email already registered. Enter a new one.', 'danger')
            return redirect(url_for('register'))

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        username_exists = cursor.fetchone()

        if username_exists:
            flash('Username already taken. Enter a new one.', 'danger')
            return redirect(url_for('register'))

        cursor.execute("SELECT user_id FROM users ORDER BY user_id DESC LIMIT 1")
        last_user = cursor.fetchone()

        if last_user:
            last_user_id = last_user[0]
            user_number = int(last_user_id.replace("CCUSER", "")) + 1
            new_user_id = f"CCUSER{user_number:04d}"
        else:
            new_user_id = "CCUSER0001"

        cursor.execute("INSERT INTO users (user_id, email, name, username, password) VALUES (%s, %s, %s, %s, %s)",
                       (new_user_id, email, name, username, hashed_password))
        db.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

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