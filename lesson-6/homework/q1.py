def check(func):
    def wrapper(a, b):
        if b == 0:
            print("Denominator can't be zero")
        else:
            return a/b
    return wrapper        
@check
def div(a, b):
   return a / b

print(div(6, 2))
div(6, 0)