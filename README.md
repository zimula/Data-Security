# INTRODUCTION TO DATA SECURITY

## Day 1: Encryption: Classical ciphers/ basic encryption. 
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

## Day 2: Encryption + TLS (Incomplete).
3. Cornerstones og Encryption

        i. Confidenciality: Ability to restrict data/ parts of it to some users.  
        ii. Authenticity: Ability to confirm the the identity of both recipient and data source. 
        iii. Integrity: Confirm that data has not been interfered with during transfer.
        v. Non Repudiation:Data source must not be able to deny that it's the souce. 

3.1. Illustration via GnuPG/ GPG4WWin

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
        
        i. On windows: install gpg4win. 
        ii. open cmd: 
            - type gpg --list-key (finds the directory automatically)
            - type gpg --gen-key (prompts for a secret phrase) and generates private and public key. 
            - Private key is not include in the output. 
            - gpg --edit-key: lets you edit key attributes. 
            - gpg --delete-key <id>: lets you delete key. 
            - gpg --export -a "user_id" > "path\outputfile.asc": exports file to another folder. 
            - gpg --import "path\file": imports key
            - gpg --edit-key id from import: 
            - fpr: confirms key. 
        iii. Making public-key available
            - use export method like above: make downloadable from site. 
            - display on websit: fpr and paste it on site.
            - key servers (keyp.opengpg.org will be used): gpg --send-keys --keyserver keys.opengpg.org "name" 
            - failde when I used name but the id (3E65401BA3FAF2A1) worked fine. 
        iv. Encrypting a file (either by username or key id)
            - gpg -r "username" -e file
            - output: file.extension.gpg
            - opening before decryption: „^’<î¾c@ýoxé!Í€d}2J³|?)ÄìöN~_5‘ñ×¿Zþ0ÕŒã0ìŠ)Ÿ“XzâNm~‹í9¬CCßÚ¯¼$=Ü÷1Ù -„!{d…ÔÀo	Ð#"£PÍÓM,m¸’Ñÿ²rÕ-¼Á¥9Þ*üy~‚AÂƒ_(Š|Ë’SØý®ÉïüvJÑŠ ôÑËp97àÂÄVµ¦YûTõ¨QQ}Â™=Uý•í9Ñ «¢ÅF_iEO0®ÖPóÚ…è<w“±^MDJŸdæß¥Y ‡jåÆ¡Ô}Í¥Xa6·;›U¯átHr¥0å¼Œçüºdp[L!;¼Ø¿dN§zrËÉ[WX8ÿ¾$Œ.€4c¶\ÖìK>“ÎþuV7éÞgç¡²™ýZ ð%UÝéÛ½ù,áñnL:„‚"ÂØ£#’cŽ2DšßKIÿ|óF#/1v¯Ô|':d)Qg;eæúx2Éøé'Á8ˆŒP#p¤ÒÖlQÀÕŒ…ã¡E1Ù“k‚K
        v. Decryption: 
            -gpg -d Encryption_test.txt.gpg
            - output: gpg: encrypted with cv25519 key, ID
            921D163CEEBE1063, created 2025-02-03
            "Martin Zimula <zimula@live.dk>"
            name: Martin Zimula
            email: zimula@live.dk
            phrase: Testing123

            output from cmd:
            pub   ed25519 2025-02-03 [SC] [expires: 2028-02-03]
            64246580A3AD4578FE1ED2693E65401BA3FAF2A1
            uid           [ultimate] Martin Zimula <zimula@live.dk>
            sub   cv25519 2025-02-03 [E] [expires: 2028-02-03]
            message: Hello!.
3.4. TLS 
Simple diagram and explanation.

![alt text](image-2.png)

    Basically, the client shares a key with the server 
    before sending encrypted data. 
    The server uses the key to decrypt the data (revise osi). 

## Day 3: Hashing and salting
- Using algorithms to map data of any size to a bit string (message) of a fixed sized. 
- Hashing algorithms: they differ in the complexity of hashes they produce (bcrypt, sha1, md5 etc).
- Collision: String resulting in similar hashes. Probability is low with existing algorithms (when more than one value to be hashed points to the same slot int he hash table). 
- Salt: add random data to hash. Make the cracking process take longer.  
 
### 4.2. Assignment: Steps in solving the exercise (user registration app). 

    - promp to enter user id/ name and password. 
    - Password must not be in rockyou.txt
    - use singleton pattern to make avoid reading the file each time. 
    - Reject common passwords with a message
    - Acknowledge success of providing a unique password 
    - Hash password using bcrypt and salt.
    - test to see if hash produces same string
    - user id/ name must be stored in database. 

#### 4.2.1. Hash functions, Schema and db complete.
    - Has the following attributes: id, name, mail, hashed password
    - db connector/ initializer and crud are in db.py
    - Function to hash and one to check if the hash produces the same string as user-input. 

#### 4.2.2. singleton pattern and relevance to the assignment
    - Allows to create just one instance of a class. 
    - Global point of access for resource (rockyou.txt in our case). 
    - Make sure there's only one instance of a class throughout the entire lifetime of a program.  
    i. Types
        - module: Data is shared among all the modules (loaded one per program). 
        - classic: Create instance only if none are created so far (overrides __new__ to ensure that only one instance is created).  
        - borg: Instead of enforcing, it makes all instances share the same state. 
    ii. Real life use cases
        - managing database connections. 
        - Logging
        - File manager
        - rockyou.txt: use it as the criterion for password(singleton.py). 

## Day 4 (Solution in day 3 folder): Owasp (OPEN WORLD APPLICATON SECURITY PROJECT)
- OSWAP is an open source nonprofit organization that works to improve security of software. 
- Incidents with code can be found on their website (option to experiment).
- The organization provides ways/ guides on how to protect systems.

### 5. SQL INJECTIONS
    - Gaining unauthorized access via the login screen.
        i. routers: directs http request to the code that handles them. An example of one can be seen below. They are the easiest way to get in into a system if it's not protected.   
 ![alt text](image-3.png)
        ii. Handlers: These are the functions that process the http requests directed by router.  
        iii. My test using red team attack: select name from users where email = '' or 1=1; -- '. This returned all the rows in the database.
        iv. Remedies: 
            a. optimization of the hash: salting. 
            b. sanitizing: modifying/ validating input to ensure format before insertion.    
            c. prepared statements: passing prepared sql statement limits direct interaction with the database. Arguments are replaced with "?" in the statements.  
### 5.1. Assignment¨
    - continue on last assignment
    - replace bcrypt with sha256
    - add another table database users256 (id, userid (unique, varchar (32)), password, comments)
    - attempt sql injection: ' or 1=1;--
    
## Day 5 Ethical Hacking
- John and Hash Cat: easiest to mess with. 
- Hack Niels pc. 
- 


