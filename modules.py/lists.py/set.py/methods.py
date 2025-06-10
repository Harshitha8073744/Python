names={"rg","nm","pg","sg"}

names.add("vk")# only for single element
print(names)

unames={"dk","gh"}# values to be updated
names.update(unames)# add multiple values single will give error, expects another sequence
print(names)

#union
s1={20,30,10}
s2={30,40,50,60}

s1.union(s2)# all elements but printed only once we can use union or just s1+s2 or p(s1 | s2)
print(s1.union(s2))

#inersection
print(s1.intersection(s2)) # p(s1 & s2)  instead of p(s1.intersection(s2))

#difference 

print("exclusive s1:",s1-s2)
print("exclusive s2:",s2-s1)
print(s2.difference(s1)) # same as above

#symmetric difference: union of both the exclusive sets i.e  A U B -2(a intersection b) only the exclusive s1 and exclusice s2
print(s1^s2)
print(s1.symmetric_difference(s2))

#delete
s1.clear()
print(s1) # set() --> output
s1.remove(10)# remove specific element
print(s1) # {20,30}-->o/p

s1.pop() # to remove arbitary element, no gaurentee as to which element will be removed. no arguments t be passed like this s1.pop(10)
s1.remove(101)# if element not present then we get key error
s1.discard(101)# no error even if element not present

i=sorted(names)
print(type(i))
print(i)
result=set(i)
print(type(i))