#with decorator

def smartdiv(func):
    def inner(a,b):
        if b==0:
            print("not divisible by zero")
        else:
            return func(a,b)
    return inner


@smartdiv
def calc(a,b):
    print(a/b)

calc(10,2) # 5.0
calc(10,0)# prints not divisible
print("ga") 