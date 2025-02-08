# Hash format must be in byte. 
#import bcrypt: Implementeres senere
#import hashlib: Implementeres senere
from flask import Flask, render_template_string, request

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
        if name and email and password:
            members.append({'name': name, 'email': email, 'password': password})
            message = f"Member {name} registered successfully!"
            print ("Number of members: ",len(members))
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

