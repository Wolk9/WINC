# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(name):
    return f'Hello, {name}!'

print(greet("Bob"))

def add(x, y, z):
   sum = x + y + z
   return sum

print(add(5,3,2))

def positive(x):
    if x > 0: 
        return True
    else:
        return False

print(positive(50))

def negative(x):
    if x < 0:
        return True
    else:
        return False

print(negative(50))
    