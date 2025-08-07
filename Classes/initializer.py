class Human():
    def __init__(self, name, gender , age):
        print("Human class initialized")
        print(name)
        print(gender)
        print(age)
        self.name = name
        self.gender=gender
        self.age=age
        if self.gender=="Male":
            self.ribs=24
            self.curse="Suffer"
        else:
            self.ribs=23
            self.curse="Endure"
    
    
    def  another_method(self):
        print("This is another method in the Human class")



Adam = Human(name="Adam", gender="Male", age=24)
Adam.another_method()
print("Name:", Adam.name)
print("Ribs:",Adam.ribs)
print("Curse:",Adam.curse)

print()

Evah= Human(name="Evah", gender="Female", age=21) #Here i used **kwargs to pass the arguments
Evah.another_method()
#initializer is same as constructor in javascript
#initializer is called when an object is created
#The purpose of the initializer is to initialize the attributes of the class
print("Name:", Evah.name)
print("Ribs:",Evah.ribs)
print("Curse:",Evah.curse)