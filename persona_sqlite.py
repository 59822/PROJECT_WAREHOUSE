from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(String, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    password = Column(String)
    user_name = Column(String)

    def __init__(self, name, phone, email, password, user_name):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.user_name = user_name

class System:
    def __init__(self):
        # Aquí defines la conexión al motor de la base de datos
        self.engine = create_engine('sqlite:///usuarios.db')
        # Aquí creas todas las tablas definidas en Base en la base de datos
        Base.metadata.create_all(self.engine)
        # Aquí creas una sesión para interactuar con la base de datos
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def user_exists(self, email):
        user = self.session.query(Usuario).filter_by(email=email).first()
        return user is not None

    def login(self, email, password):
        user = self.session.query(Usuario).filter_by(email=email, password=password).first()
        return user is not None

# Ejemplo de uso
sistema = System()
email = "example@example.com"
password = "password123"

if sistema.user_exists(email):
    if sistema.login(email, password):
        print("Inicio de sesión exitoso.")
    else:
        print("Contraseña incorrecta.")
else:
    print("El usuario no existe.")
 