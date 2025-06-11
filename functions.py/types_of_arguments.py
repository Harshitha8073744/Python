#arguments
def calc(a,b):
    print(b-a)

#positional argument
calc(1,2) # 1
calc(2,1) #-1
# output changes when we interchange a and b

# key word argument
calc(a=1,b=2) # 1
calc(b=2,a=1) #1
# ouput same this is keyword argument we clearly define a and b

#default argument

def cal(a,b,c=1): # giving default value for c if we don't use it while calling
    print(a+b+c)  
cal(1,2)# not giving c value
cal(1,2,3) #c=3 and calculated

