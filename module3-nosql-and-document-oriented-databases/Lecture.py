def incriment(x):
    return x +1

def double(x):
    return x * 2

def run_twice(func, arg):
    return func(func(arg))

def rec_print(n):
    print(n)
    if n >= 0:
        rec_print(n-1)

def add(x,y):
    return x + y

def identity(x): 
    return x

