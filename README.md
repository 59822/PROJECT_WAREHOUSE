# Proyecto

## Warehouse

Yo se que esta en español, pero luego lo cambiamos a ingles

### Instrucción del código
En este caso, como pueden observar en primer lugar tenemos una clase que define al usuario, el objetivo es que se almacenen los usuarios y con su categoria puedan acceder a ver la base, a modificarla aumentando o disminuyendo 


```python 
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
    
    def vinculation(self, vinculation):
        self.vinculation = vinculation
        

class Provider(Usuario):
    def __init__(self, email: str, password: str, associated_brand: str):
        super().__init__(email, password)
        self.associated_brand = associated_brand
        
        
class Personal(Usuario):
    def __init__(self, email: str, password: str, personal_position: str):
        super().__init__(email, password)
        self.personal_position = personal_position
        
     
class System(Usuario):
    def __init__(self, email: str, password: str, vinculation: str):
        super().__init__(email, password)
        self.vinculation = vinculation
        
    def vinculation(self, vinculation):
        if self.vinculation == "Client": ##Revisar para que valide en todos formatos, upper, lower or capital
            return f"Client vinculated. Welcome to the system {self._name}!. \n Enjoy your searching buy."
        elif self.vinculation == "Provider": #Revisar x2 ok
            return f"Provider vinculated. Welcome to the system {self._name}!. \n You will be redirected to our provider base."
        elif self.vinculation == "Personal": #Revisar x2 ok
            return f"Personal vinculated. Welcome to the system {self._name}!. \n You will be redirected to the personal base."
        
```
Aquí practicamente busco que se con su vinculación pueda acceder, pero no se si tenga que hacer algo tipo otro archivo.
### Pendiente ok
1. Queda pendiente si son de caracter privado, publico o la otra q no me acuerdo ok
2. Redirigir al usuario de acuerdo a su categoria 



```python 
       
class Product:
    def __init__(self, name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand=None):
        self.name = name
        self.quantity = quantity
        self.set_provider(provider, id_provider)
        self.set_description(description)
        self.set_price(price_personal, price_wholesale)
        self.brand = brand  # Brand is optional and can be None

    def __str__(self):
        return f"{self.name}: {self.quantity} units"

    def set_provider(self, provider, id_provider):
        if isinstance(provider, str) and isinstance(id_provider, int):
            self.provider = provider
            self.id_provider = id_provider
        else:
            raise TypeError("Provider must be a string and provider ID must be an integer.")
    
    def get_provider(self):
        return self.provider
    
    def set_description(self, description):
        self.description = description
    
    def get_description(self):
        return self.description
    
    def set_price(self, personal, wholesale):
        if isinstance(personal, (int, float)) and isinstance(wholesale, (int, float)):
            self.price_personal = personal
            self.price_wholesale = wholesale
        else:
            raise TypeError("Prices must be integers or decimals.")

    def get_price_wholesale(self):
        return self.price_wholesale
    
    def get_price_personal(self):
        return self.price_personal

class Agenda(Product):
    def __init__(self, name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand):
        super().__init__(name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand)

class Color(Product):
    def __init__(self, name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand, color):
        super().__init__(name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand)
        self.color = color

class Micropoint(Product):
    def __init__(self, name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand, point_type, color):
        super().__init__(name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand)
        self.point_type = point_type
        self.color = color
        
class Corrector(Product):
    def __init__(self, name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand):
        super().__init__(name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand)


class Eraser(Product):
    def __init__(self, name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand):
        super().__init__(name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand)


class SewingMachine(Product):
    def __init__(self, name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand):
        super().__init__(name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand)


class Notebook(Product):
    def __init__(self, name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand, format, sheets):
        super().__init__(name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand)
        self.format = format
        self.sheets = sheets


class Pen(Product):
    def __init__(self, name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand, color):
        super().__init__(name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand)
        self.color = color


class GeometrySet(Product):
    def __init__(self, name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand):
        super().__init__(name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand)


class Pencil(Product):
    def __init__(self, name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand):
        super().__init__(name, quantity, provider, id_provider, description, price_personal, price_wholesale, brand)

```

### Observacion

Aquí en este codigo solo se despliega las clases y sus clasificaciones

### Pendiente
1. Saber como se van a unir los datos con un texto que pensaba que fuera JSON
2. Generar el sistema de productos que es un fichero a parte pq pues se ve medio feo ahi o no se 

``` python 

class SistemaProductos:
    def __init__(self):
        self.productos = []
        self.usuarios = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None

    def registrar_usuario(self, nombre, email, rol):
        usuario = Usuario(nombre, email, rol)
        self.usuarios.append(usuario)
        print(f"Usuario {nombre} registrado como {rol}.")

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario.nombre, usuario.email, usuario.rol)
            

```

### Observacion
No le hagan caso a eso pq me quede en blanco intentando unirlo. Pero es el que quiero integrar en u fichero aparte ok 

### Pendiente
1. Integrarlo a fichero a parte


# General
La verdad me mori, luego ya intent unir todo el codigo pero ahi estarian las bases. 

1. Los objetos los podriamos integrar en otro fichero para q no quede tan largo el proyecto
2. Utilice lo de raise y esa vaina, tambien lo del encapsulamiento pero no se q opinen
3. Están los setters y getters 
4. Me gustaria hacer la base de datos en JSON, pero luego vemos okey. Cualquier cosa me escriben xd