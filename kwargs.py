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
          