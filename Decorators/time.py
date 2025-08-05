def time_fn(fn):
    import time
    def wrapper():
        start_time = time.time()
        fn()
        end_time = time.time()
        diff = end_time - start_time
        print(f"Function took {diff} seconds to execute.")
    return wrapper
   
@time_fn
def count():
    for i in range(1000000):
        print(i)
@time_fn
def count2():
    for i in range(0,1000):
        print(i)

count2()
# This will prgitint the time taken to execute the count function
# and the count2 function will execute without timing information.
# You can also use the decorator on other functions


    