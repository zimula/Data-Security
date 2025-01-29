# INTRO TO ENCRYPTION
1. Caeser cipher: Works by substituting letters using integers. The integer represents a the position of in the alphabet.  
    1.1. Can be solved using a simple maths like so: 

        i. Encryption
        En(x) = (x + n) mod 26
        - mod: to ensure that if the result is greater than 26, it starts from the beginning.
        - Divides by 26 and returns the remainder (new position) 

        ii. Decryption
        En(x) = (x-n) mod 26
    
        ***Requires to know the cipher number/shift. 

2. (Must Revise)Vigenere Cipher: Takes Caeser a step further by using a different number value for each letter. 

        i. The math is complicated. 
        ii. Includes a key. 
        iii. Each letter of the plain text has a different caeser cipher. 
        iv. an example: 
            - plain txt: tool (positions: 0,1,2,3) 
            - key: dead (positions: 3, 4,0, )j