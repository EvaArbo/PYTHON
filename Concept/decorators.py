#Decorator 
def my_decor(fun):
    def wrapper():
        print("Before function call")
        fun()
        print("After function call")
    return wrapper

@my_decor
def say_hello():
    print("Hello, World!")

# keywords and arguments
@my_decor
def greet():
    print("Greeting from above!!")

say_hello()
greet()



