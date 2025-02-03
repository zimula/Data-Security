# INTRO TO ENCRYPTION

## Day 1: Classical ciphers/ basic encryption. 
1. Caesar cipher: Works by substituting letters using integers. The integer represents the position in the alphabet.
    1.1. Can be solved using simple math like so:

        i. Encryption:
        En(x) = (x + n) mod 26
        - mod: to ensure that if the result is greater than 25, it starts from the beginning.
        - Divides by 26 and returns the remainder (new position)

        ii. Decryption:
        Dn(x) = (x - n + 26) mod 26
        - Adding 26 ensures the result is non-negative

        ***Requires knowing the cipher number/shift.

2. Vigenère Cipher: Takes Caesar a step further by using a different number value for each letter based on a keyword.
    2.1. Can be solve using the following formula: 

        i. Encryption:
        C_i = (P_i + K_i) % 26
        - P_i: Position of the plaintext letter in the alphabet (A=0, B=1, ..., Z=25)
        - K_i: Position of the key letter in the alphabet (A=0, B=1, ..., Z=25)
        - C_i: Position of the ciphertext letter in the alphabet (A=0, B=1, ..., Z=25)

        ii. Decryption:
        P_i = (C_i - K_i + 26) % 26
        - Adding 26 ensures the result is non-negative

        iii. Each letter of the plaintext is encrypted using a different Caesar cipher based on the corresponding letter of the key.

        iv. Example:
       - Plaintext: TOOL (positions: 19, 14, 14, 11)
       - Key: DEAD (repeated to match plaintext length: DEAD, positions: 3, 4, 0, 3)
       - Encryption:
            T (19) + D (3) = W (22)
            O (14) + E (4) = S (18)
            O (14) + A (0) = O (14)
            - L (11) + D (3) = O (14)
            Ciphertext: WSOO

## Day 2: Encryption TLS.
3. Encryption

    i. Cornerstones
        - Confidenciality: Ability to restrict data/ parts of it to some users.  
        - Authenticity: Ability to confirm the the identity of both recipient and data source. 
        - Integrity: Confirm that data has not been interfered with during transfer. 
        - Non Repudiation:Data source must not be able to deny that it's the souce. 

3.1. Illustration via GnuPG

3.1.1. GnuPG (GNU privacy guard):

    A free open source software for encrypting and signing data. 
    The tool does the following
    i. Encryption: both files and messages. 
    ii. Digital signatures: add digital signatures to data for authentication and guarantee safety in transit.
    iii. Key management: generating, storing & managing cryptographic keys (public and private keys). 
    iv. Email security: encrypt and sign emails. 
    v. File encryption: Used to encrypt individual files.  
    vi. Secure communication: chat and file transfer encryption. 
3.2. How it works

    i. Symmetric-key cryptography:for fast encryption of large amounts of data. 
    ii. Assymmetric/ Public-key cryptography: for secure key exchange. 
    iii. Steps: 
        - generating key pairs: each user creates a pair of keys (public and private).  
        - encrypting data: encrypt message using public key (requires matching private key to decrypt). 
        - signing data: uses private and is verified using matching public key.

3.3. How to use GnuPG
  