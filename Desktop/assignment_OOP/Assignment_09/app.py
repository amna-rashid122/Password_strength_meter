from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):
    def __init__(self, width , height):
        self.width = width
        self.height = height 
    def area (self):
        return self.width * self.height
if __name__ == "__main__":
    rect = Rectangle(5,10)
    print("Area of reactangle:", rect.area())        