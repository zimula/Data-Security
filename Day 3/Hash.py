#import bcrypt
import hashlib
from flask import Flask, render_template_string, request
from db import insert_member, get_all
from singleton import PasswordChecker
import os


#hasing password
""" def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed """
#Checkig password. Rewrite to fetch hashed password from database.
""" def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed) """

#Replacing bcrypt with hashlib.sha256
def hash_password(password):
    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed
#Checking password
def check_password(password, hashed):
    return hash_password(password) == hashed  

app = Flask(__name__)

#set file path for rockyou.txt(abspath makes sure the path is absolute)
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'rockyou.txt')
#feed passwordchecker with file path
password_checker = PasswordChecker(file_path)

# Will change it to a database table later. 
#members = [] 

@app.route('/', methods=['GET', 'POST'])
def register():
    message = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        hashed = hash_password(password)
        if name and email and password and check_password(password, hashed):
            #add passwordchecker conditional
            if password_checker.is_password_in_file(password):
                message = "Password is too common. Please choose a different password."
                return render_template_string(HTML_TEMPLATE, message=message)
            else:
                message = "Password is not in the list."

                #members.append({'name': name, 'email': email, 'password': password})
                insert_member(name, email, hashed)
                #confirm list and hashed password. 
                message = f"Member {name} registered successfully!"
                #print ("Number of members: ",len(members), "password: ", hashed)
                print("Reversed: ", check_password(password, hashed ))
        else:
            message = "Please enter name, email, and password."
    return render_template_string(HTML_TEMPLATE, message=message)


@app.route('/login', methods=['POST'])
def login():
    message = None
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '').strip()
    if email and password:
        members = get_all()
        member = next((m for m in members if m['email'] == email), None)
        if member and check_password(password, member['password']):
            return render_template_string(USER_TEMPLATE, name=member['name'], email=member['email'], users=members)
        else:
            message = "Invalid email or password."
    else:
        message = "Please enter email and password."
    return render_template_string(HTML_TEMPLATE, message=message)


#***************HTML Templates & Main guard*******************
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Member Registration and Login</title>
</head>
<body>
    <h1>Register a New Member</h1>
    <form method="POST" action="/">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <button type="submit">Register</button>
    </form>
    <h1>Login</h1>
    <form method="POST" action="/login">
        <label for="email">Email:</label>
        <input type="email" id="login_email" name="email" required>
        <label for="password">Password:</label>
        <input type="password" id="login_password" name="password" required>
        <button type="submit">Login</button>
    </form>
    {% if message %}
    <h2>{{ message }}</h2>
    {% endif %}
</body>
</html>
"""


USER_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>User Dashboard</title>
</head>
<body>
    <h1>Welcome, {{ name }}!</h1>
    <p>Email: {{ email }}</p>
    <h2>All Users</h2>
    <ul>
    {% for user in users %}
        <li>{{ user['id'] }} -- {{ user['name'] }} -- {{ user['email'] }} -- {{user['password']}}</li>
    {% endfor %}
    </ul>
    <a href="/">Logout</a>
</body>
</html>
"""
if __name__ == '__main__':
    app.run(debug=True, port=5001)

