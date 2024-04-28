Class Client(Person):
    def __init__(self, name: str, phone: str, email: str, address: str, id_client : int):
        super().__init__(name, phone, email, address)
        self.id_client = id_client

    def id_length(self):
        if (len(self.id_client) != 10):
            raise ValueError("The id must have 10 characters. Please add 0 to complete the 10 characters.")
        
        
        
class Rectangle:
  def __init__(self, method):
      self.method = method

  def method1(self, blf_x, blf_y, width, height):
      self.width = width
      self.height = height
      self.bl_x = blf_x
      self.bl_y = blf_y

  def method2(self, center_x, center_y, width, height):
      self.center_x = center_x
      self.center_y = center_y
      self.width = width
      self.height = height

  def method3(self, bl_x, bl_y, ur_x, ur_y):
      self.bl_x = bl_x
      self.bl_y = bl_y
      self.ur_x = ur_x
      self.ur_y = ur_y

  def compute_area(self):
      if self.method == 1:
          return self.width * self.height
      elif self.method == 2:
          return (self.width * self.height) / 2
      elif self.method == 3:
          return (self.ur_x - self.bl_x) * (self.ur_y - self.bl_y)

  def compute_perimeter(self):
      if self.method == 1:
          return 2 * (self.width + self.height)
      elif self.method == 2:
          return 2 * self.width + 2 * self.height
      elif self.method == 3:
          return 2 * (self.ur_x - self.bl_x) + 2 * (self.ur_y - self.bl_y)


class Square(Rectangle):
  def __init__(self, method):
      super().__init__(method)

  def compute_interference_point(self, point_x, point_y):
      if self.method == 1:
          if point_x < self.bl_x or point_x > self.bl_x + self.width or point_y < self.bl_y or point_y > self.bl_y + self.height:
              return "The point is outside the square"
          else:
              return "The point is inside the square"
      elif self.method == 2:
          if point_x < self.center_x - self.width / 2 or point_x > self.center_x + self.width / 2 or point_y < self.center_y - self.height / 2 or point_y > self.center_y + self.height / 2:
              return "The point is outside the square"
          else:
              return "The point is inside the square"
      elif self.method == 3:
          if point_x > self.bl_x and point_x < self.ur_x and point_y > self.bl_y and point_y < self.ur_y:
              return "The point is inside the square"
          else:
              return "The point is outside the square"

square = Square(3)
square.method3(0, 0, 9, 5)  
print("The area is: ", square.compute_area())
point_x = -2
point_y = 3  
result = square.compute_interference_point(point_x, point_y)

print(f"This is inside the square: {result}")
    
    
    
    class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido
        self._edad = edad      # Atributo protegido

    # Getter para el atributo nombre
    def get_nombre(self):
        return self._nombre

    # Setter para el atributo nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

    # Getter para el atributo edad
    def get_edad(self):
        return self._edad

    # Setter para el atributo edad
    def set_edad(self, edad):
        if edad >= 0:
            self._edad = edad
        else:
            print("La edad debe ser un número positivo.")
