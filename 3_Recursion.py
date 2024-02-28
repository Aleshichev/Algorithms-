# Recursion
# ------------stack ----------------------
def greet(name):
    print ("hello, " + name + "!")
    greet2(name)
    print ("getting ready to say bye ... ")
    Bye()

def greet2(name):
    print ("how are you, " + name + "?")
    
def Bye():
    print ("ok bye!")

greet("maggie")

# ------------factorial ----------------------

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)