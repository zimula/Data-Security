# rockyou.txt and see if password is in the list

class PasswordChecker:
    
    _instance = None

    def __new__(cls, file_path):
        if cls._instance is None:
            
            cls._instance = super(PasswordChecker, cls).__new__(cls)
            
            cls._instance.file_path = file_path
            
            cls._instance.load_passwords()
        return cls._instance
    
    #load passwords from file
    def load_passwords(self):
        try:
            with open(self.file_path, 'r') as f:
                self.passwords = set(line.strip() for line in f)
        except FileNotFoundError:
            self.passwords = set()
    
    def is_password_in_file(self, password):
        return password in self.passwords