""" 
NOTES: 
1: Caeser cipher:
Works by substituting letters using integers. The integer represents a the position of in the alphabet.  
1.1: Can be solved using a simple maths like so: 

    i. Encryption
        En(x) = (x + n) mod 26
        - mod: to ensure that if the result is greater than 26, it starts from the beginning.
        - Divides by 26 and returns the remainder (new position) 

    ii. Decryption
        En(x) = (x-n) mod 26
    
    ***Requires to know the cipher number/shift. 

2. Vigenere Cipher: Takes Caeser a step further by using a different number value 
    for each letter. 

    i. The math is complicated. 
    ii. Includes a key. 
    iii. Each letter of the plain text has a different caeser cipher. 
    iv. an example: 
            - plain txt: tool (positions: 0,1,2,3) 
            - key: dead (positions: 3, 4,0, )j


"""
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Caesar Cipher Encryption Function
def caesar_cipher(text, shift=3):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text



@app.route('/', methods=['GET', 'POST'])
def home():
    output = None
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        shift = int(request.form.get('shift', 3))  # Get shift value from form
        encrypted_text = caesar_cipher(user_input, shift)  # Encrypt the input
        output = f'Original: {user_input}<br>Encrypted: {encrypted_text}'
    return render_template_string(HTML_TEMPLATE, output=output)


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Tiny Web App with Caesar Cipher</title>
</head>
<body>
    <h1>Welcome to the Tiny Web App!</h1>
    <form method="POST">
        <label for="user_input">Enter something:</label>
        <input type="text" id="user_input" name="user_input" required>
        <br>
        <label for="shift">Number of shifts (integer):</label>
        <input type="number" id="shift" name="shift" required>
        <br>
        <button type="submit">Encrypt</button>
    </form>
    {% if output %}
    <h2>Encrypted Output:</h2>
    <p>{{ output }}</p>
    {% endif %}
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True) 