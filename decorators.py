def shout(text):
    return text.upper()+"!"

f=shout
print(f("hello"))
#print(f("arshita"))
#twice_function(shout, "hello") has 2 arguments, and that is correct because twice_function accepts 2 arguments. Problem was inside it: shout() was getting 2 arguments.
#def twice_function(func,value):
 #   return func(func,value)
#print(twice_function(shout,"hello"))
#twice_function(shout, "hello") has 2 arguments, and that is correct because twice_function accepts 2 arguments. Problem was inside it: shout() was getting 2 argument

def twice_function(func,val):
    return func(func(val))
print(twice_function(shout,"hello"))

#decorative function
def log_call(func):
   def wrapper(*args,**kwargs):
        print(f"calling ...")
        print(f"func.__name__")
        result=func(*args,**kwargs)
        print("Done")
        return result
   return wrapper

@log_call
def greet(name):
    print(f"hello {name}")

greet("Arshita")