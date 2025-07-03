# list; group of elements as one entity while duplicates and heterogeneous. stored based on indexing

enames=['rahul','sonia','priya','nm'] #creating list
print(enames) 
print(enames[0])# reading the list
print(enames[-1])# indexing of negative starts from the back with -1 as the first
print(type(enames))
for ena in enames:
    print(ena)

#update operation
enames[0]='rahul Gandhi'
print(enames)
print(enames) 


# delete specific element
enames.remove("rahul Gandhi")
print(enames) 


#delete all the elements
enames.clear()
print(enames) 


#delete the object itself
del enames
print(enames) 


