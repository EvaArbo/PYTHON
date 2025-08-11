class Shape:
    def __init__(self, name):
        self.name= name
    def describe(self):
        print(f"This shape is called {self.name}")
shape1= Shape(name="Circle")
shape1.describe()
    
        