#write a 2d vector class with basic operations like addition, subtraction, scalar multiplication, dot product, and magnitude calculation.
class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def __add__(self,other):
    return Vector2D(self.x + other.x, self.y + other.y)    

def __sub__(self,other):
    return Vector2D(self.x - other.x, self.y - other.y)

def __mul__(self,scalar):
    return Vector2D(self.x * scalar, self.y * scalar)

obj1 = Vector2D(3, 4)
obj2 = Vector2D(1, 2)