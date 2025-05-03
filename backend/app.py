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

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')
app.secret_key = os.urandom(24)
s = URLSafeTimedSerializer(app.secret_key) 

db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="admin",  
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

@app.route('/homepage')
def homepage():
    if 'user_id' not in session:
        return redirect(url_for('login')) 

    user_id = session['user_id']
    username = session['username']

    cursor.execute(
        "SELECT email FROM users WHERE user_id = %s", (user_id,)
    )
    result = cursor.fetchone()

    if result:  
        email = result[0]  
    else:
        email = 'Error fetching.'  

    cursor.execute(
        "SELECT name FROM users WHERE user_id = %s", (user_id,)
    )
    result_name = cursor.fetchone()

    if result_name:  
        name = result_name[0]  
    else:
        name = 'Error fetching.' 

    cursor.execute(
        "SELECT crypt_id FROM favorites WHERE user_id = %s", (user_id,)
    )
    favorites = cursor.fetchall()

    favorite_ciphers = {favorite[0] for favorite in favorites}
    
    return render_template('homepage.html', username=username, email=email, name=name, 
                          user_id=user_id, favorite_ciphers=favorite_ciphers)

@app.route('/favorites')
def favorites():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    username = session.get('username', 'Guest')
    
    cursor.execute("SELECT email, name FROM users WHERE user_id = %s", (user_id,))
    user_details = cursor.fetchone()
    
    if user_details:
        email = user_details[0]
        name = user_details[1]
    else:
        email = 'Error fetching'
        name = 'Error fetching'
    
    cursor.execute("""
        SELECT 
            c.type_of_tool, 
            f.description, 
            f.icon_text, 
            f.href
        FROM 
            favorites f
        JOIN 
            ciphers c ON f.crypt_id = c.crypt_id
        WHERE 
            f.user_id = %s
    """, (user_id,))
    
    favorites = cursor.fetchall()
    
    return render_template('favorites.html', favorites=favorites, username=username, email=email, name=name)

@app.route('/toggle-favorite', methods=['POST'])
def toggle_favorite():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Not logged in"}), 401
    
    data = request.get_json()
    tool_name = data.get('tool_name')
    description = data.get('description')
    icon_text = data.get('icon_text')
    is_favorited = data.get('is_favorited')
    user_id = session['user_id']
    
    tool_url = "/" + tool_name.lower().replace(" ", "").replace("cipher", "").strip()
    
    cursor.execute("SELECT crypt_id FROM ciphers WHERE type_of_tool = %s", (tool_name,))
    crypt_id_result = cursor.fetchone()
    
    if not crypt_id_result:
        return jsonify({"success": False, "message": "Cipher not found"}), 404
    
    crypt_id = crypt_id_result[0]
    
    if is_favorited:
        try:
            cursor.execute("SELECT MAX(fav_id) FROM favorites")
            max_fav_id = cursor.fetchone()[0]
            
            if max_fav_id:
                fav_num = int(max_fav_id[3:]) + 1
                new_fav_id = f"FAV{fav_num:04d}"
            else:
                new_fav_id = "FAV0001"
                
            cursor.execute("""
                INSERT INTO favorites 
                (fav_id, user_id, crypt_id, description, icon_text, href) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (new_fav_id, user_id, crypt_id, description, icon_text, tool_url))
            db.commit()
            return jsonify({"success": True, "message": "Added to favorites"})
        except mysql.connector.Error as e:
            db.rollback()
            return jsonify({"success": False, "message": f"Database error: {str(e)}"}), 500
    else:
        try:
            cursor.execute("""
                DELETE FROM favorites 
                WHERE user_id = %s AND crypt_id = %s
            """, (user_id, crypt_id))
            db.commit()
            
            if cursor.rowcount > 0:
                if request.referrer and 'favorites' in request.referrer:
                    return jsonify({"success": True, "message": "Removed from favorites", "reload": True})
                return jsonify({"success": True, "message": "Removed from favorites"})
            else:
                return jsonify({"success": False, "message": "Favorite not found"}), 404
        except mysql.connector.Error as e:
            db.rollback()
            return jsonify({"success": False, "message": f"Database error: {str(e)}"}), 500

@app.route('/contacts')
def contacts():
    email = None  
    name = None  
    username = None 
    user_id = session.get('user_id')  

    if user_id:
        username = session.get('username', 'Guest')

        cursor.execute("SELECT email FROM users WHERE user_id = %s", (user_id,))
        email_result = cursor.fetchone()
        if email_result:
            email = email_result[0]
        else:
            email = 'Error fetching.'

        cursor.execute("SELECT name FROM users WHERE user_id = %s", (user_id,))
        name_result = cursor.fetchone()
        if name_result:
            name = name_result[0]
        else:
            name = 'Error fetching.'

    if 'user_id' not in session:
        return redirect(url_for('login'))

    return render_template('contacts.html', email=email, username=username, name=name)

@app.route('/allhistory', methods=['GET'])
def all_history():
   
    email = None  
    name = None  
    username = None 
    user_id = session.get('user_id')  

    if user_id:
        username = session.get('username', 'Guest')

        
        cursor.execute("SELECT email FROM users WHERE user_id = %s", (user_id,))
        email_result = cursor.fetchone()
        if email_result:
            email = email_result[0]
        else:
            email = 'Error fetching.'

        cursor.execute("SELECT name FROM users WHERE user_id = %s", (user_id,))
        name_result = cursor.fetchone()
        if name_result:
            name = name_result[0]
        else:
            name = 'Error fetching.'

    if not user_id:
        flash("Please log in to view your history.")
        return redirect(url_for('login'))


    cipher_type = request.args.get('cipher_type', '')
    sort_order = request.args.get('sort_order', 'recent')  

    cipher_filter = ""
    if cipher_type:
        cipher_filter = "AND c.type_of_tool = %s"
    
   
    order_by = "ORDER BY h.date_time DESC" if sort_order == 'recent' else "ORDER BY h.date_time ASC"

    
    query = f'''
    SELECT h.date_time, h.crypt_id, h.mode_id, h.input, h.output, h.shift, h.key, h.a_value, h.b_value, h.rail, c.type_of_tool, co.type_of_conversion
    FROM history h
    JOIN ciphers c ON h.crypt_id = c.crypt_id
    JOIN conversion co ON h.mode_id = co.mode_id
    WHERE h.user_id = %s {cipher_filter}
    {order_by}
    '''
    
   
    params = (user_id,)
    if cipher_type:
        params += (cipher_type,)
    
    cursor.execute(query, params)
    history_records = cursor.fetchall()


    history = []
    for record in history_records:
        conversion_type = record[10]
        mode_name = record[11]

        history_entry = {
            'timestamp': record[0],
            'conversion_type': conversion_type,
            'mode_type': mode_name,
            'input': record[3],
            'output': record[4]
        }

        if record[5] is not None:
            history_entry['shift'] = record[5]
        if record[6] and record[6] != 'n/a':
            history_entry['key'] = record[6]
        if record[7] is not None:
            history_entry['a_value'] = record[7]
        if record[8] is not None:
            history_entry['b_value'] = record[8]
        if record[9] is not None:
            history_entry['rail'] = record[9]

        
        history.append(history_entry)

   
    return render_template('allhistory.html', history=history, email=email, username=username, name=name)

def atbash_cipher(text):
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reversed_alphabet_upper = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    reversed_alphabet_lower = 'zyxwvutsrqponmlkjihgfedcba'
    result = ''

    for char in text:
        if char in alphabet_upper:
            index = alphabet_upper.index(char)
            converted_char = reversed_alphabet_upper[index]
            result += converted_char
        elif char in alphabet_lower:
            index = alphabet_lower.index(char)
            converted_char = reversed_alphabet_lower[index]
            result += converted_char
        else:
            result += char
    return result


@app.route('/atbash', methods=['GET', 'POST'])
def atbash():
    result = ""
    email = None  
    name = None  
    username = None 
    user_id = session.get('user_id')  

    if user_id:
        username = session.get('username', 'Guest')

        cursor.execute("SELECT email FROM users WHERE user_id = %s", (user_id,))
        email_result = cursor.fetchone()
        if email_result:
            email = email_result[0]
        else:
            email = 'Error fetching.'

        cursor.execute("SELECT name FROM users WHERE user_id = %s", (user_id,))
        name_result = cursor.fetchone()
        if name_result:
            name = name_result[0]
        else:
            name = 'Error fetching.'

    if request.method == 'POST':
       
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('login'))
        
       
        mode = request.form.get('mode')
        
       
        if not mode:
            flash("Please select an option before entering text.")
            return redirect(url_for('atbash'))  

        
        if mode == 'toCipher':
            mode_id = 'Text to Atbash Cipher'
        elif mode == 'toText':
            mode_id = 'Atbash Cipher to Text'

        text = request.form['input_text']

        result = atbash_cipher(text)

        crypt_id = 'Atbash Cipher' 
     
        insert_history(user_id, crypt_id, mode_id, None, None, None, None, None, text, result)

    return render_template('atbash.html', result=result, email=email, username=username, name=name, user_id=user_id)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
