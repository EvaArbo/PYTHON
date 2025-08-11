
from datetime import datetime
def write_file(f_name,txt):
    with open(f_name,'a') as file:
        file.write(f"{txt} \n")

class Human():
    species = "Homo sapiens"  # Static attribute shared by all instances
    genus = "Homo"
    count = 0

    def __init__(self, name, gender , age):
        print("Human class initialized")
        print(name)
        print(gender)
        print(age)
        self._name = name
        self._gender=gender
        self._age=age
        if self._gender=="Male":
            self._ribs=24
            self._curse="Suffer"
        else:
            self._ribs=23
            self._curse="Endure"
        self.__class__.count=self.__class__.count+1
        
    def  another_method(self):
        print("This is another method in the Human class")
        #Getter for name
    @property
    def name(self):
        now =datetime.now()
        print (f"Name accessed at {now}")
        write_file(f_name="logger.txt", txt=f"Name accessed at {now}")
        # Return the name attribute
        # This is a getter method to access the name attribute
        return self._name
    @name.setter
    def name(self, NewName):
        if not isinstance(NewName, str):
            print("Invalid name type. Must be a string.")
            return
        now = datetime.now()
        print(f"Name set at {now} to {NewName} from {self._name}")
        write_file(f_name="logger.txt", txt=f"Name set at {now} to {NewName} from {self._name}")
        self._name =NewName
        return self._name
    @classmethod
    def get_general_info(cls):
        print("Species:", cls.species)
        print("Genus:", cls.genus)
        print("Total Humans created:", cls.count)
Adam= Human(name="Adam", gender="Male", age=24)
Evah= Human(name="Evah", gender="Female", age=23)
Human.get_general_info()  # Call the class method to print general info

print("Name:", Adam.name)
print("Name:", Evah.name)
                
#setters are used to set the value of an attribute


# Adam = Human(name="Adam", gender="Male", age=24)
# Adam.another_method()
# print("Name:", Adam._name)
# print("Ribs:",Adam._ribs)
# print("Curse:",Adam._curse)
# print(Adam._name)  # Accessing the getter for name
# Adam.name = "Adam Smith"  # Using the setter to change the name
# print("Adam species:", Adam.species)  # Accessing the static attribute

# print()

# Evah= Human(name="Evah", gender="Female", age=21) #Here i used **kwargs to pass the arguments
# Evah.another_method()
# #initializer is same as constructor in javascript
# #initializer is called when an object is created
# #The purpose of the initializer is to initialize the attributes of the class
# print("Name:", Evah._name)
# print("Ribs:",Evah._ribs)
# print("Curse:",Evah._curse)
# print(Evah._name)  # Accessing the getter for name
# Evah.name = "Evah Johnson"  # Using the setter to change the name
# print("Evah species:", Evah.species)  # Accessing the static attribute
# print("Species:", Human.species)  #
# print("Genus:", Human.genus)  # Accessing the static attribute
# print("Total Humans created:", Human.count)  # Accessing the static attribute

    
