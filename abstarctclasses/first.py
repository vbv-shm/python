from abc import ABC, abstractmethod, abstractproperty
 
class Shape(ABC):
    def __init__(self, shape_name):
        self.shape_name = shape_name
    
    @abstractproperty
    def name(self):
        pass
     
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self):
        super().__init__("circle")
 
    @property
    def name(self):
        return self.shape_name
    
    def draw(self):    
        print("Drawing a Circle")

circle = Circle()

print(circle.name)