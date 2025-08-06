x=10#Integer
pi=3.142#Float
name="John Doe"#String
is_active=True#Boolean
#List
fruits=["apple", "banana", "cherry"] #List of strings
#Tuple
coordinates=(10.0, 20.0) #Tuple with two float values immutable
#Dictionary
person={"name": "John", "age": 30, "is_active": True}#key-value pairs
#Set
unique_numbers={1, 2, 3, 4, 5} #Set with unique integers
#NoneType
nothing=None
#Complex number
complex_num=2 + 3j  #Complex number with real and imaginary parts   
#Bytes
byte_data=b"Hello, World!"  #Bytes type for binary data
#Bytearray
byte_array=bytearray([65, 66, 67])  #Mutable sequence of bytes
#Memoryview
memory_view=memoryview(byte_array)  #Memory view of the bytearray       
#Range
number_range=range(5)  #Range object representing numbers from 0 to 4
#Frozen set
frozen_set=frozenset([1, 2, 3, 4, 5])  #Immutable set
#Enum
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3    
#Example usage of Enum
favorite_color = Color.RED  #Assigning an Enum value
#Function
def greet(name):
    return f"Hello, {name}!"  #Function that returns a greeting message
#Example usage of function
greeting_message = greet("Alice")  #Calling the function with a name
#Class
class Person:       
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."  #Method to introduce the person
#Example usage of class
john = Person("John", 30)  #Creating an instance of the Person class
introduction = john.introduce()  #Calling the introduce method
#Printing the data types and their values
print(f"Integer: {x}, Type: {type(x)}")
print(f"Float: {pi}, Type: {type(pi)}")
print(f"String: {name}, Type: {type(name)}")
print(f"Boolean: {is_active}, Type: {type(is_active)}")
print(f"List: {fruits}, Type: {type(fruits)}")
print(f"Tuple: {coordinates}, Type: {type(coordinates)}")
print(f"Dictionary: {person}, Type: {type(person)}")
print(f"Set: {unique_numbers}, Type: {type(unique_numbers)}")
print(f"NoneType: {nothing}, Type: {type(nothing)}")
print(f"Complex Number: {complex_num}, Type: {type(complex_num)}")
print(f"Bytes: {byte_data}, Type: {type(byte_data)}")
print(f"Bytearray: {byte_array}, Type: {type(byte_array)}")
print(f"Memoryview: {memory_view}, Type: {type(memory_view)}")
print(f"Range: {number_range}, Type: {type(number_range)}")
print(f"Frozen Set: {frozen_set}, Type: {type(frozen_set)}")
print(f"Enum: {favorite_color}, Type: {type(favorite_color)}")
print(f"Function: {greet}, Type: {type(greet)}")
print(f"Class: {john}, Type: {type(john)}")
print(f"Introduction: {introduction}, Type: {type(introduction)}")
#This code demonstrates various data types in Python, including basic types, collections, and user-defined types like classes and enums.
#Each data type is printed along with its value and type for clarity.
#This serves as a comprehensive overview of Python's data types and their usage.    
#This code snippet demonstrates various data types in Python, including basic types, collections, and user-defined types.
#Each data type is defined, and examples of their usage are provided.
#This code snippet demonstrates various data types in Python, including basic types, collections, and user-defined types.
#Each data type is defined, and examples of their usage are provided.
#This code snippet demonstrates various data types in Python, including basic types, collections, and user-defined types.
#Each data type is defined, and examples of their usage are provided.
#This code snippet demonstrates various data types in Python, including basic types, collections, and user
#-defined types.
