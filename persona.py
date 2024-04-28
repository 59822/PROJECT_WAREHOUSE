class Usuario:
    def __init__(self, name: str, phone: str, email: str, password: str, user_name: str):
        self._name = name
        self._phone = phone
        self._email = email #Protected attribute
        self.__password = None #Private attribute
        self.user_name = user_name #Public attribute
    
    def set_password(self, password):
        if (len(password) < 10 and any(char.isupper()) for char in password and any(char.islower() for char in password)):
            raise ValueError("The password must have at least 8 characters. And at least one uppercase and one lowercase letter.")
        else:
            self.__password = password
        
    def get_password(self):
        return "The password is protected"
    
    def 