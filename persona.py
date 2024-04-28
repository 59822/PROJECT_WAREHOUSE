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
        
class WareHouse:
    def __init__(self, code: str, line: str, quantity: int, description: str):
        self._code = code
        self._line = line
        self._quantity = quantity
        self._description = description
        self._providers = []  # List to store instances of Provider
        self._associated_brands = []  # List to store associated brands
        self._personal_positions = []  # List to store personal positions

    def add_provider(self, provider: Provider):
        self._providers.append(provider)

    def add_associated_brand(self, brand: str):
        self._associated_brands.append(brand)

    def add_personal_position(self, position: str):
        self._personal_positions.append(position)

class Producto:
    def __init__(self, nombre, cantidad, provider, id_provider, description, precio_personal, precio_mayorista):
        self.nombre = nombre
        self.cantidad = cantidad  ##Aqui vemos si lo hacemos privado o no, protegido o no
        self.provider = provider
        self.id_provider = id_provider
        self.description = description
        self.precio_personal = precio_personal
        self.precio_mayorista = precio_mayorista

    def __str__(self):
        return f"{self.nombre}: {self.cantidad} unidades".


    def set_provider(self, provider, id_provider):
        if isinstance(provider, str) and isinstance(id_provider, int):
            self.provider = provider
            self.id_provider = id_provider
        else:
            raise TypeError("El proveedor debe ser una cadena de caracteres y el ID del proveedor debe ser un entero.")
    
    def get_provider(self):
        return self._provider
    
    def set_description(self, description):
        self._description = description
    
    def get_description(self):
        return self._description
    
    def set_price(self, personal, mayorista):
        if isinstance(personal, (int, float)) and isinstance(mayorista, (int, float)):
            self.precio_personal = personal
            self.precio_mayorista = mayorista
        else:
            raise TypeError("Los precios deben ser números enteros o decimales.")

    def get_price_mayorista(self):
        return self.precio_mayorista
    
    def get_price_personal(self):
        return self.precio_personal
    
class Agenda(Producto):
    def __init__(self, nombre, cantidad, codigo, proveedor, marca, descripcion, personal, mayorista):
        super().__init__(nombre, cantidad)
        self.codigo = codigo
        self.proveedor = proveedor
        self.marca = marca
        self.descripcion = descripcion
        self.precio_personal = personal
        self.precio_mayorista = mayorista


class Color(Producto):
    def __init__(self, nombre, cantidad, codigo, proveedor, marca, descripcion, personal, mayorista):
        super().__init__(nombre, cantidad)
        self.codigo = codigo
        self.proveedor = proveedor
        self.marca = marca
        self.descripcion = descripcion
        self.precio_personal = personal
        self.precio_mayorista = mayorista
        self.color = None


class Micropunta(Producto):
    def __init__(self, nombre, cantidad, codigo, proveedor, marca, descripcion, personal, mayorista):
        super().__init__(nombre, cantidad)
        self.codigo = codigo
        self.proveedor = proveedor
        self.marca = marca
        self.descripcion = descripcion
        self.precio_personal = personal
        self.precio_mayorista = mayorista


class Corrector(Producto):
    def __init__(self, nombre, cantidad, codigo, proveedor, marca, descripcion, personal, mayorista):
        super().__init__(nombre, cantidad)
        self.codigo = codigo
        self.proveedor = proveedor
        self.marca = marca
        self.descripcion = descripcion
        self.precio_personal = personal
        self.precio_mayorista = mayorista


class Borrador(Producto):
    def __init__(self, nombre, cantidad, codigo, proveedor, marca, descripcion, personal, mayorista):
        super().__init__(nombre, cantidad)
        self.codigo = codigo
        self.proveedor = proveedor
        self.marca = marca
        self.descripcion = descripcion
        self.precio_personal = personal
        self.precio_mayorista = mayorista


class Cosedora(Producto):
    def __init__(self, nombre, cantidad, codigo, proveedor, marca, descripcion, personal, mayorista):
        super().__init__(nombre, cantidad)
        self.codigo = codigo
        self.proveedor = proveedor
        self.marca = marca
        self.descripcion = descripcion
        self.precio_personal = personal
        self.precio_mayorista = mayorista
        self.linea = None


class Cuaderno(Producto):
    def __init__(self, nombre, cantidad, codigo, proveedor, marca, descripcion, personal, mayorista):
        super().__init__(nombre, cantidad)
        self.codigo = codigo
        self.proveedor = proveedor
        self.marca = marca
        self.descripcion = descripcion
        self.precio_personal = personal
        self.precio_mayorista = mayorista
        self.tamano = None


class Esfero(Producto):
    def __init__(self, nombre, cantidad, codigo, proveedor, marca, descripcion, personal, mayorista):
        super().__init__(nombre, cantidad)
        self.codigo = codigo
        self.proveedor = proveedor
        self.marca = marca
        self.descripcion = descripcion
        self.precio_personal = personal
        self.precio_mayorista = mayorista


class JuegoGeometrica(Producto):
    def __init__(self, nombre, cantidad, codigo, proveedor, marca, descripcion, personal, mayorista):
        super().__init__(nombre, cantidad)
        self.codigo = codigo
        self.proveedor = proveedor
        self.marca = marca
        self.descripcion = descripcion
        self.precio_personal = personal
        self.precio_mayorista = mayorista


class Lapiz(Producto):
    def __init__(self, nombre, cantidad, codigo, proveedor, marca, descripcion, personal, mayorista):
        super().__init__(nombre, cantidad)
        self.codigo = codigo
        self.proveedor = proveedor
        self.marca = marca
        self.descripcion = descripcion
        self.precio_personal = personal
        self.precio_mayorista = mayorista


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
            
producto1 = Producto("Lápiz", 100, "Proveedor1", 123, "Lápiz de grafito", 0.5, 0.3)

print("Precio personal actual:", producto1.precio_personal)
print("Precio mayorista actual:", producto1.precio_mayorista)

# Intentando cambiar los precios con un tipo de dato incorrecto
try:
    producto1.set_price("0.5", 0.3)
except TypeError as e:
    print("Error:", e)

# Cambiando los precios correctamente
producto1.set_price(0.6, 0.4)
print("Precio personal actualizado:", producto1.precio_personal)
print("Precio mayorista actualizado:", producto1.precio_mayorista)