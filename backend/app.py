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