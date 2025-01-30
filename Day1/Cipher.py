# 1. Caesar Cipher Encryption Function
letters = 'abcdefghijklmnopqrstuvwxyz'
def caeser_cipher(text, shift):
    encrypted_text =""
    for letter in text:
        letter = letter.lower()
        if not letter == '':
            index = letters.find(letter)
            if index == -1:
                encrypted_text += letter
            else:
                new_index = index + shift
                if new_index >= 26:
                    new_index -=26
                encrypted_text += letters[new_index]
    return encrypted_text

# 1.1. Decryption Function
def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        letter = letter.lower()
        if not letter == '':
            index = letters.find(letter)
            if index == -1:
                decrypted_text += letter
            else:
                new_index = (index - shift) % 26
                decrypted_text += letters[new_index]
    return decrypted_text

# 2. Vigenère Cipher Encryption Function
def vigenere_cipher(text, keyword):
    encrypted_text = ""
    keyword_repeated = ""
    keyword_length = len(keyword)
    text_length = len(text)
    
    for i in range(text_length):
        keyword_repeated += keyword[i % keyword_length]
    
    for i in range(text_length):
        letter = text[i].lower()
        if letter in letters:
            P_i = letters.find(letter)
            K_i = letters.find(keyword_repeated[i].lower())
            C_i = (P_i + K_i) % 26
            encrypted_text += letters[C_i]
        else:
            encrypted_text += letter
    
    return encrypted_text

# 2.1. Vigenère Cipher Decryption Function
def vigenere_decrypt(text, keyword):
    decrypted_text = ""
    keyword_repeated = ""
    keyword_length = len(keyword)
    text_length = len(text)
    
    for i in range(text_length):
        keyword_repeated += keyword[i % keyword_length]
    
    for i in range(text_length):
        letter = text[i].lower()
        if letter in letters:
            P_i = letters.find(letter)
            K_i = letters.find(keyword_repeated[i].lower())
            C_i = (P_i - K_i + 26) % 26
            decrypted_text += letters[C_i]
        else:
            decrypted_text += letter
    return decrypted_text




#===============================NOT IMPORTANT======================================================
from flask import Flask, render_template_string, request

app = Flask(__name__)

#==========================ROUTE HANDLER=================================================
@app.route('/', methods=['GET', 'POST'])
def home():
    encrypted_output = None
    decrypted_output = None
    vigenere_encrypted_output = None
    vigenere_decrypted_output = None

    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        vigenere_user_input = request.form.get('vigenere_user_input', '')
        shift = int(request.form.get('shift', 3))
        keyword = request.form.get('keyword', '')
        action = request.form.get('action', '')

        if action == 'encrypt':
            encrypted_output = caeser_cipher(user_input, shift)
        elif action == 'decrypt':
            decrypted_output = decrypt(user_input, shift)
        elif action == 'vigenere_encrypt':
            vigenere_encrypted_output = vigenere_cipher(vigenere_user_input, keyword)
        elif action == 'vigenere_decrypt':
            vigenere_decrypted_output = vigenere_decrypt(vigenere_user_input, keyword)

    return render_template_string(HTML_TEMPLATE, encrypted_output=encrypted_output, decrypted_output=decrypted_output, vigenere_encrypted_output=vigenere_encrypted_output, vigenere_decrypted_output=vigenere_decrypted_output)


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Tiny Web App with Caesar and Vigenère Cipher</title>
</head>
<body>
    <h1>Encryption and Decryption App</h1>
    
    <!-- Caesar Cipher Encryption Form -->
    <h2>Encrypt Text with Caesar Cipher</h2>
    <form method="POST">
        <label for="encrypt_input">Enter text to encrypt:</label>
        <input type="text" id="encrypt_input" name="user_input" required>
        <br>
        <label for="shift">Number of shifts (integer):</label>
        <input type="number" id="shift" name="shift" required>
        <br>
        <button type="submit" name="action" value="encrypt">Encrypt</button>
    </form>
    {% if encrypted_output %}
    <h2>Encrypted Output:</h2>
    <p>{{ encrypted_output }}</p>
    {% endif %}
    
    <!-- Caesar Cipher Decryption Form -->
    <h2>Decrypt Text with Caesar Cipher</h2>
    <form method="POST">
        <label for="decrypt_input">Enter text to decrypt:</label>
        <input type="text" id="decrypt_input" name="user_input" required>
        <br>
        <label for="shift">Number of shifts (integer):</label>
        <input type="number" id="shift" name="shift" required>
        <br>
        <button type="submit" name="action" value="decrypt">Decrypt</button>
    </form>
    {% if decrypted_output %}
    <h2>Decrypted Output:</h2>
    <p>{{ decrypted_output }}</p>
    {% endif %}
    
    <!-- Vigenère Cipher Encryption Form -->
    <h2>Encrypt Text with Vigenère Cipher</h2>
    <form method="POST">
        <label for="vigenere_encrypt_input">Enter text to encrypt:</label>
        <input type="text" id="vigenere_encrypt_input" name="vigenere_user_input" required>
        <br>
        <label for="keyword">Keyword:</label>
        <input type="text" id="keyword" name="keyword" required>
        <br>
        <button type="submit" name="action" value="vigenere_encrypt">Encrypt</button>
    </form>
    {% if vigenere_encrypted_output %}
    <h2>Encrypted Output:</h2>
    <p>{{ vigenere_encrypted_output }}</p>
    {% endif %}
    
    <!-- Vigenère Cipher Decryption Form -->
    <h2>Decrypt Text with Vigenère Cipher</h2>
    <form method="POST">
        <label for="vigenere_decrypt_input">Enter text to decrypt:</label>
        <input type="text" id="vigenere_decrypt_input" name="vigenere_user_input" required>
        <br>
        <label for="keyword">Keyword:</label>
        <input type="text" id="keyword" name="keyword" required>
        <br>
        <button type="submit" name="action" value="vigenere_decrypt">Decrypt</button>
    </form>
    {% if vigenere_decrypted_output %}
    <h2>Decrypted Output:</h2>
    <p>{{ vigenere_decrypted_output }}</p>
    {% endif %}
</body>
</html>
"""



if __name__ == '__main__':
    app.run(debug=True) 


"""
ALTERNATIVE FUNCTIONS WITH BUILT IN ARRAY: 
- must revise string manipulation. 
def encrypt(text, shift=3):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char islower() else ord('A')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text
    
    def decrypt(text, shift):
    dec_text = ""
    for char in text:
        base = ord("a") if char islower() else ord("A")
        dec_char = (ord(char)- base - shift) % 26
        dec_text += dec_char
    return dec_text


    ***********************VIGENEERE******************************
    # 2. Vigenère Cipher Encryption Function
def vigenere_cipher(text, keyword):
    encrypted_text = ""
    keyword_repeated = ""
    keyword_length = len(keyword)
    text_length = len(text)
    
    for i in range(text_length):
        keyword_repeated += keyword[i % keyword_length]
    
    for i in range(text_length):
        letter = text[i].lower()
        if letter in letters:
            text_index = letters.find(letter)
            keyword_index = letters.find(keyword_repeated[i].lower())
            new_index = (text_index + keyword_index) % 26
            encrypted_text += letters[new_index]
        else:
            encrypted_text += letter
    
    return encrypted_text

# 2.1. Vigenère Cipher Decryption Function
def vigenere_decrypt(text, keyword):
    decrypted_text = ""
    keyword_repeated = ""
    keyword_length = len(keyword)
    text_length = len(text)
    
    for i in range(text_length):
        keyword_repeated += keyword[i % keyword_length]
    
    for i in range(text_length):
        letter = text[i].lower()
        if letter in letters:
            text_index = letters.find(letter)
            keyword_index = letters.find(keyword_repeated[i].lower())
            new_index = (text_index - keyword_index) % 26
            decrypted_text += letters[new_index]
        else:
            decrypted_text += letter
    
    return decrypted_text

    """