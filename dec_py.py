def div(a,b):
    return a%b

def samrt_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return func()
    return inner()

result=div(3,9)
print(result)