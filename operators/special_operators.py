# membership and identity operators are known as special operators

#membership: to verify element present in sequence or not
enames=['rg','sg','pg','nm']
print('nm' in enames) #True

unames=('rahul','Sonia')
print('Rajini' not in unames) # False

eid={101,102,103,104}
print(106 in eid) #false

#identity: address comparision.  is, is not: address comparision |  == : content comparision

a=10
b=90
c=10
# both a and c will be stored in the same memory address and will have two reference a and c 

print( a is c) # True
print( a is b) # false

# range(start, end, step)

range_values= range(0,500,1)
print(390 in range_values) # True