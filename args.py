def sum(*args):
    ans= 0
    for n in args:
        print(f"{ans} = {ans} + {n}")
        ans += n
        print(f"answer is {ans}")
    return ans
sum(100,200,12,30,90,50)


def greeting(*args):
    for arg in args:
        print(f"Hello {arg}!")

greeting("Alice", "Bob", "Charlie")      

    