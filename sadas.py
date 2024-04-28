class Person:
    def __init__(self, name: str, phone: str, email: str, address: str):
        self._name = name
        self._phone = phone
        self._email = email
        self._address = address

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("Name must be a string.")

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str):
        if isinstance(value, str):
            self._phone = value
        else:
            raise TypeError("Phone must be a string.")

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if isinstance(value, str):
            self._email = value
        else:
            raise TypeError("Email must be a string.")

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str):
        if isinstance(value, str):
            self._address = value
        else:
            raise TypeError("Address must be a string.")

class Client(Person):
    def __init__(self, name: str, phone: str, email: str, address: str, id_client: int):
        super().__init__(name, phone, email, address)
        self._id_client = id_client

    @property
    def id_client(self) -> int:
        return self._id_client

    @id_client.setter
    def id_client(self, value: int):
        if isinstance(value, int):
            self._id_client = value
        else:
            raise TypeError("ID Client must be an integer.")

class Provider(Person):
    def __init__(self, name: str, phone: str, email: str, address: str, id_provider: int):
        super().__init__(name, phone, email, address)
        self._id_provider = id_provider

    @property
    def id_provider(self) -> int:
        return self._id_provider

    @id_provider.setter
    def id_provider(self, value: int):
        if isinstance(value, int):
            self._id_provider = value
        else:
            raise TypeError("ID Provider must be an integer.")

class Personal(Person):
    def __init__(self, name: str, phone: str, email: str, address: str, id_personal: int):
        super().__init__(name, phone, email, address)
        self._id_personal = id_personal

    @property
    def id_personal(self) -> int:
        return self._id_personal

    @id_personal.setter
    def id_personal(self, value: int):
        if isinstance(value, int):
            self._id_personal = value
        else:
            raise TypeError("ID Personal must be an integer.")

class SystemWareHouse:
    """Warehouse system for managing clients, providers, and personnel."""

    def __init__(self):
        self.users = {}  # User IDs to passwords
        self.clients = {}  # User IDs to Client instances
        self.providers = {}  # User IDs to Provider instances
        self.personnel = {}  # User IDs to Personal instances

    def register_user(self, user_id: int, password: str) -> None:
        """Register a new user with the given user ID and password.

        Args:
            user_id (int): The user ID for the new user.
            password (str): The user's password.

        Raises:
            KeyError: If the user ID already exists.
        """
        if user_id in self.users:
            raise KeyError("User ID already exists.")
        self.users[user_ 
                   
                   
                   
                   
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)