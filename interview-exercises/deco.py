
def negative(func):
    def inner(a,b):
        if a<0:
            return "negative"
        return func(a,b)
    return inner

@negative
def add(a,b):
    return a+b

k=print(add(-2,10))