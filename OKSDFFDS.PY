class Usuario:
    def __init__(self, nombre, email, rol):
        self.nombre = nombre
        self.email = email
        self.rol = rol


class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre}: {self.cantidad} unidades"


class Color(Producto):
    def __init__(self, nombre, cantidad, color):
        super().__init__(nombre, cantidad)
        self.color = color


class Marcador(Producto):
    def __init__(self, nombre, cantidad, tipo_tinta):
        super().__init__(nombre, cantidad)
        self.tipo_tinta = tipo_tinta


class Cuaderno(Producto):
    def __init__(self, nombre, cantidad, tamano):
        super().__init__(nombre, cantidad)
        self.tamano = tamano


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


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def comprar_producto(self, sistema, nombre_producto, cantidad):
        producto = sistema.buscar_producto(nombre_producto)
        if producto:
            if producto.cantidad >= cantidad:
                producto.cantidad -= cantidad
                print(f"¡Compra realizada! {cantidad} {nombre_producto}(s) comprado(s) por {self.nombre}.")
            else:
                print("Lo siento, no hay suficiente cantidad en stock.")
        else:
            print("Producto no encontrado.")


class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre

    def agregar_stock(self, sistema, nombre_producto, cantidad):
        producto = sistema.buscar_producto(nombre_producto)
        if producto:
            producto.cantidad += cantidad
            print(f"Stock de {nombre_producto} actualizado a {producto.cantidad} unidades.")
        else:
            print("Producto no encontrado.")


class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def consultar_stock(self, sistema):
        print("Stock actual:")
        sistema.mostrar_productos()


# Ejemplo de uso:
sistema = SistemaProductos()
sistema.agregar_producto(Color("Lápiz de color", 50, "rojo"))
sistema.agregar_producto(Marcador("Marcador permanente", 30, "tinta negra"))
sistema.agregar_producto(Cuaderno("Cuaderno de dibujo", 20, "A4"))

sistema.registrar_usuario("Juan", "juan@example.com", "Cliente")
sistema.registrar_usuario("Maria", "maria@example.com", "Proveedor")
sistema.registrar_usuario("Pedro", "pedro@example.com", "Empleado")

cliente1 = Cliente("Juan")
cliente1.comprar_producto(sistema, "Lápiz de color", 10)

proveedor1 = Proveedor("Maria")
proveedor1.agregar_stock(sistema, "Lápiz de color", 20)

empleado1 = Empleado("Pedro")
empleado1.consultar_stock(sistema)

print("\nUsuarios registrados:")
sistema.mostrar_usuarios()
