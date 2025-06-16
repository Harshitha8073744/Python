# it is a function that takes a function as a input and returns modified function as output

#without decorator

def calc(a,b):
    print(a/b)

calc(10,2) # 5.0
calc(10,0)# zero division error
print("ga") # does not execute due to error in before line
