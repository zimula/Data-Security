# rockyou.txt and see if password is in the list

class PasswordChecker:
    
    _instance = None
    #See if there existes an instance of the class
    def __new__(cls, file_path):
        if cls._instance is None:
            
            cls._instance = super(PasswordChecker, cls).__new__(cls)
            
            cls._instance.file_path = file_path
            
            cls._instance.load_passwords()
        return cls._instance
    
    #load passwords from file
    def load_passwords(self):
        try:
            with open(self.file_path, 'r', encoding="latin-1") as f: #utf-8 can be used but errors must be ignored. 
                self.passwords = set(line.strip() for line in f)
        except FileNotFoundError:
            self.passwords = set()
            
    #See if password is in the list
    def is_password_in_file(self, password):
        return password in self.passwords