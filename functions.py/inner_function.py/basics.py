<<<<<<< HEAD
def outer():
    print('outer started')
    def inner():
        print('inner function started')# without calling seperately on def happens not executed as it is not called
    inner()
    def login():
        print('login succesful')
    login()
    return inner

outer()# inner and login won't work without calling outer
# another method to call inner function is adding return value in the outer function 

inner=outer() # inner refers to a function
inner() # inner function started. we have to invoke it as it represents a function
=======
def outer():
    print('outer started')
    def inner():
        print('inner function started')# without calling seperately on def happens not executed as it is not called
    inner()
    def login():
        print('login succesful')
    login()
    return inner

outer()# inner and login won't work without calling outer
# another method to call inner function is adding return value in the outer function 

inner=outer() # inner refers to a function
inner() # inner function started. we have to invoke it as it represents a function
>>>>>>> 97f9261a9df0acc17e96c094d6bc43ad10a8b5c8
