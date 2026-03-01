# Decorator = A FUNCTION THAT EXTENDS THE BEHAVIOR OF ANOTHER FUNCTION
# w/o modifying the base function
# Pass the base function as an argument to the decorator

#  @add_sprinkles
#  get_ice_cream("Vanilla")


#DECORATOR
def add_sprinkles(func):
    def wrapper(*args, **kwargs):#WRAPPER FUNCS CAN ONLY HAVE *args and **kwargs AS PARAMETERS
        print("YOU ADD SPRINKLES")
        func(*args, **kwargs)

    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs): #WRAPPER FUNCS CAN ONLY HAVE *args and **kwargs AS PARAMETERS
        print("YOU ADD FUDGE")
        func(*args,  **kwargs)

    return wrapper


#THE DECORATOE EXTENDS THE BASE FUNCTION 
@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"HERE IS YOUR {flavour} ICE CREAM")

get_ice_cream("CHOCOLATE")