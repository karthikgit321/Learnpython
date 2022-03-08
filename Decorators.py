def div(a,b):

    print(a/b)

#consider if the above new logic code is present in different file or you dont hve access to this code
#or if you dont want to change the existing code,so in this case we need to swap without modifying the existing function
#thats when the decorators come into picture to avoid code reusability and make the code make more readable

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div=smart_div(div)
div(2,4)