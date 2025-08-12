#Polymorphism in Python is the ability to present the same interface for different data types.
#Taking advantage of polymorphism allows us to write more generic and reusable code.
#Taking the same method to implement different functionalities in different classes.
class Shape:
    def __init__(self, name):
        self.name= name
    def describe(self):
        print(f"This shape is called {self.name}")
shape1= Shape(name="Circle")
shape1.describe()
#Inheritance allows a class to inherit attributes and methods from another class.
#In this case, the Human class inherits from the Shape class.
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)  # Call the constructor of the parent class
        self.length = length
        self.width = width
    def area(self):
        area= self.length * self.width
        print(f"The area of the {self.name} is {area}")
        return area
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)  # Call the constructor of the parent class
        self.radius = radius
    def area(self):
        area = 3.14 * (self.radius ** 2)
        print(f"The area of the {self.name} is {area}")
        return area

r1 = Rectangle(name="Rectangle", length=5, width=3)
r1.describe()  # Call the method from the parent class
r1.area()  # Call the method from the child class

c1 = Circle(name="Circle", radius=4)
c1.describe()  # Call the method from the parent class
c1.area()  # Call the method from the child class

    
        
