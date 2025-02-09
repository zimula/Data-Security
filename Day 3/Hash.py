# Hash format must be in byte. 
#import bcrypt: Implementeres senere
#import hashlib: Implementeres senere
import bcrypt
from flask import Flask, render_template_string, request


#hasing password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

#Checkig password. Rewrite to fetch hashed password from database.
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)





app = Flask(__name__)


# Will change it to a database table later. 
members = [] 

@app.route('/', methods=['GET', 'POST'])
def register():
    message = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        hashed = hash_password(password)
        if name and email and password:
            members.append({'name': name, 'email': email, 'password': password})
            #confirm list and hashed password. 
            message = f"Member {name} registered successfully!"
            print ("Number of members: ",len(members), "password: ", hashed)
            print("Reversed: ", check_password(password, hashed ))
        else:
            message = "Please enter name, email, and password."
    return render_template_string(HTML_TEMPLATE, message=message)





HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Member Registration</title>
</head>
<body>
    <h1>Register a New Member</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <button type="submit">Register</button>
    </form>
    {% if message %}
    <h2>{{ message }}</h2>
    {% endif %}
</body>
</html>
"""
if __name__ == '__main__':
    app.run(debug=True, port=5001)

