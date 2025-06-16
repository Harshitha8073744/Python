def login_required(func):
    def inner(name,status):
        if status== False:
            print("login is required")
        else:
            return func(name,status)
    return inner