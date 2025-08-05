# keywords and arguments
def greeting(name, Nationality):
    print("Name is", name)
    print("From the", Nationality)
greeting("STATE", "EVA")
#if i swith the position of the arguments, output will be different name will be Nationality and vice versa
#but if i use keyword arguments, it will not matter
def Hello(name,Nationality):
    print("Name is", name)
    print("From the", Nationality)
Hello(Nationality="STATE", name="Eva")
#KWARGS PROFILE
def employee(**kwargs):
    print(kwargs)
employee(name="John", age=30, position="Developer")
employee(name="Alice", age=25, position="Designer", country="USA")
#employee(Bob, age=40)  # This will raise an error because 'Bob' is not a keyword argument 
#kwargs allows you to pass a variable number of keyword arguments to a function
                                                                            
def mixed(*args, **kwargs):
    print ("Positional arguments:", args)
    print ("Keyword arguments:", kwargs)
mixed(1, 2, 3, name="Alice", age=30)
# This will print:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 30}
# You can also pass arguments as a list
 
   