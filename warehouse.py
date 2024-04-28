class Product:
    def __init__(self, codigo: str, proveedor: str, linea: str, marca: str, producto: str, personal: float, mayorista: float, cantidad: int, descripcion: str):
        self._codigo = codigo  # código del producto
        self._proveedor = proveedor  # nombre del proveedor. // Foreign key
        self._linea = linea  # línea del producto  
        self._marca = marca  # marca del producto
        self._producto = producto  # nombre del producto
        self._personal = personal  # precio para personal
        self._mayorista = mayorista  # precio mayorista
        self._cantidad = cantidad  # cantidad en stock
        self._descripcion = descripcion  # descripción del producto             
        
        
               
class Person:
    person = "Person that interacts with the system of warehouse"
    def __init__(self, name: str, phone: str, email: str, address: str):
        self._name = name
        self._phone = phone
        self._email = email       
        self._address = address

class Client(Person):
    def __init__(self, name: str, phone: str, email: str, address: str, id_client : int):
        super().__init__(name, phone, email, address)
        self.id_client = id_client
        
    def id_length(self):
        if (len(self.id_client) != 10):
            raise ValueError("The id must have 10 characters. Please add 0 to complete the 10 characters.")
        
        
class Provider(Person):
    def __init__(self, name: str, phone: str, email: str, address: str, id_provider : int):
        super().__init__(name, phone, email, address)
        self._id_address = id_provider
        
        
        
class Personal(Person):
    def __init__(self, name: str, phone: str, email: str, address: str, id_personal : int):
        super().__init__(name, phone, email, address)
        self._id_personal = id_personal


                             
class WareHouse:
    def __init__(self):
        self.items = []
    
    def add_item(self, item: Product):
        self.items.append(item)
        
    def rest_item(self, item: Product):
        self.items.remove(item)
        
    def show_items(self):
        for item in self.items:
            print(f"Code: {item._codigo}")
            print(f"Supplier: {item._proveedor}")
            print(f"Line: {item._linea}")
            print(f"Brand: {item._marca}")
            print(f"Product: {item._producto}")
            print(f"Personal Price: {item._personal}")
            print(f"Wholesale Price: {item._mayorista}")
            print(f"Quantity: {item._cantidad}")
            print(f"Description: {item._descripcion}")
            print()

        
class Agenda(Product):
    def __init__(self, codigo: str, proveedor: str, marca: str, descripcion: str, personal: float, mayorista: float, cantidad: int):
        super().__init__(codigo, proveedor, "Agenda", marca, "Agenda", personal, mayorista, cantidad)
        
class Color(Product):
    def __init__(self, codigo: str, proveedor: str, marca: str, descripcion: str, personal: float, mayorista: float, cantidad: int):
        super().__init__(codigo, proveedor, "Color", marca, "Color", personal, mayorista, cantidad)
                
class Micropunta(Product):
    def __init__(self, codigo: str, proveedor: str, marca: str, descripcion: str, personal: float, mayorista: float, cantidad: int):
        super().__init__(codigo, proveedor, "Micropunta", marca, "Micropunta", personal, mayorista, cantidad)
        
class Corrector(Product):
    pass

class Borrador(Product):
    def __init__(self, codigo: str, proveedor: str, marca: str, descripcion: str, personal: float, mayorista: float, cantidad: int):
        super().__init__(codigo, proveedor, "Borrador", marca, "Borrador", personal, mayorista, cantidad)
        
class Cosedora(Product):
    def __init__(self, codigo: str, proveedor: str, linea: str, marca: str, producto: str, personal: float, mayorista: float, cantidad: int):
        super().__init__(codigo, proveedor, linea, marca, producto, personal, mayorista, cantidad)
        
class Cuaderno(Product):
    def __init__(self, codigo: str, proveedor: str, marca: str, descripcion: str, personal: float, mayorista: float, cantidad: int):
        super().__init__(codigo, proveedor, "Cuaderno", marca, "Cuaderno", personal, mayorista, cantidad)
        
class Esfero(Product):
    def __init__(self, codigo: str, proveedor: str, marca: str, descripcion: str, personal: float, mayorista: float, cantidad: int):
        super().__init__(codigo, proveedor, "Esfero", marca, "Esfero", personal, mayorista, cantidad)
        
class JuegoGeometrica(Product):
    def __init__(self, codigo: str, proveedor: str, marca: str, descripcion: str, personal: float, mayorista: float, cantidad: int):
        super().__init__(codigo, proveedor, "Juego Geométrico", marca, "Juego Geométrico", personal, mayorista, cantidad)
        
class Lapiz(Product):
    def __init__(self, codigo: str, proveedor: str, marca: str, descripcion: str, personal: float, mayorista: float, cantidad: int):
        super().__init__(codigo, proveedor, "Lápiz", marca, "Lápiz", personal, mayorista, cantidad)
        
pepito = WareHouse()
print(pepito.show_items())


client1 = Client("Juan", "1234567", "juan3213@hotmail.com", "Calle 123", 100000) 
client1.id_length()
print(client1.id_client)